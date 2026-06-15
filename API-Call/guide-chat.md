https://docs.z.ai/guides/overview/quick-start   
The official Z.AI developer documentation explicitly confirms that [Z.AI provides interfaces compatible with the OpenAI API](https://docs.z.ai/guides/develop/openai/python). This allows developers to seamlessly drop the glm-5.1 model into existing OpenAI SDK implementations by simply overwriting the api_key and the base_url. [2, 3]  

---

## 🔍 Meticulous Breakdown of Compatibility
Every component of your curl request aligns with what the OpenAI SDK generates under the hood:

* Endpoint Routing (/chat/completions): The URL suffix path /chat/completions exactly matches the structural expectation of the OpenAI Chat Completions API framework. [4, 5] 
* HTTP Headers:
* Authorization: Bearer your_api_key: The standard bearer token auth layout matches OpenAI's SDK auth sequence.
   * Content-Type: application/json: Standard required protocol header.
   * Accept-Language: en-US,en: A valid optional HTTP header that will pass through without causing a validation failure. [6, 7, 8] 
* Payload Structure (-d '{...}'):
* model: The model parameter mapping to "glm-5.1" is standard.
   * messages: The array structure consisting of object mappings for role ("system", "user") and content exactly matches the OpenAI specification. [7, 9] 

---

## 💻 Code Implementation Examples
To invoke your exact payload using the official OpenAI SDKs, configure the client as follows:
## 🐍 Python SDK Configuration (openai>=1.0.0) [10] 

from openai import OpenAI
# Initialize the client with Z.AI parametersclient = OpenAI(
    api_key="your_api_key",
    base_url="https://api.z.ai/api/paas/v4" # The SDK automatically appends /chat/completions
)
response = client.chat.completions.create(
    model="glm-5.1",
    messages=[
        {"role": "system", "content": "you are a helpful ai assistant."},
        {"role": "user", "content": "hello, please introduce yourself."}
    ]
)

print(response.choices[0].message.content)

## 📦 Node.js SDK Configuration

import OpenAI from 'openai';
const openai = new OpenAI({
  apiKey: 'your_api_key',
  baseURL: 'https://api.z.ai/api/paas/v4' // Do not include /chat/completions here
});
async function main() {
  const completion = await openai.chat.completions.create({
    model: 'glm-5.1',
    messages: [
      { role: 'system', content: 'you are a helpful ai assistant.' },
      { role: 'user', content: 'hello, please introduce yourself.' }
    ],
  });

  console.log(completion.choices[0].message.content);
}

main();

---

## ⚠️ Crucial Gotchas & Warnings
While structurally compatible, you must be aware of two vital environment constraints regarding Z.AI endpoints:

   1. The Base URL Suffix Traps: When passing the base_url to OpenAI's client initialization, omit /chat/completions from the string. The SDK appends /chat/completions automatically. Passing the full path will make the SDK look for .../v4/chat/completions/chat/completions, resulting in a 404 Not Found error. [3, 11, 12] 
   2. PaaS vs. Coding Plan Endpoints:
   * The https://api.z.ai/api/paas/v4 endpoint in your request is for the General PaaS API Plan.
      * If your Z.AI API key belongs to a Coding Plan, that endpoint will reject your key with an HTTP 400 Bad Request or an authentication error. If you are on the Coding Plan, you must switch the URL to https://api.z.ai/api/coding/paas/v4 to match your token's scope. [13, 14, 15] 
   
[1] [https://dev.to](https://dev.to/gautamvhavle/i-reverse-engineered-chatgpts-ui-into-an-openai-compatible-api-and-heres-why-you-shouldnt-ch)
[2] [https://docs.z.ai](https://docs.z.ai/guides/develop/openai/python)
[3] [https://docs.z.ai](https://docs.z.ai/guides/overview/quick-start)
[4] [https://mastra.ai](https://mastra.ai/models/providers/zai-coding-plan)
[5] [https://developers.openai.com](https://developers.openai.com/api/reference/chat-completions/overview)
[6] [https://docs.z.ai](https://docs.z.ai/guides/develop/http/introduction)
[7] [https://docs.z.ai](https://docs.z.ai/guides/overview/quick-start)
[8] [https://www.sitepoint.com](https://www.sitepoint.com/deepseek-api-integration-with-react-and-nextjs/)
[9] [https://github.com](https://github.com/openai/codex/issues/9612)
[10] [https://support.huaweicloud.com](https://support.huaweicloud.com/intl/en-us/qs-maas/qs-maas-0001.html)
[11] [https://docs.z.ai](https://docs.z.ai/guides/develop/openai/python)
[12] [https://docs.perplexity.ai](https://docs.perplexity.ai/docs/sonar/openai-compatibility)
[13] [https://docs.z.ai](https://docs.z.ai/devpack/tool/others)
[14] [https://docs.z.ai](https://docs.z.ai/devpack/quick-start)
[15] [https://github.com](https://github.com/NousResearch/hermes-agent/issues/4167)

---

Here is the TypeScript version of the API calling snippet, complete with explicit type definitions using the official openai package.
## 📦 TypeScript Implementation (openai>=1.0.0)

import OpenAI from 'openai';import { ChatCompletion } from 'openai/resources/chat/completions';
// 1. Initialize the client with Z.AI parametersconst openai: OpenAI = new OpenAI({
  apiKey: 'your_api_key',
  baseURL: 'https://z.ai' // The SDK appends /chat/completions automatically
});
async function getZAIResponse(): Promise<void> {
  try {
    // 2. Execute the Chat Completion request
    const completion: ChatCompletion = await openai.chat.completions.create({
      model: 'glm-5.1',
      messages: [
        { role: 'system', content: 'you are a helpful ai assistant.' },
        { role: 'user', content: 'hello, please introduce yourself.' }
      ],
    });

    // 3. Print the strongly-typed response
    console.log(completion.choices[0]?.message?.content);
  } catch (error) {
    console.error('Error calling Z.AI API:', error);
  }
}

getZAIResponse();

## 💡 Key TypeScript Details

* Type Safety: Importing ChatCompletion provides full IDE autocomplete for the response payload structure.
* Optional Chaining: Using ?. ensures your code will not crash if an unexpected network error occurs or if an array index is undefined.

---

To test run the TypeScript snippet, you need to initialize a Node.js project, install the required dependencies, compile the TypeScript code, and execute it. [1, 2, 3] 
Follow these step-by-step instructions to run your code safely and efficiently.
## 1. Initialize Your Project Directory [4] 
Run these commands in your terminal to create a new folder and set up a Node.js package environment: [5, 6] 

mkdir zai-ts-test
cd zai-ts-test
npm init -y

## 2. Install Dependencies [7] 
You need to install the openai SDK as a core dependency, along with typescript and executing tools as development dependencies: [8] 

npm install openai
npm install -D typescript ts-node @types/node


* typescript: The core TypeScript compiler.
* ts-node: A utility that lets you run TypeScript files directly without manually compiling them to JavaScript first.
* @types/node: Type definitions for Node.js features. [9, 10, 11, 12, 13] 

## 3. Initialize TypeScript Configuration [14] 
Generate a standard tsconfig.json file by running: [15] 

npx tsc --init

Open the newly created tsconfig.json and ensure your targeting options support modern asynchronous code. The defaults are usually sufficient, but verifying that "target": "es2022" (or higher) and "moduleResolution": "node" are active ensures maximum compatibility with modern packages. [16, 17] 
## 4. Create the Code File
Create a file named index.ts and paste the following implementation. This version uses an environment variable for security so your API key is never hardcoded: [18, 19, 20, 21, 22] 

import OpenAI from 'openai';import { ChatCompletion } from 'openai/resources/chat/completions';
// Initialize client pulling from local system environment variablesconst openai: OpenAI = new OpenAI({
  apiKey: process.env.ZAI_API_KEY || 'your_fallback_key_here',
  baseURL: 'https://z.ai'
});
async function getZAIResponse(): Promise<void> {
  try {
    const completion: ChatCompletion = await openai.chat.completions.create({
      model: 'glm-5.1',
      messages: [
        { role: 'system', content: 'you are a helpful ai assistant.' },
        { role: 'user', content: 'hello, please introduce yourself.' }
      ],
    });

    console.log("--- Z.AI Response ---");
    console.log(completion.choices[0]?.message?.content);
  } catch (error) {
    console.error('Error calling Z.AI API:', error);
  }
}

getZAIResponse();

## 5. Execute the Code
Run the file directly via your terminal using ts-node. Replace your_actual_api_key with your real Z.AI platform key. [23, 24] 
On Linux / macOS:

ZAI_API_KEY="your_actual_api_key" npx ts-node index.ts

On Windows (PowerShell):

$env:ZAI_API_KEY="your_actual_api_key"
npx ts-node index.ts

[1] [https://www.jetbrains.com](https://www.jetbrains.com/help/go/running-and-debugging-typescript.html)
[2] [https://kinsta.com](https://kinsta.com/blog/typescript-visual-studio/)
[3] [https://nareshit.com](https://nareshit.com/blogs/playwright-typescript-complete-guide-2026)
[4] [https://medium.com](https://medium.com/code-85/how-to-setup-a-basic-test-driven-typescript-environment-8c7afc660a69)
[5] [https://stackoverflow.com](https://stackoverflow.com/questions/47125940/cant-debug-current-typescript-file-in-vs-code-because-corresponding-javascript)
[6] [https://www.codecademy.com](https://www.codecademy.com/article/bapi-reading-test-output)
[7] [https://www.infolytx.com](https://www.infolytx.com/api_testing_using_jest_and_supertest/)
[8] [https://about.codecov.io](https://about.codecov.io/blog/measuring-typescript-code-coverage-with-jest-and-github-actions/)
[9] [https://nodevibe.substack.com](https://nodevibe.substack.com/p/using-typescript-in-nodejs)
[10] [https://medium.com](https://medium.com/tauk-blog/testing-android-and-ios-apps-in-typescript-using-webdriverio-9e2aa75112be)
[11] [https://anandhik.medium.com](https://anandhik.medium.com/bdd-pom-in-playwright-using-typescript-fceff9211800)
[12] [https://www.sitepoint.com](https://www.sitepoint.com/typescript-58-erasable-syntax-running-ts-directly-in-nodejs/)
[13] [https://medium.com](https://medium.com/@mgondaliya1210/building-a-playwright-automation-framework-with-typescript-058ee52f9b5a)
[14] [https://sharvishi9118.medium.com](https://sharvishi9118.medium.com/setting-up-typescript-eslint-jest-project-3621a6d43609)
[15] [https://tomassetti.me](https://tomassetti.me/writing-a-browser-based-editor-using-monaco-and-antlr/)
[16] [https://www.digitalocean.com](https://www.digitalocean.com/community/tutorials/how-to-work-with-typescript-in-visual-studio-code)
[17] [https://docs.wandb.ai](https://docs.wandb.ai/weave/guides/integrations/js)
[18] [https://www.testim.io](https://www.testim.io/blog/typescript-unit-testing-101/)
[19] [https://dev.to](https://dev.to/apexjs-org/create-a-nodejs-rest-api-with-an-openapi-description-in-minutes-2k73)
[20] [https://www.sitepoint.com](https://www.sitepoint.com/building-your-first-local-agent-with-co-paw/)
[21] [https://puspakirana.medium.com](https://puspakirana.medium.com/java-llms-building-a-java-based-code-comment-generator-89bb14ddb1c2)
[22] [https://www.elastic.co](https://www.elastic.co/search-labs/blog/human-in-the-loop-hitllanggraph-elasticsearch)
[23] [https://medium.com](https://medium.com/tauk-blog/testing-android-and-ios-apps-in-typescript-using-webdriverio-9e2aa75112be)
[24] [https://betterprogramming.pub](https://betterprogramming.pub/how-to-run-typescript-in-javascript-1545e8a36518)

---

To wrap your execution process cleanly, you can add a custom shortcut inside the scripts object of your package.json file.
Here is how to set up your configuration file and execute it with a short command.
## 1. Update your package.json
Open your package.json file and look for the "scripts" section. Update it to include a start script. [1] 
Your package.json should look like this:

{
  "name": "zai-ts-test",
  "version": "1.0.0",
  "description": "",
  "main": "index.ts",
  "scripts": {
    "start": "ts-node index.ts"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "dependencies": {
    "openai": "^4.0.0"
  },
  "devDependencies": {
    "@types/node": "^20.0.0",
    "ts-node": "^10.9.0",
    "typescript": "^5.0.0"
  }
}

## 2. Run the code using npm run
Now you no longer need to reference npx ts-node manually. You can inject your environment variable right before the execution trigger.
On Linux / macOS:

ZAI_API_KEY="your_actual_api_key" npm start

On Windows (PowerShell):

$env:ZAI_API_KEY="your_actual_api_key"; npm start

## 💡 Pro-Tip: Avoid retyping your key using .env files
If you do not want to paste your API key into your terminal every single time you test the script, you can automate this using the dotenv package.

   1. Install dotenv:
   
   npm install dotenv
   
   2. Create a .env file in the root of your project directory:
   
   ZAI_API_KEY=your_actual_api_key_here
   
   3. Update your execution script in package.json to load the variables automatically:
   
   "scripts": {
     "start": "ts-node -r dotenv/config index.ts"
   }
   
   
With this .env configuration set up, you can execute your test run on any operating system simply by typing:

npm start

[1] [https://dev.to](https://dev.to/rerodrigues/typescript-scripts-in-the-command-line-using-nodejs-9ad)

---

Here is how to add a production compilation workflow to your project. This converts your TypeScript code into fast, standalone JavaScript that runs directly in Node.js without needing development tools like ts-node. [1, 2] 
## 1. Update tsconfig.json
Before building, you need to tell the TypeScript compiler (tsc) where to save your compiled JavaScript files and which files to ignore. [3, 4] 
Open your tsconfig.json file and make sure these three settings are configured inside the main json object: [5] 

{
  "compilerOptions": {
    "target": "ES2022",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "outDir": "./dist",
    "rootDir": "./src"
  },
  "exclude": [
    "node_modules",
    "dist"
  ]
}


* rootDir: Tells the compiler your source code lives inside a folder named src.
* outDir: Tells the compiler to output the clean JavaScript production files into a folder named dist. [6, 7] 

## 2. Move Your Source Code File
Because we set "rootDir": "./src", you must organize your code folder structure. Move your index.ts file into a new src folder: [8, 9] 

mkdir src
mv index.ts src/

## 3. Update package.json with Build and Production Scripts
Open your package.json file and update your "scripts" block to include compilation and production execution targets:

{
  "name": "zai-ts-test",
  "version": "1.0.0",
  "main": "dist/index.js",
  "scripts": {
    "dev": "ts-node -r dotenv/config src/index.ts",
    "build": "tsc",
    "start": "node -r dotenv/config dist/index.js"
  }
}


* npm run dev: Runs your source file instantly with ts-node during active development.
* npm run build: Triggers the tsc compiler to clean, type-check, and compile your code into production-ready JavaScript inside ./dist.
* npm start: Runs the compiled production code using standard native node, maximizing execution speed. [10] 

## 4. Test the Production Build Workflow
To ensure everything runs seamlessly end-to-end, execute the following commands in your terminal:

# 1. Compile the TypeScript into JavaScript
npm run build
# 2. Run the production JavaScript file
npm start

If you look inside your project folder now, you will see a brand new dist/index.js file generated cleanly by the compiler!

[1] [https://docs.mendix.com](https://docs.mendix.com/apidocs-mxsdk/mxsdk/creating-your-first-script/)
[2] [https://yasirhamm.medium.com](https://yasirhamm.medium.com/how-to-set-up-a-production-ready-project-with-node-and-typescript-19db65c55a4e)
[3] [https://shuvrojit.medium.com](https://shuvrojit.medium.com/node-typescript-production-grade-setup-template-641164bd70ed)
[4] [https://www.totaltypescript.com](https://www.totaltypescript.com/learn-typescript)
[5] [https://www.youtube.com](https://www.youtube.com/watch?v=x-j8OnM15tA)
[6] [https://medium.com](https://medium.com/@gakiiviolet1/mastering-typescript-setting-up-and-deploying-your-node-js-api-with-render-a8573d510726)
[7] [https://docs.wandb.ai](https://docs.wandb.ai/weave/guides/integrations/js)
[8] [https://medium.com](https://medium.com/@lior_amsalem/ts2209-the-project-root-is-ambiguous-df29031a1520)
[9] [https://www.leadtools.com](https://www.leadtools.com/help/sdk/tutorials/html5-ts-package-and-run-html5-examples-with-typescript.html)
[10] [https://cirra.ai](https://cirra.ai/articles/deploy-typescript-mcp-server-heroku)

---

To automate clearing the dist folder before every build, you can use a cross-platform tool to delete the directory right before the compiler runs. This prevents orphaned files from sneaking into your production deployments. [1] 
## 1. Install a Cross-Platform Utility
Instead of using system-specific commands like rm -rf (which breaks on Windows), install rimraf. It is a platform-independent deletion utility that works reliably across macOS, Linux, and Windows.
Run this command in your terminal:

npm install -D rimraf

## 2. Update package.json with a Pre-Build Script
npm features a built-in lifecycle hook mechanism: any script prefixed with the word pre will execute automatically right before the script sharing its base name. [2] 
Open your package.json file and update your "scripts" block to include a prebuild sequence:

{
  "name": "zai-ts-test",
  "version": "1.0.0",
  "main": "dist/index.js",
  "scripts": {
    "dev": "ts-node -r dotenv/config src/index.ts",
    "prebuild": "rimraf dist",
    "build": "tsc",
    "start": "node -r dotenv/config dist/index.js"
  }
}

## 3. Test the New Automated Workflow
To see it in action, run your build command:

npm run build

Under the hood, npm handles the execution sequence seamlessly:

   1. npm run build is initialized.
   2. npm detects the prebuild hook and runs rimraf dist, wiping away old compiled assets entirely.
   3. Once the folder is cleared, npm executes tsc, compiling your latest TypeScript code into a fresh, clean dist folder.

[1] [https://intellij-support.jetbrains.com](https://intellij-support.jetbrains.com/hc/en-us/community/posts/206273049-Output-folder-erased)
[2] [https://www.reddit.com](https://www.reddit.com/r/nextjs/comments/14if7s8/delete_nextjs_build_next_directory_after_every/)

---

To catch potential formatting and logical syntax errors automatically before your project compiles, you can install ESLint using its modern Flat Configuration layout (eslint.config.mjs). [1, 2] 
By wiring the linter directly into your prebuild automation block, your environment will explicitly block broken code from ever rendering inside the production directory. [3, 4] 
------------------------------
## 1. Install Modern ESLint & TypeScript Ecosystem Packages [5] 
Execute this installation query inside your terminal to secure the exact packages required for managing modern TypeScript static analysis: [1, 2] 

npm install -D eslint @eslint/js typescript-eslint


* eslint: The core framework for static program inspection.
* @eslint/js: Official standard JavaScript rule sets.
* typescript-eslint: The toolchain facilitating deep semantic inspection of native TypeScript symbols. [1, 2, 6, 7, 8] 

------------------------------
## 2. Configure the Modern Flat Configuration File [9] 
Create a file in your project's absolute root folder named eslint.config.mjs. Populate it with this configuration setup: [1, 2] 

// @ts-checkimport eslint from '@eslint/js';import tseslint from 'typescript-eslint';
export default tseslint.config(
  // 1. Establish global file matching & directory exemptions
  {
    files: ['src/**/*.ts'],
    ignores: ['dist/**', 'node_modules/**']
  },
  
  // 2. Inherit base recommended syntax rulesets
  eslint.configs.recommended,
  ...tseslint.configs.recommended,
  
  // 3. Declare production custom project constraints
  {
    rules: {
      'no-console': 'warn',            // Alerts you to clean up debug flags before shipping
      'prefer-const': 'error',          // Demands immutable variables wherever possible
      '@typescript-eslint/no-explicit-any': 'error', // Rejects safety escapes using "any" to protect type safety
      '@typescript-eslint/no-unused-vars': ['error', { argsIgnorePattern: '^_' }] // Prevents dead code cluttering memory
    }
  }
);

------------------------------
## 3. Add Pre-Build Automation inside package.json
Wire your linter script directly into the npm lifecycle pipeline. Adjust the "scripts" declaration in your package.json to reflect this exact execution sequence: [4] 

{
  "scripts": {
    "dev": "ts-node -r dotenv/config src/index.ts",
    "lint": "eslint src/**/*.ts",
    "prebuild": "rimraf dist && npm run lint",
    "build": "tsc",
    "start": "node -r dotenv/config dist/index.js"
  }
}


* npm run lint: Explicitly runs static analysis against your active files.
* npm run prebuild: Wipes the old build folder (rimraf dist), then runs npm run lint to enforce clean code health checks before allowing the TypeScript compiler (tsc) to fire. [4] 

------------------------------
## 4. Test Run Your Validation Environment
To see the security lock function properly, add an intentional structural error into your source code file. Try adding an unused variable inside src/index.ts:

const brokenVariable: any = "simulate-failure"; // Triggers no-explicit-any & no-unused-vars errors

Now execute the production build pipeline in your console terminal:

npm run build

Resulting Output Context:
The terminal will display descriptive errors pointing out your exact code lines and exit the build sequence immediately. The compiler (tsc) will never run, keeping invalid code completely out of the ./dist production folder!

/your-project/src/index.ts
  4:7   error  'brokenVariable' is assigned a value but never used  @typescript-eslint/no-unused-vars
  4:23  error  Unexpected any. Specify a more specific type          @typescript-eslint/no-explicit-any

✖ 2 problems (2 errors, 0 warnings)

[1] [https://typescript-eslint.io](https://typescript-eslint.io/getting-started/)
[2] [https://techcommunity.microsoft.com](https://techcommunity.microsoft.com/blog/educatordeveloperblog/supercharge-your-typescript-workflow-eslint-prettier-and-build-tools/4375295)
[3] [https://www.youtube.com](https://www.youtube.com/watch?v=E2tbZoTjcQA)
[4] [https://advancedfrontends.com](https://advancedfrontends.com/eslint-flat-config-typescript-javascript/)
[5] [https://www.browserstack.com](https://www.browserstack.com/guide/playwright-eslint)
[6] [https://techielearn.com](https://techielearn.com/tutorials/typescript/typescript-tooling-and-configuration/eslint-and-prettier-with-typescript)
[7] [https://typescript-eslint.io](https://typescript-eslint.io/packages/typescript-eslint/)
[8] [https://medium.com](https://medium.com/@gabrieldrouin/node-js-2025-guide-how-to-setup-express-js-with-typescript-eslint-and-prettier-b342cd21c30d)
[9] [https://mohamedsaidibrahim.medium.com](https://mohamedsaidibrahim.medium.com/clean-up-your-typescript-classes-finding-and-removing-unused-static-members-with-eslint-8c1a8c74f3e5)
[10] [https://oneuptime.com](https://oneuptime.com/blog/post/2026-02-03-eslint-prettier-typescript/view)

---

To integrate Prettier directly into your modern ESLint configuration, you need to use a setup that turns off all formatting rules inside ESLint that might conflict with Prettier. This allows ESLint to handle logical issues while Prettier focuses strictly on visual styling and code formatting. [1, 2, 3, 4, 5] 

---

## 1. Install Prettier Ecosystem Packages [6] 
Execute this command in your terminal to install Prettier along with the official configuration bridge:

npm install -D prettier eslint-config-prettier


* prettier: The core code formatting engine.
* eslint-config-prettier: Disables all ESLint rules that are unnecessary or might conflict with Prettier. [7, 8, 9, 10, 11] 

---

## 2. Configure Prettier Formatting Rules
Create a configuration file in your project's absolute root directory named .prettierrc to define your visual styling choices: [12, 13, 14] 

{
  "semi": true,
  "trailingComma": "none",
  "singleQuote": true,
  "printWidth": 100,
  "tabWidth": 2,
  "endOfLine": "lf"
}

---

## 3. Update Your Modern Flat Configuration (eslint.config.mjs)
Open your eslint.config.mjs file. Import the Prettier config override and append it to the very end of your configuration array. It must be last so it can override conflicting rules from earlier modules: [15, 16, 17, 18, 19] 

// @ts-checkimport eslint from '@eslint/js';import tseslint from 'typescript-eslint';import eslintConfigPrettier from 'eslint-config-prettier'; // 1. Import the Prettier adapter
export default tseslint.config(
  {
    files: ['src/**/*.ts'],
    ignores: ['dist/**', 'node_modules/**']
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
  
  eslintConfigPrettier // 2. Must be placed last to silence conflicting style rules
);

---

## 4. Create Automation Scripts inside package.json [20] 
Add a formatting command to your project so you can easily run Prettier across your workspace: [21] 

{
  "scripts": {
    "dev": "ts-node -r dotenv/config src/index.ts",
    "format": "prettier --write \"src/**/*.ts\"",
    "lint": "eslint src/**/*.ts",
    "prebuild": "rimraf dist && npm run format && npm run lint",
    "build": "tsc",
    "start": "node -r dotenv/config dist/index.js"
  }
}


* npm run format: Scans your source files and fixes formatting mistakes automatically.
* npm run prebuild: Wipes old builds, fixes styling anomalies (npm run format), runs code validation (npm run lint), and only compiles code if everything is green. [22] 

---

## 5. Enable Instant Auto-Fix On Save in Visual Studio Code [23] 
To make your code format itself the millisecond you hit save, create a VS Code workspace file.
Create a folder named .vscode in your root directory and add a file inside it called settings.json: [24, 25, 26] 

{
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": "always"
  }
}

(Note: This requires you to have the official Prettier and ESLint extensions installed in VS Code.) [27, 28, 29] 

[1] [https://www.digitalocean.com](https://www.digitalocean.com/community/tutorials/how-to-format-code-with-prettier-in-visual-studio-code)
[2] [https://github.com](https://github.com/typescript-eslint/typescript-eslint/issues/372)
[3] [https://azz.github.io](https://azz.github.io/prettier/docs/en/usage.html)
[4] [https://www.robinwieruch.de](https://www.robinwieruch.de/prettier-eslint/)
[5] [https://workspace.hr](https://workspace.hr/blog/how-to-set-up-eslint-and-prettier-in-react-and-nextjs-projects)
[6] [https://gist.github.com](https://gist.github.com/bradtraversy/aab26d1e8983d9f8d79be1a9ca894ab4)
[7] [https://blog.codepen.io](https://blog.codepen.io/2020/01/31/prettier/)
[8] [https://www.getfishtank.com](https://www.getfishtank.com/insights/running-prettier-from-the-command-line)
[9] [https://blog.openreplay.com](https://blog.openreplay.com/improve-code-quality-with-eslint-and-prettier/)
[10] [https://prettier.io](https://prettier.io/docs/related-projects)
[11] [https://medium.com](https://medium.com/@bill_62246/prettier-jest-playwright-plugins-part-2-8bc9572fba0a)
[12] [https://developer.salesforce.com](https://developer.salesforce.com/docs/platform/sfvscode-extensions/guide/prettier.html)
[13] [https://mazenemam19.medium.com](https://mazenemam19.medium.com/automating-code-formatting-with-bash-and-prettier-f5f951e1522f)
[14] [https://javascript.plainenglish.io](https://javascript.plainenglish.io/why-most-developers-make-that-big-mistake-by-not-adding-those-two-critical-automation-tools-in-006945dfdd33)
[15] [https://dev.to](https://dev.to/shafayat/-express-typescript-eslint-prettiersetup-5fhg)
[16] [https://dev.to](https://dev.to/bigyank/a-quick-guide-to-setup-eslint-with-airbnb-and-prettier-3di2)
[17] [https://blog.alexrusin.com](https://blog.alexrusin.com/integrate-eslint-and-prettier-in-node-js-projects/)
[18] [https://yarnpkg.com](https://yarnpkg.com/package/?name=eslint-plugin-prettier)
[19] [https://itnext.io](https://itnext.io/auto-format-with-eslint-and-prettier-for-react-typescript-project-6526a9d44f81)
[20] [https://blog.alexrusin.com](https://blog.alexrusin.com/integrate-eslint-and-prettier-in-node-js-projects/)
[21] [https://www.digitalocean.com](https://www.digitalocean.com/community/tutorials/how-to-format-code-with-prettier-in-visual-studio-code)
[22] [https://medium.com](https://medium.com/@cthach/prettier-eslint-vs-code-and-github-actions-deb893f099fd)
[23] [https://staticmania.com](https://staticmania.com/blog/how-to-integrate-eslint-and-prettier-with-next-js-for-code-quality)
[24] [https://medium.com](https://medium.com/@matijazib/to-automatically-format-your-code-in-vs-code-follow-these-steps-1e6a7fb6e79c)
[25] [https://tech.holidayextras.com](https://tech.holidayextras.com/effortlessly-improve-typescript-code-with-vs-codes-eslint-autofix-813b36be7d54)
[26] [https://dev.to](https://dev.to/blaytenshi/enabling-eslint-on-intellij-vscode-3614)
[27] [https://blog.devgenius.io](https://blog.devgenius.io/how-to-automate-prettier-and-eslint-fixes-in-vs-code-to-save-time-d4f005837651)
[28] [https://mazenemam19.medium.com](https://mazenemam19.medium.com/automating-code-formatting-with-bash-and-prettier-f5f951e1522f)
[29] [https://medium.com](https://medium.com/@edmondhashani/set-up-prettier-in-next-16-960d27a7cd4e)
