from flask import Flask, request, jsonify
import faiss, pickle, json
from sentence_transformers import SentenceTransformer
from llm_runner import run_llm

app = Flask(__name__)
model = SentenceTransformer('all-MiniLM-L6-v2')
index = faiss.read_index('vector.index')
kb = pickle.load(open('kb_data.pkl', 'rb'))

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    issue = data['issue']
    dry_run = data.get('dry_run', True)

    query_vec = model.encode([issue])
    _, I = index.search(query_vec, 1)
    selected_kb = kb[I[0][0]]

    actions = []
    for step in selected_kb['steps']:
        if 'rm' in step:
            actions.append(f"❗ Approval needed for: {step}")
            continue
        if dry_run:
            actions.append(f"[Dry-run] {step}")
        else:
            actions.append(f"Executing: {step}")
            # subprocess.run(step, shell=True)

    response = "\n".join(actions)
    llm_response = run_llm(f"Issue: {issue}\nResolution Steps:\n{response}")
    return jsonify({"steps": response, "llm_summary": llm_response})

if __name__ == '__main__':
    app.run(debug=True)