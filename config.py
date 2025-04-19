
import json
import os

CONFIG_FILE = os.path.expanduser("~/.aiclipboard_config.json")

default_config = {
    "model": "ollama",
    "ollama_model": "llama3.2",
    "chatgpt_key": "",
    "chatgpt_model": "gpt-3.5-turbo",
    "gemini_key": "",
    "gemini_model": "gemini-pro"
}

def get_config():
    if not os.path.exists(CONFIG_FILE):
        save_config(default_config)
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)
