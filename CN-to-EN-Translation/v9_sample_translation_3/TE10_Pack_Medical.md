--- DOMAIN PACK: Medical (v9) ---
VERSION: 1.0
TRIGGER: medical, clinical, patient, dosage, contraindicated, adverse event, trial, 患者, 临床, 剂量, 禁忌, 不良反应

## MODALITY TABLE

| Source Term | Target Term | Direction | Note |
|---|---|---|---|
| suggests | 提示 | EN→CN | Never 证明 |
| indicates | 表明 / 提示 | EN→CN | |
| contraindicated | 禁忌 | EN→CN | |
| associated with | 与……相关 | EN→CN | Never 导致 (correlation ≠ causation) |
| correlates with | 与……相关 | EN→CN | Never 导致 |
| is linked to | 与……存在关联 | EN→CN | Never 引起 |
| significant (statistical) | 具有统计学意义 / 显著性 | EN→CN | Never casual 显著 alone |
| significantly associated with | 与……显著相关（统计学） | EN→CN | Never 与……明显相关 (vague) |
| 提示 | "suggests" | CN→EN | Never "proves" |
| 表明 | "indicates" | CN→EN | |
| 与……相关 | "associated with" / "correlated with" | CN→EN | Never "causes" |
| 导致 | "causes" / "leads to" | CN→EN | Only when source asserts causation |

## COLLOCATION TABLE

| Source Phrase | Target Phrase | Direction | Note |
|---|---|---|---|
| adverse event | 不良事件 | EN→CN | |
| randomized controlled trial | 随机对照试验 | EN→CN | |
| informed consent | 知情同意 | EN→CN | |
| standard of care | 标准治疗方案 | EN→CN | |
| 不良反应 | "adverse reaction" | CN→EN | |
| 临床试验 | "clinical trial" | CN→EN | |
| 预后 | "prognosis" | CN→EN | |

## ANTI-TRANSLATIONESE PAIRS

| Wrong | Correct | Note |
|---|---|---|
| "the drug was found to cause" | "the drug was associated with" | Unless source asserts causation |
| "conduct an examination" | "examine" | Prefer verb form |

--- END DOMAIN PACK ---
