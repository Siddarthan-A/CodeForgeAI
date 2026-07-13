# 🚀 CodeForgeAI

CodeForgeAI is an AI-powered coding assistant built with Python. It provides a clean desktop interface where developers can chat with an AI, ask programming questions, and upload source code files to receive explanations.

This project combines a modern AI workflow with function calling, making it more than just a chatbot—it acts as an intelligent coding assistant.

---

## ✨ Features

- 💬 AI-powered coding assistant
- 🖥️ Simple desktop GUI built with Tkinter
- 📂 Upload source code files for AI analysis
- 📖 Explain code structure and functionality
- ⚡ Multi-threaded responses (UI remains responsive)
- 🔧 Function-calling AI agent
- 🌐 OpenRouter API integration
- 🔒 Environment variable support using `.env`

---

## 📸 Demo

*(Add screenshots or a GIF here)*

Example:

```
Welcome to CodeForgeAI!

Your AI-powered coding assistant.

Describe what you'd like to build, fix, or understand...
```

---

## 🛠️ Tech Stack

- Python
- Tkinter
- OpenAI Python SDK
- OpenRouter API
- python-dotenv

---

## 📂 Project Structure

```
CodeForgeAI/
│
├── interface.py          # Desktop GUI (Run this file)
├── main.py               # AI Agent
├── call_function.py      # Tool calling logic
├── prompts.py            # System prompt
├── .env                  # API key (Not uploaded)
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Siddarthan-A/CodeForgeAI.git
```

Move into the project

```bash
cd CodeForgeAI
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```
OPENROUTER_API_KEY=your_api_key_here
```

You can obtain an API key from:

https://openrouter.ai/

---

## ▶️ Running the Application

Start the desktop application with:

```bash
python interface.py
```

---

## 💡 How to Use

### Chat with the AI

Simply type your programming question and press **Send**.

Examples:

- Explain Python decorators
- Find the bug in this algorithm
- Generate a REST API
- Optimize this code

---

### Upload a File

1. Click **Upload File**
2. Select a source code file
3. Ask questions such as:

- Explain this file
- What does this function do?
- Can this code be optimized?
- Find possible bugs
- Add documentation

---

## 📈 Current Capabilities

✔ AI Chat

✔ Code Explanation

✔ File Upload

✔ Function Calling

✔ Multi-threading

✔ Modern Desktop Interface

---

## 🔮 Future Improvements

- Project Folder Analysis
- Conversation Memory
- Multiple File Support
- Syntax Highlighting
- Code Refactoring
- AI Code Generation
- Unit Test Generation
- Git Integration
- Multiple AI Model Support

---

## 👨‍💻 Author

**Siddarthan A**

GitHub:
https://github.com/Siddarthan-A

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
