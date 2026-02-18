## Autonomous Orchestration with OpenCode CLI

OpenCode CLI provides robust capabilities for scripting autonomous coding tasks through multiple interfaces: non-interactive mode, headless server API, and session management. For building an orchestrator agent to plan and assign coding sub-tasks, you have three primary architectural approaches. [opencode](https://opencode.ai/docs/cli/)

## Non-Interactive Mode (`opencode run`)

The `opencode run` command executes tasks without launching the TUI, ideal for scripting and automation. [dev.opencode](https://dev.opencode.ai/docs/cli/)

### Basic Usage

```bash
opencode run "Create a REST API endpoint for user authentication"
opencode run --model anthropic/claude-sonnet-4.5 "Refactor the database layer"
opencode run --agent code-reviewer "Review the latest changes"
```

### Key Flags for Orchestration

- `--command`: Execute specific slash commands programmatically (added in response to feature request #2330) [github](https://github.com/sst/opencode/issues/2330)
- `--session/-s`: Continue specific sessions for multi-turn workflows [opencode](https://opencode.ai/docs/cli/)
- `--continue/-c`: Resume the last session [opencode](https://opencode.ai/docs/cli/)
- `--file/-f`: Attach context files to messages [opencode](https://opencode.ai/docs/cli/)
- `--format`: Output in JSON format for parsing (`--format json`) [opencode](https://opencode.ai/docs/cli/)
- `--attach`: Connect to a running server to avoid cold boot times [onedollarvps](https://onedollarvps.com/blogs/how-to-install-and-use-opencode)
- `--agent`: Specify which agent to use [opencode](https://opencode.ai/docs/cli/)
- `--model/-m`: Select the model in `provider/model` format [opencode](https://opencode.ai/docs/cli/)
- `--title`: Set session title for organization [opencode](https://opencode.ai/docs/cli/)

### Orchestration Pattern Example

```bash
# Start server once for faster execution
opencode serve --port 4096 &

# Execute parallel sub-tasks
opencode run --attach http://localhost:4096 --title "Auth Module" "Implement JWT authentication" &
opencode run --attach http://localhost:4096 --title "Database Layer" "Create user model and migrations" &
opencode run --attach http://localhost:4096 --title "API Routes" "Build REST endpoints" &

wait
```

## Headless Server API (`opencode serve`)

The `opencode serve` command exposes a comprehensive HTTP API with an OpenAPI 3.1 specification, enabling full programmatic control. [opencode](https://opencode.ai/docs/server/)

### Server Setup

```bash
# Basic server
opencode serve

# Custom configuration
opencode serve --port 3000 --hostname 0.0.0.0

# With authentication
export OPENCODE_SERVER_PASSWORD="your_password"
opencode serve
```

### Core API Endpoints for Orchestration

**Session Management**: [opencode](https://opencode.ai/docs/server/)
- `POST /session` - Create new sessions for sub-tasks (body: `{parentID?, title?}`)
- `GET /session` - List all sessions
- `GET /session/:id` - Get session details
- `POST /session/:id/fork` - Fork sessions at specific messages for exploration
- `POST /session/:id/abort` - Abort running sessions
- `DELETE /session/:id` - Clean up completed sessions

**Message/Task Execution**: [opencode](https://opencode.ai/docs/server/)
- `POST /session/:id/message` - Send task and wait synchronously (returns `{info, parts}`)
- `POST /session/:id/prompt_async` - Send task asynchronously (returns 204, no wait)
- `POST /session/:id/command` - Execute slash commands (body: `{command, arguments, agent?, model?}`)
- `POST /session/:id/shell` - Run shell commands (body: `{command, agent, model?}`)
- `GET /session/:id/message` - Retrieve message history with limit parameter

**Monitoring & Control**: [opencode](https://opencode.ai/docs/server/)
- `GET /session/status` - Get status of all sessions
- `GET /session/:id/todo` - Retrieve todo items
- `GET /session/:id/diff` - Get file changes
- `GET /event` - Server-sent events stream for real-time updates
- `POST /session/:id/init` - Analyze app and create `AGENTS.md`

### Python Orchestrator Example

```python
import requests
import json

class OpenCodeOrchestrator:
    def __init__(self, base_url="http://localhost:4096"):
        self.base_url = base_url
        self.sessions = {}
    
    def create_session(self, title, parent_id=None):
        """Create a new session for a sub-task"""
        response = requests.post(
            f"{self.base_url}/session",
            json={"title": title, "parentID": parent_id}
        )
        session = response.json()
        self.sessions[title] = session['id']
        return session['id']
    
    def execute_task_sync(self, session_id, prompt, agent=None, model=None):
        """Execute task and wait for completion"""
        payload = {
            "parts": [{"type": "text", "text": prompt}]
        }
        if agent:
            payload["agent"] = agent
        if model:
            payload["model"] = model
        
        response = requests.post(
            f"{self.base_url}/session/{session_id}/message",
            json=payload
        )
        return response.json()
    
    def execute_task_async(self, session_id, prompt, agent=None):
        """Fire-and-forget task execution"""
        payload = {
            "parts": [{"type": "text", "text": prompt}],
            "agent": agent
        }
        requests.post(
            f"{self.base_url}/session/{session_id}/prompt_async",
            json=payload
        )
    
    def monitor_sessions(self):
        """Check status of all sessions"""
        response = requests.get(f"{self.base_url}/session/status")
        return response.json()
    
    def get_session_diff(self, session_id):
        """Get file changes from a session"""
        response = requests.get(f"{self.base_url}/session/{session_id}/diff")
        return response.json()

# Usage
orchestrator = OpenCodeOrchestrator()

# Create parent planning session
plan_id = orchestrator.create_session("Project Planning")
plan_result = orchestrator.execute_task_sync(
    plan_id, 
    "Break down building a todo app into sub-tasks"
)

# Create parallel implementation sessions
auth_id = orchestrator.create_session("Authentication", parent_id=plan_id)
db_id = orchestrator.create_session("Database", parent_id=plan_id)
ui_id = orchestrator.create_session("UI Components", parent_id=plan_id)

# Execute sub-tasks asynchronously
orchestrator.execute_task_async(auth_id, "Implement JWT authentication")
orchestrator.execute_task_async(db_id, "Create database models")
orchestrator.execute_task_async(ui_id, "Build todo list component")

# Monitor progress
while True:
    statuses = orchestrator.monitor_sessions()
    if all(s['status'] == 'idle' for s in statuses.values()):
        break
```

## Multi-Agent Architecture

OpenCode supports advanced multi-agent workflows through plugins and built-in features. [reddit](https://www.reddit.com/r/opencodeCLI/comments/1ojlu01/i_built_an_opencode_plugin_for_multiagent/)

### Built-In Primary & Sub-Agents

OpenCode has native support for primary agents managing sub-agents with shared context: [reddit](https://www.reddit.com/r/opencodeCLI/comments/1ojlu01/i_built_an_opencode_plugin_for_multiagent/)
- Primary agents orchestrate and maintain overview of all sub-agent sessions
- Sub-agents can share context with each other
- Toggle between sessions while they operate
- Configure in `AGENTS.md` documentation

### Session Management Plugin

The `opencode-sessions` plugin provides four orchestration modes: [reddit](https://www.reddit.com/r/opencodeCLI/comments/1ojlu01/i_built_an_opencode_plugin_for_multiagent/)

**Fork Mode**: Explore multiple approaches in parallel
```bash
# In opencode.json
{"plugins": ["op-sessions"]}

# Usage in conversation
"Use session tool to fork three sessions: microservices, monolith, serverless architectures"
```

**Message Mode**: Enable agent-to-agent handoffs within same conversation [reddit](https://www.reddit.com/r/opencodeCLI/comments/1ojlu01/i_built_an_opencode_plugin_for_multiagent/)
- Useful for passing work from planning → implementation → review
- Note: Works best with same provider (e.g., sonnet-4.5)

**New Mode**: Start fresh sessions for clear phase transitions [reddit](https://www.reddit.com/r/opencodeCLI/comments/1ojlu01/i_built_an_opencode_plugin_for_multiagent/)

**Compact Mode**: Compress conversation history with optional agent handoff [reddit](https://www.reddit.com/r/opencodeCLI/comments/1ojlu01/i_built_an_opencode_plugin_for_multiagent/)

### Agent Configuration

Create custom agents with specific system prompts and tools: [opencode](https://opencode.ai/docs/cli/)
```bash
opencode agent create
opencode agent list
```

## Advanced Orchestration Patterns

### Hierarchical Task Decomposition

```python
def decompose_and_execute(orchestrator, high_level_task):
    # Planning phase
    plan_session = orchestrator.create_session("Planning")
    plan_result = orchestrator.execute_task_sync(
        plan_session,
        f"Analyze this task and break into 5-7 sub-tasks: {high_level_task}",
        agent="planner"
    )
    
    # Extract sub-tasks (parse plan_result)
    sub_tasks = extract_subtasks(plan_result)
    
    # Execution phase - parallel workers
    worker_sessions = []
    for task in sub_tasks:
        session_id = orchestrator.create_session(
            task['title'], 
            parent_id=plan_session
        )
        worker_sessions.append(session_id)
        orchestrator.execute_task_async(
            session_id,
            task['description'],
            agent="builder"
        )
    
    # Review phase
    review_session = orchestrator.create_session("Code Review")
    orchestrator.execute_task_sync(
        review_session,
        "Review all changes and provide feedback",
        agent="reviewer"
    )
```

### Event-Driven Monitoring

```python
import sseclient
import requests

def stream_events(base_url="http://localhost:4096"):
    """Monitor all OpenCode events in real-time"""
    response = requests.get(f"{base_url}/event", stream=True)
    client = sseclient.SSEClient(response)
    
    for event in client.events():
        data = json.loads(event.data)
        
        if data['type'] == 'session.created':
            print(f"New session: {data['session']['title']}")
        elif data['type'] == 'message.completed':
            print(f"Task completed in session {data['sessionID']}")
        elif data['type'] == 'file.changed':
            print(f"File modified: {data['path']}")
```

### Shell Script Orchestrator

```bash
#!/bin/bash

# Start server
opencode serve --port 4096 &
SERVER_PID=$!
sleep 2

# Function to create session and get ID
create_session() {
    curl -s -X POST http://localhost:4096/session \
        -H "Content-Type: application/json" \
        -d "{\"title\": \"$1\"}" | jq -r '.id'
}

# Function to execute task
execute_task() {
    SESSION_ID=$1
    PROMPT=$2
    curl -s -X POST "http://localhost:4096/session/${SESSION_ID}/prompt_async" \
        -H "Content-Type: application/json" \
        -d "{\"parts\": [{\"type\": \"text\", \"text\": \"${PROMPT}\"}]}"
}

# Create sessions
AUTH_SESSION=$(create_session "Authentication Module")
DB_SESSION=$(create_session "Database Layer")
API_SESSION=$(create_session "API Endpoints")

# Execute tasks
execute_task $AUTH_SESSION "Implement OAuth2 authentication"
execute_task $DB_SESSION "Design and implement user schema"
execute_task $API_SESSION "Create RESTful API endpoints"

# Monitor until complete
while true; do
    STATUS=$(curl -s http://localhost:4096/session/status)
    BUSY=$(echo $STATUS | jq -r 'to_entries[] | select(.value.status == "busy") | .key' | wc -l)
    
    if [ $BUSY -eq 0 ]; then
        echo "All tasks completed"
        break
    fi
    sleep 5
done

kill $SERVER_PID
```

## Best Practices for Orchestration

### Performance Optimization
1. **Use persistent server**: Start `opencode serve` once and attach via `--attach` to avoid MCP server cold boot times [onedollarvps](https://onedollarvps.com/blogs/how-to-install-and-use-opencode)
2. **Async for parallelism**: Use `/session/:id/prompt_async` for fire-and-forget parallel execution [opencode](https://opencode.ai/docs/server/)
3. **Session forking**: Fork sessions at decision points to explore multiple approaches simultaneously [reddit](https://www.reddit.com/r/opencodeCLI/comments/1ojlu01/i_built_an_opencode_plugin_for_multiagent/)

### Context Management
1. **Parent-child relationships**: Link sessions via `parentID` to maintain hierarchical structure [opencode](https://opencode.ai/docs/server/)
2. **Session titles**: Use descriptive titles for organization and debugging [opencode](https://opencode.ai/docs/cli/)
3. **File attachments**: Pass context files with `--file` flag in CLI or via API [opencode](https://opencode.ai/docs/cli/)
4. **Compact mode**: Use session compression when token limits are reached [reddit](https://www.reddit.com/r/opencodeCLI/comments/1ojlu01/i_built_an_opencode_plugin_for_multiagent/)

### Error Handling
1. **Monitor status**: Poll `/session/status` endpoint regularly [opencode](https://opencode.ai/docs/server/)
2. **Abort capability**: Use `/session/:id/abort` to cancel runaway tasks [opencode](https://opencode.ai/docs/server/)
3. **Event streaming**: Subscribe to `/event` SSE stream for real-time error detection [opencode](https://opencode.ai/docs/server/)
4. **Logging**: Use `/log` endpoint to write orchestrator logs [opencode](https://opencode.ai/docs/server/)

### Security Considerations
1. **Authentication**: Set `OPENCODE_SERVER_PASSWORD` for production deployments [opencode](https://opencode.ai/docs/server/)
2. **CORS configuration**: Use `--cors` flag to restrict browser access [opencode](https://opencode.ai/docs/cli/)
3. **Permissions**: Configure `OPENCODE_PERMISSION` environment variable for tool restrictions [opencode](https://opencode.ai/docs/cli/)

## Environment Variables for Orchestration

Key variables for scripting: [opencode](https://opencode.ai/docs/cli/)
- `OPENCODE_AUTO_SHARE`: Automatically share sessions
- `OPENCODE_CONFIG_CONTENT`: Inline JSON config (useful for containerized deployments)
- `OPENCODE_DISABLE_AUTOUPDATE`: Prevent update checks in CI/CD
- `OPENCODE_CLIENT`: Set client identifier for tracking
- `OPENCODE_EXPERIMENTAL_PLAN_MODE`: Enable planning mode (experimental)

## OpenAPI Specification

The full API specification is available at `http://localhost:4096/doc` when running `opencode serve`, providing detailed schemas for request/response types. This can be used to generate type-safe clients in any language supporting OpenAPI code generation. [opencode](https://opencode.ai/docs/server/)

---

https://www.perplexity.ai/search/please-do-a-deep-dive-research-XIId2L9xRr.BxdBbwDm4hg#0
