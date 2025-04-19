import requests
from config import get_config

def get_corrected_text(text):
    config = get_config()
    model = config.get("model")
    if model == "ollama":
        return correct_text_with_ollama(text, config.get("ollama_model", "llama3"))
    elif model == "chatgpt":
        return correct_text_with_chatgpt(text, config.get("chatgpt_key"), config.get("chatgpt_model", "gpt-3.5-turbo"))
    elif model == "gemini":
        return correct_text_with_gemini(text, config.get("gemini_key"), config.get("gemini_model", "gemini-pro"))
    return text

def correct_text_with_ollama(text, model):
    if not model:
        print("⚠️ model key is missing.")
        return text
    try:
        response = requests.post("http://localhost:11434/api/generate", json={
            "model": model,
            "prompt": f"Correct the grammar and spelling of this text. Only output the corrected sentence, no explanation, no extra words:\\n{text}",
            "stream": False
        }, timeout=120)
        return response.json()["response"].strip()
    except Exception as e:
        print(f"⚠️ Ollama error: {e}")
        return text

def correct_text_with_chatgpt(text, api_key, model):
    if not api_key or not model:
        print("⚠️ ChatGPT API Key or model key is missing.")
        return text
    try:
        headers = {"Authorization": f"Bearer {api_key}"}
        payload = {
            "model": model,
            "messages": [{"role": "user", "content": f"Correct the grammar and spelling of this text. Only output the corrected sentence, no explanation, no extra words:\\n{text}"}]
        }
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
        return response.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"⚠️ ChatGPT error: {e}")
        return text

def correct_text_with_gemini(text, api_key, model):
    if not api_key or not model:
        print("⚠️ Gemini API key or model key is missing.")
        return text
    try:
        headers = {"Authorization": f"Bearer {api_key}"}
        payload = {
            "contents": [{"parts": [{"text": f"Correct the grammar and spelling of this text. Only output the corrected sentence, no explanation, no extra words:\\n{text}"}]}]
        }
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
        response = requests.post(url, headers=headers, json=payload)
        return response.json()["candidates"][0]["content"]["parts"][0]["text"].strip()
    except Exception as e:
        print(f"⚠️ Gemini error: {e}")
        return text
