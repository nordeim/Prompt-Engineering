# SKILL: zai-api-scaffold-test

## Metadata
- **Name**: Z.AI API Scaffold & Test
- **Description**: Autonomously scaffolds, configures, and validates Z.AI (`glm-5.1`) API integrations using OpenAI-compatible SDKs across Python 3.12+, JavaScript, and Production-Grade TypeScript.
- **Triggers**: "Z.AI API", "glm-5.1", "OpenAI compatible Z.AI", "scaffold Z.AI integration"
- **Target Environments**: Python 3.12+, Node.js 18+, TypeScript 5.0+

---

## ⚠️ CORE DIRECTIVES (ANTI-FAIL LAYER)
*You must strictly adhere to these rules. Violating them will result in immediate API failure.*

1. **THE BASE URL TRAP**: NEVER include `/chat/completions` in the `baseURL` or `base_url` string. The OpenAI SDK automatically appends this path. Providing it manually results in a malformed URL (`.../v4/chat/completions/chat/completions`) and a `404 Not Found` error.
2. **ENDPOINT SCOPE MATCHING**: 
   - Use `https://api.z.ai/api/paas/v4` for **General PaaS API Plans**.
   - Use `https://api.z.ai/api/coding/paas/v4` for **Coding Plans**. 
   - Mismatching the key scope to the endpoint yields an `HTTP 400 Bad Request` or authentication failure.
3. **ZERO HARDCODING**: NEVER hardcode API keys. Always enforce `.env` file usage and `python-dotenv` / `dotenv` packages.
4. **TYPE SAFETY (TS Only)**: Never use `any`. Use strict TypeScript configurations and explicit OpenAI SDK types (e.g., `ChatCompletion`).

---

## 🐍 WORKFLOW 1: Python 3.12+

### 1. Scaffold Environment
```bash
mkdir zai-python-test && cd zai-python-test
python3.12 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install openai>=1.0.0 python-dotenv
```

### 2. Configuration (`.env`)
Create a `.env` file in the root directory:
```env
ZAI_API_KEY=your_actual_api_key_here
ZAI_BASE_URL=https://api.z.ai/api/paas/v4
```
*Add `.env` and `.venv/` to `.gitignore`.*

### 3. Implementation (`main.py`)
```python
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_zai_response() -> None:
    api_key = os.getenv("ZAI_API_KEY")
    base_url = os.getenv("ZAI_BASE_URL", "https://api.z.ai/api/paas/v4")
    
    if not api_key:
        raise ValueError("ZAI_API_KEY is not set in the environment.")

    # Initialize client (SDK auto-appends /chat/completions)
    client = OpenAI(
        api_key=api_key,
        base_url=base_url
    )

    try:
        response = client.chat.completions.create(
            model="glm-5.1",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": "Hello, please introduce yourself."}
            ]
        )
        
        # Early return / safe access
        content = response.choices[0].message.content
        print("--- Z.AI Response ---")
        print(content)
        
    except Exception as error:
        print(f"Error calling Z.AI API: {error}")

if __name__ == "__main__":
    get_zai_response()
```

### 4. Validation
```bash
python main.py
```
*Success Criteria: Console prints the AI's introduction without `404` or `400` errors.*

---

## 📦 WORKFLOW 2: JavaScript (Node.js)

### 1. Scaffold Environment
```bash
mkdir zai-js-test && cd zai-js-test
npm init -y
npm install openai dotenv
```

### 2. Configuration (`.env`)
```env
ZAI_API_KEY=your_actual_api_key_here
ZAI_BASE_URL=https://api.z.ai/api/paas/v4
```

### 3. Implementation (`index.js`)
```javascript
import 'dotenv/config';
import OpenAI from 'openai';

const apiKey = process.env.ZAI_API_KEY;
const baseURL = process.env.ZAI_BASE_URL || 'https://api.z.ai/api/paas/v4';

if (!apiKey) {
    console.error('FATAL: ZAI_API_KEY is not set in the environment.');
    process.exit(1);
}

const openai = new OpenAI({
    apiKey: apiKey,
    baseURL: baseURL // SDK auto-appends /chat/completions
});

async function getZAIResponse() {
    try {
        const completion = await openai.chat.completions.create({
            model: 'glm-5.1',
            messages: [
                { role: 'system', content: 'You are a helpful AI assistant.' },
                { role: 'user', content: 'Hello, please introduce yourself.' }
            ]
        });

        console.log('--- Z.AI Response ---');
        console.log(completion.choices[0]?.message?.content || 'No content returned.');
    } catch (error) {
        console.error('Error calling Z.AI API:', error.message || error);
    }
}

getZAIResponse();
```
*Note: Ensure `"type": "module"` is added to `package.json` to support ES Modules.*

### 4. Validation
```bash
node index.js
```

---

## 💎 WORKFLOW 3: TypeScript (Production-Grade)

### 1. Scaffold & Dependencies
```bash
mkdir zai-ts-test && cd zai-ts-test
npm init -y
npm install openai dotenv
npm install -D typescript ts-node @types/node rimraf eslint @eslint/js typescript-eslint prettier eslint-config-prettier
```

### 2. Configuration Files

**`tsconfig.json`**
```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "noImplicitAny": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  },
  "exclude": ["node_modules", "dist"]
}
```

**`.prettierrc`**
```json
{
  "semi": true,
  "trailingComma": "none",
  "singleQuote": true,
  "printWidth": 100,
  "tabWidth": 2,
  "endOfLine": "lf"
}
```

**`eslint.config.mjs`**
```javascript
import eslint from '@eslint/js';
import tseslint from 'typescript-eslint';
import eslintConfigPrettier from 'eslint-config-prettier';

export default tseslint.config(
  {
    files: ['src/**/*.ts'],
    ignores: ['dist/', 'node_modules/']
  },
  eslint.configs.recommended,
  ...tseslint.configs.recommended,
  {
    rules: {
      'no-console': 'warn',
      'prefer-const': 'error',
      '@typescript-eslint/no-explicit-any': 'error',
      '@typescript-eslint/no-unused-vars': ['error', { argsIgnorePattern: '^_' }]
    }
  },
  eslintConfigPrettier // Must be last to silence conflicting style rules
);
```

**`.vscode/settings.json`** (Create `.vscode` folder first)
```json
{
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": "explicit"
  }
}
```

### 3. Implementation (`src/index.ts`)
```typescript
import 'dotenv/config';
import OpenAI from 'openai';
import { ChatCompletion } from 'openai/resources/chat/completions';

interface MessagePayload {
  role: 'system' | 'user' | 'assistant';
  content: string;
}

const apiKey = process.env.ZAI_API_KEY;
const baseURL = process.env.ZAI_BASE_URL || 'https://api.z.ai/api/paas/v4';

if (!apiKey) {
  throw new Error('FATAL: ZAI_API_KEY is not set in the environment.');
}

const openai: OpenAI = new OpenAI({
  apiKey,
  baseURL, // SDK auto-appends /chat/completions
});

async function getZAIResponse(): Promise<void> {
  const messages: MessagePayload[] = [
    { role: 'system', content: 'You are a helpful AI assistant.' },
    { role: 'user', content: 'Hello, please introduce yourself.' }
  ];

  try {
    const completion: ChatCompletion = await openai.chat.completions.create({
      model: 'glm-5.1',
      messages,
    });

    const content = completion.choices[0]?.message?.content;
    
    if (!content) {
      console.warn('Warning: API returned empty content.');
      return;
    }

    console.log('--- Z.AI Response ---');
    console.log(content);
  } catch (error: unknown) {
    const errorMessage = error instanceof Error ? error.message : 'Unknown error occurred';
    console.error('Error calling Z.AI API:', errorMessage);
  }
}

// Execute
getZAIResponse().catch((err) => {
  console.error('Unhandled promise rejection:', err);
  process.exit(1);
});
```

### 4. Automation Scripts (`package.json`)
Update the `"scripts"` block:
```json
{
  "name": "zai-ts-test",
  "version": "1.0.0",
  "main": "dist/index.js",
  "type": "module",
  "scripts": {
    "dev": "ts-node -r dotenv/config src/index.ts",
    "format": "prettier --write \"src/**/*.ts\"",
    "lint": "eslint \"src/**/*.ts\"",
    "prebuild": "rimraf dist && npm run format && npm run lint",
    "build": "tsc",
    "start": "node -r dotenv/config dist/index.js"
  }
}
```

### 5. Validation Sequence
Execute the following commands in order. The agent must verify each succeeds before proceeding:
```bash
# 1. Verify linting and formatting pass (prebuild hook)
npm run build

# 2. Execute production-compiled code
npm start
```
*Success Criteria: `dist/` folder is generated cleanly, ESLint reports 0 errors, and the Node process outputs the AI response.*

---

## ✅ AGENT VALIDATION CHECKLIST
*Before declaring this task complete, you must mentally verify:*
- [ ] Did I omit `/chat/completions` from all `baseURL` / `base_url` configurations?
- [ ] Did I confirm the user's Z.AI plan (PaaS vs. Coding) and apply the correct endpoint?
- [ ] Are all API keys strictly loaded via `.env` and `.gitignore`'d?
- [ ] (TypeScript only) Did I enforce `strict: true` and avoid the `any` type?
- [ ] Did I include early returns and explicit error handling (`try/catch` or `.catch()`)?
- [ ] Did I verify the `prebuild` script successfully runs `rimraf`, `prettier`, and `eslint` before `tsc`?
