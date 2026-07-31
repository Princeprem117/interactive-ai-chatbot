# 🤖 AI Chatbot using Groq API

A simple terminal-based AI chatbot built with **Python** and the **Groq API**. The chatbot remembers previous conversations between **The User** and **Bot** by storing chat history in a JSON file. **Bot** response to the **User** by revewing the previous conversations and gives the concise Answers..

---

## ✨ Features

- 💬 Multi-turn conversations
- 🧠 Conversation memory
- 💾 Persistent chat history
- 🔐 Secure API key using `.env`
- ⚡ Powered by Groq API
- 🤖 Uses the `openai/gpt-oss-120b` model

---

## 🛠 Technologies Used

- Python
- Groq Python SDK
- python-dotenv
- JSON

---

## 📂 Project Structure

```text
chatbot_Groq_proj/
│
├── chat_history/
│   └── history.json
├── .env
├── .gitignore
├── First_Chatbot.py
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/your-username/your-repository.git
```

### Go into the project folder

```bash
cd chatbot_Groq_proj
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate it

Windows:

```bash
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```text
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the chatbot

```bash
python First_Chatbot.py
```

---

## 💬 Example

```
You: Hello
Bot: Hello! How can I help you today?

You: What is Python?
Bot: Python is a popular programming language...

You: quit
Goodbye!
```

---

## 📌 Future Improvements

- Streaming responses
- Multiple chat sessions
- Voice input
- GUI using Tkinter
- Web version using Flask/FastAPI
- Tool calling (Weather, Calculator, Search)

---

## 👨‍💻:

Prince Prem