# Medical Assistant: Ready-to-run Training Pipeline

This document contains a complete, ready-to-run training pipeline for fine-tuning an open-source LLM for your Medical Assistant AI Agent. It includes:

- `Dockerfile` — reproducible container with CUDA, NVIDIA drivers, and required Python packages.
- `requirements.txt` — pinned Python dependencies.
- `deepspeed_config.json` — recommended DeepSpeed ZeRO-3 config for large-model training.
- `train.py` — LoRA + k-bit quantization + PEFT training script using Hugging Face Transformers, PEFT, bitsandbytes, and DeepSpeed/Accelerate.
- `train_scheduler.sh` — example scheduler script (slurm-friendly) to launch the training with DeepSpeed.
- `README` — quick run instructions and notes on customization.

---

## README (Quick start)

1. Edit environment variables in `train_scheduler.sh` (MODEL_NAME, DATA_PATH, OUTPUT_DIR, NUM_GPUS etc.).
2. Build the Docker image:

```bash
# from repo root
docker build -t med-assistant-train:latest .
```

3. Run on a multi-GPU node (example using slurm):

```bash
sbatch train_scheduler.sh
```

4. Monitor logs in the output directory. The script will save PEFT weights (LoRA) separately from the base model.

---

## Dockerfile

```Dockerfile
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive

# Basic utilities
RUN apt-get update && apt-get install -y --no-install-recommends \
    git build-essential curl ca-certificates wget unzip python3-venv python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Python setup
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN python -m pip install --upgrade pip

# Copy requirements and install
COPY requirements.txt /workspace/requirements.txt
RUN pip install --no-cache-dir -r /workspace/requirements.txt

# Create workdir
WORKDIR /workspace

# Default entry
ENTRYPOINT ["/bin/bash"]
```

---

## requirements.txt

```
transformers>=4.35.0
accelerate>=0.20.3
peft>=0.4.0
bitsandbytes>=0.39.0
datasets>=2.12.0
safetensors
sentence-transformers
chromadb
faiss-cpu
deepspeed>=0.9.0
torch>=2.1.0
protobuf<=3.20.3
huggingface_hub
```

Notes: Pin versions as needed for your infra. If using GPUs with specific CUDA versions, align `torch`/`bitsandbytes` builds accordingly.

---

## deepspeed_config.json

```json
{
  "train_micro_batch_size_per_gpu": 1,
  "gradient_accumulation_steps": 8,
  "optimizer": {
    "type": "AdamW",
    "params": {"lr": 2e-4, "betas": [0.9, 0.999], "eps": 1e-8}
  },
  "fp16": {"enabled": true},
  "zero_optimization": {
    "stage": 3,
    "offload_optimizer": {"device": "cpu"},
    "offload_param": {"device": "cpu"}
  },
  "wall_clock_breakdown": false
}
```

Adjust `offload_*` settings based on available CPU memory and NVMe.

---

## train.py

```python
"""
train.py
LoRA + k-bit quantization + PEFT training script.

Key features:
- Loads a base causal LM (supports TrustRemoteCode models)
- Prepares model for k-bit training using `prepare_model_for_kbit_training`
- Wraps model with LoRA via PEFT
- Uses Hugging Face Trainer with DeepSpeed integration OR Accelerate/Trainer depending on your cluster

USAGE:
  python train.py \
    --model_name_or_path <MODEL> \
    --data_path <JSONL> \
    --output_dir ./runs/med-lora \
    --per_device_train_batch_size 1 \
    --gradient_accumulation_steps 8

"""
import argparse
import os
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments, DataCollatorForLanguageModeling
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training, get_peft_model_state_dict
import torch


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument('--model_name_or_path', type=str, required=True)
    p.add_argument('--data_path', type=str, required=True)
    p.add_argument('--output_dir', type=str, default='./output')
    p.add_argument('--per_device_train_batch_size', type=int, default=1)
    p.add_argument('--gradient_accumulation_steps', type=int, default=8)
    p.add_argument('--num_train_epochs', type=int, default=3)
    p.add_argument('--learning_rate', type=float, default=2e-4)
    p.add_argument('--max_seq_len', type=int, default=2048)
    p.add_argument('--use_deepspeed', action='store_true')
    p.add_argument('--deepspeed_config', type=str, default='deepspeed_config.json')
    return p.parse_args()


def build_prompt(example):
    # Expect example to have 'instruction' and 'response' fields (jsonl template)
    return example['instruction'] + example.get('response', '')


def prepare_dataset(tokenizer, data_path, max_seq_len=2048):
    ds = load_dataset('json', data_files={'train': data_path}, split='train')
    def tokenize_fn(ex):
        prompt = build_prompt(ex)
        out = tokenizer(prompt, truncation=True, max_length=max_seq_len, padding='max_length')
        out['labels'] = out['input_ids'].copy()
        return out
    tokenized = ds.map(tokenize_fn, batched=False, remove_columns=ds.column_names)
    return tokenized


if __name__ == '__main__':
    args = parse_args()
    os.makedirs(args.output_dir, exist_ok=True)

    print('Loading tokenizer...')
    tokenizer = AutoTokenizer.from_pretrained(args.model_name_or_path, use_fast=True)
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token = tokenizer.eos_token

    print('Loading model...')
    model = AutoModelForCausalLM.from_pretrained(
        args.model_name_or_path,
        load_in_8bit=True,  # bitsandbytes 8-bit quantization
        device_map='auto',
        trust_remote_code=True
    )

    print('Preparing model for k-bit training...')
    model = prepare_model_for_kbit_training(model)

    print('Applying LoRA...')
    lora_config = LoraConfig(
        r=32,
        lora_alpha=128,
        target_modules=['q_proj','v_proj','k_proj','o_proj'],
        lora_dropout=0.05,
        bias='none',
        task_type='CAUSAL_LM'
    )
    model = get_peft_model(model, lora_config)

    # Optional: print trainable params
    trainable_params = 0
    total_params = 0
    for n, p in model.named_parameters():
        total_params += p.numel()
        if p.requires_grad:
            trainable_params += p.numel()
    print(f'Trainable params: {trainable_params} / {total_params}')

    print('Preparing dataset...')
    train_dataset = prepare_dataset(tokenizer, args.data_path, max_seq_len=args.max_seq_len)

    data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

    training_args = TrainingArguments(
        output_dir=args.output_dir,
        per_device_train_batch_size=args.per_device_train_batch_size,
        gradient_accumulation_steps=args.gradient_accumulation_steps,
        num_train_epochs=args.num_train_epochs,
        learning_rate=args.learning_rate,
        fp16=True,
        logging_steps=50,
        save_total_limit=3,
        save_strategy='steps',
        save_steps=500,
        remove_unused_columns=False,
        optim='adamw_torch'
    )

    if args.use_deepspeed:
        training_args.deepspeed = args.deepspeed_config

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        data_collator=data_collator,
        tokenizer=tokenizer
    )

    print('Starting training...')
    trainer.train()

    # Save only PEFT weights
    print('Saving PEFT adapter...')
    peft_path = os.path.join(args.output_dir, 'lora_adapter')
    model.save_pretrained(peft_path)
    print('Done.')
```

Notes:
- `load_in_8bit=True` uses BitsAndBytes. Make sure CUDA/bnb builds are compatible.
- For very large models (>30B), prefer to start via `deepspeed` launcher rather than `Trainer` due to device_map complexities.

---

## train_scheduler.sh (example slurm + deepspeed launcher)

```bash
#!/bin/bash
#SBATCH --job-name=med-lora
#SBATCH --gres=gpu:8
#SBATCH --cpus-per-task=16
#SBATCH --mem=190G
#SBATCH --time=72:00:00
#SBATCH --output=logs/train_%j.out

# User-editable variables
MODEL_NAME_OR_PATH="/path/to/base/model"  # e.g. meditron-70b or a smaller 7b fallback
DATA_PATH="/data/instruction_dataset.jsonl"
OUTPUT_DIR="/output/med_lora_run"
NUM_NODES=1
GPUS_PER_NODE=8
DEEPSPEED_CONFIG="/workspace/deepspeed_config.json"

mkdir -p ${OUTPUT_DIR}

# Activate conda/venv if needed
# source /opt/conda/etc/profile.d/conda.sh
# conda activate medenv

# Run via deepspeed
deepspeed --num_nodes ${NUM_NODES} --num_gpus ${GPUS_PER_NODE} \
  train.py \
  --model_name_or_path ${MODEL_NAME_OR_PATH} \
  --data_path ${DATA_PATH} \
  --output_dir ${OUTPUT_DIR} \
  --per_device_train_batch_size 1 \
  --gradient_accumulation_steps 8 \
  --num_train_epochs 3 \
  --use_deepspeed \
  --deepspeed_config ${DEEPSPEED_CONFIG}
```

Notes:
- Change `--gres` and memory flags according to your cluster.
- If using a single-node GPU with `torchrun`, you can instead use `accelerate launch` or `torchrun --nproc_per_node=NUM_GPUS train.py ...` depending on preference.

---

## Operational & safety hooks

- Insert a preprocessing hook in `prepare_dataset` that validates de-identification and ensures that PHI tokens are replaced consistently.
- Add a callback in `Trainer` to run safety filter checks on generated samples every `n` steps and log to `safety_failures.jsonl`.
- Always save only adapter weights to `lora_adapter/` and do NOT publish base model weights.

---

## Troubleshooting checklist
- If CUDA OOM: reduce batch size, increase gradient_accumulation_steps, enable ZeRO offload or NVMe offload.
- If bitsandbytes import fails: ensure compatible CUDA/Torch/bitsandbytes builds and that `libbitsandbytes.so` is accessible.
- Verify `transformers` and `peft` versions for API compatibility.

---

## Next steps & customization
- I can produce a smaller `demo_train.py` configured for an 8GB GPU (Mistral/7B) so you can sanity-check locally.
- I can produce a `safety_callback.py` hooking into Trainer to enforce medical-safety constraints and automatic escalation triggers.

---

*End of training pipeline v1.*

