# GenAI Local KB Chatbot 🚀 (No Cloud Version)

## Features
✅ Local LLM Execution (Ollama / llama.cpp)  
✅ FAISS Vector Search  
✅ Dry-run & Risky Command Approval  
✅ Streamlit Frontend  

## Usage
1. Install dependencies: `pip install -r requirements.txt`
2. Generate FAISS index: `python faiss_index.py`
3. Run API: `python app.py`
4. Optional UI: `streamlit run streamlit_app.py`

## Example Call
```bash
curl -X POST http://localhost:5000/chat -H "Content-Type: application/json" -d '{"issue": "Disk usage is high", "dry_run": true}'
```