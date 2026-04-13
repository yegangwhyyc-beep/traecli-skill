# TRAE CLI Skill 🚀

[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-blue)](https://docs.openclaw.ai)

TRAE CLI integration for OpenClaw — enable natural language code generation, framework initialization, and automated testing within your AI agent workflow.

---

## 📖 Overview

This skill provides a seamless interface to **TRAE CLI** (ByteDance's AI-powered development tool), allowing you to:

- 🤖 **Generate code** through natural language descriptions
- 🏗️ **Initialize frameworks** (React, Vue, Node.js, Python, etc.)
- ✅ **Build and run automated tests** with conversational prompts
- 🔄 **Iterate development** through AI-powered refinement

---

## 📁 Directory Structure

```
trae-cli/
├── README.md              # This file
├── SKILL.md               # OpenClaw skill definition
└── scripts/
    └── trae_wrapper.py    # Python wrapper for TRAE CLI
```

---

## 🚀 Quick Start

### Prerequisites

1. **Install TRAE CLI** — Ensure `traecli` is installed and in your system PATH
2. **OpenClaw Environment** — This skill requires an OpenClaw agent session

### Installation

Place this skill in your OpenClaw skills directory:

```bash
# For user skills
~/.openclaw/skills/trae-cli/

# Or for system-wide skills
/opt/homebrew/lib/node_modules/openclaw/skills/trae-cli/
```

### Basic Usage

The skill is automatically triggered when you request development tasks that match TRAE CLI capabilities:

```
User: "帮我创建一个 React 待办事项应用"
Agent: [Invokes TRAE CLI skill to initialize React project]

User: "给这个项目添加用户认证功能"
Agent: [Invokes TRAE CLI skill to generate authentication code]

User: "为这个功能写测试并运行"
Agent: [Invokes TRAE CLI skill to build and run tests]
```

---

## 🛠️ Python Wrapper API

The `trae_wrapper.py` script provides a programmatic interface:

```python
from scripts.trae_wrapper import TraeCLI

# Initialize wrapper
trae = TraeCLI(executable="traecli")

# Execute general command
result = trae.execute("Add user authentication with JWT", workdir="./my-app")

# Generate code
result = trae.generate_code("Create a REST API endpoint for user registration", workdir="./my-app")

# Initialize framework
result = trae.init_framework("react", "my-project", workdir="./workspace")

# Build tests
result = trae.build_tests("Test user authentication module", workdir="./my-app")

# Run tests
result = trae.run_tests(workdir="./my-app")

# Check result
if result["success"]:
    print(result["output"])
else:
    print(f"Error: {result['error']}")
```

### Return Format

All methods return a dictionary:

```python
{
    "success": bool,        # Command succeeded?
    "output": str,          # Standard output
    "error": str,           # Error message (if any)
    "return_code": int      # Exit code
}
```

---

## 💡 Use Cases

### 1. Full-Stack Application Development

```
User: "Create a full-stack blog application with React frontend and Node.js backend"
```

**Agent workflow:**
1. Initialize React frontend
2. Initialize Node.js backend
3. Generate API endpoints
4. Generate frontend components
5. Connect frontend to backend

---

### 2. Feature Addition to Existing Project

```
User: "Add dark mode support to this React app"
```

**Agent workflow:**
1. Analyze current project structure
2. Generate theme toggle component
3. Update CSS/styling
4. Run tests to verify

---

### 3. Test-Driven Development

```
User: "Write tests for the payment processing module and ensure they pass"
```

**Agent workflow:**
1. Build test scripts
2. Run tests
3. Debug if failures occur
4. Report coverage

---

### 4. Project Migration

```
User: "Migrate this jQuery project to React"
```

**Agent workflow:**
1. Analyze existing jQuery code
2. Initialize React project
3. Generate equivalent React components
4. Port business logic
5. Verify functionality

---

## ⚙️ Configuration

### Working Directory

Always specify an appropriate working directory:

- **New projects**: Parent directory where the project should be created
- **Existing projects**: The project root directory

```bash
# New project
trae.init_framework("react", "my-app", workdir="./workspace")

# Existing project
trae.generate_code("Add search feature", workdir="./workspace/my-app")
```

### Timeout

The wrapper has a **5-minute timeout** by default to prevent hanging. Adjust in `trae_wrapper.py`:

```python
result = subprocess.run(
    cmd,
    cwd=workdir,
    capture_output=True,
    text=True,
    timeout=300  # Change timeout in seconds
)
```

---

## ⚠️ Limitations & Considerations

1. **TRAE CLI Required** — This skill depends on `traecli` being installed and accessible
2. **Natural Language Clarity** — Prompts should be specific and unambiguous
3. **Complex Operations** — May require multiple iterations for large-scale changes
4. **Timeout** — Long-running operations may trigger the 5-minute timeout
5. **Internet Connection** — TRAE CLI may require network access for AI processing

---

## 🔗 Integrations

This skill works seamlessly with other OpenClaw skills:

| Skill | Integration Pattern |
|-------|---------------------|
| **coding-agent** | Use TRAE CLI as backend for coding tasks |
| **gh-issues** | Build and test fixes for GitHub issues |
| **android-app-programming** | Generate Android app code via TRAE CLI |

---

## 🐛 Troubleshooting

### "TRA-CLI executable not found"

Ensure `traecli` is installed and in your PATH:

```bash
# Verify installation
which traecli

# If not found, install TRAE CLI
# (Follow TRAE CLI official installation guide)
```

### Timeout Errors

- Try breaking large tasks into smaller steps
- Increase timeout in `trae_wrapper.py`
- Provide more specific prompts to reduce processing time

### Code Doesn't Match Requirements

- Refine the natural language prompt with more details
- Specify constraints explicitly (e.g., "use TypeScript", "follow Material Design")
- Request iterative refinement

---

## 📚 Resources

- [OpenClaw Documentation](https://docs.openclaw.ai)
- [OpenClaw Community](https://discord.com/invite/clawd)
- [ClawHub Skills Marketplace](https://clawhub.ai)

---

## 📄 License

This skill is part of OpenClaw and follows its license terms.

---

## 🤝 Contributing

Found a bug or want to add features? Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

---

**Built with ❤️ by the OpenClaw Community**
