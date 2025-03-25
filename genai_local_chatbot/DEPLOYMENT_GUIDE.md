# 🚀 Deployment Guide - GenAI Local KB Chatbot (No Cloud)

## 🛠 Prerequisites
- Python 3.9+ installed
- Ollama / llama.cpp / GPT4All installed for local LLM execution
- Virtual environment (optional but recommended)

## 📦 Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 🗂 Generate Vector Index
```bash
python faiss_index.py
```

## 🧠 Run the Flask API
```bash
python app.py
```

## 🌐 Test API with CURL
```bash
curl -X POST http://localhost:5000/chat -H "Content-Type: application/json" -d '{"issue": "Disk usage is high", "dry_run": true}'
```

## 🎨 Run the Streamlit UI (Optional)
```bash
streamlit run streamlit_app.py
```

## ⚠ Notes
- `.env` stores local model configs like `LLM_MODEL=llama2`
- Dry-run mode prevents accidental execution of dangerous commands.
- Risky commands like `rm` require approval checkpoint.

## ✅ Done! Your local GenAI chatbot is running without any cloud tools.