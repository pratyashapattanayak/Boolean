import subprocess

def run_llm(prompt):
    # Example: Using Ollama or local Llama.cpp
    result = subprocess.run(
        ["ollama", "run", "llama2", prompt],
        capture_output=True, text=True
    )
    return result.stdout