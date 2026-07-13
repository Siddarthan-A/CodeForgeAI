# 🤖 CodeForgeAI

An AI-powered coding assistant built using Large Language Models (LLMs) and an agent-based architecture.

CodeForgeAI can understand developer instructions, reason about tasks, and interact with project files using custom tools. It demonstrates how AI agents can automate software development workflows through tool calling and structured execution.

---

# ✨ Features

## 🧠 AI Agent System

* Agent-based workflow for completing coding tasks
* Interprets user instructions and decides required actions
* Uses an iterative reasoning and execution loop
* Handles tasks through structured tool calls

---

## 📂 File Operations

CodeForgeAI can interact with files through dedicated tools:

* Create new files
* Read existing files
* Modify file contents
* Generate code based on requirements

---

## 🔧 Tool Calling Architecture

* Custom tools designed with structured schemas
* Agent dynamically selects required tools
* Modular design allowing new capabilities to be added easily

---

## 💻 Coding Assistance

* Generate code
* Modify existing code
* Explain programming concepts
* Assist with development tasks
* Automate repetitive coding operations

---

# 🏗️ System Architecture

```
                 User Request
                      |
                      ↓
              Agent Controller
                      |
                      ↓
                LLM Model
                      |
        --------------------------------
        |              |               |
        ↓              ↓               ↓
  File Tools     Code Tools      Other Tools
        |
        ↓
   Project Files
```

The agent follows this workflow:

```
User Input
     ↓
Understand Task
     ↓
Plan Action
     ↓
Select Appropriate Tool
     ↓
Execute Tool
     ↓
Analyze Result
     ↓
Complete Task
```

---

# 🛠️ Tech Stack

## Programming Language

* Python

## AI Technologies

* Large Language Models (LLMs)
* AI Agents
* Function Calling
* Prompt Engineering
* Structured Tool Schemas

## Development Tools

* Git
* GitHub
* Virtual Environment

---

# 📁 Project Structure

```
CodeForgeAI/
│
├── agent/
│   ├── agent.py
│   └── prompts.py
│
├── tools/
│   ├── file_tools.py
│   └── schemas.py
│
├── main.py
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## Clone the Repository

```bash
git clone https://github.com/Siddarthan-A/CodeForgeAI.git
```

## Navigate to Project Directory

```bash
cd CodeForgeAI
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

Start CodeForgeAI:

```bash
python main.py
```

---

# 💡 Example Interaction

```
User:
Create a Python program that calculates factorial.

Agent:
Analyzing request...

Selecting tool:
create_file()

Creating factorial.py...

Task completed successfully.
```

---

# 🧩 How It Works

1. The user provides a development task.
2. The agent analyzes the request.
3. The LLM decides the required action.
4. The agent selects the appropriate tool.
5. The tool performs the operation.
6. The result is returned to the agent.
7. The process continues until the task is completed.

---

# 📚 Concepts Learned

This project helped explore:

* How AI agents work internally
* Building tool-based AI systems
* LLM interaction patterns
* Function calling architecture
* Prompt design
* Backend system design
* Automation using AI

---

# 🎯 Project Goal

The goal of CodeForgeAI is to explore how autonomous AI agents can assist developers by combining language understanding, reasoning, and external tools.

This project demonstrates the foundation of AI-powered developer assistants.

---

# 👨‍💻 Author

**Siddarthan A**

B.Tech Student | Backend Development | AI Engineering

GitHub:
https://github.com/Siddarthan-A

---

⭐ If you find this project interesting, consider giving it a star!
