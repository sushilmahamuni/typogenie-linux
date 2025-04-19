# 🧞 TypoGenie

![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Mac%20%7C%20Linux-green)
![Status](https://img.shields.io/badge/status-Production--Ready-brightgreen)

> AI-powered clipboard assistant that silently fixes grammar and optimizes code while you copy — then magically improves it when you paste.  
> **Currently Download support only for Linux. For windows file is not signed so download will not work.**

---

## ✨ What is TypoGenie?

TypoGenie runs in the background, monitoring your clipboard.  
When you copy text (Ctrl+C), it automatically:
- Fixes grammar and spelling using AI
- Replaces the clipboard with the improved version
- Lets you paste cleaner, smarter text (Ctrl+V)

It's like having a personal AI genie at your fingertips. 🧞‍♂️

---

## 🔧 System Dependencies


Make sure you have X11 Session. you can check like below,
  echo $XDG_SESSION_TYPE
  X11


sudo apt update
pip install pynput pyperclip
sudo apt install python3-tk
sudo apt install python3-dev
pip install pynput
sudo apt install xclip


## 🧰 Setup Instructions

### 1️⃣ Install Ollama Locally
- First, install the Ollama application from the official website or using:
    sudo snap install ollama

- Then, pull the model you want. For example:
    ollama pull llama3.2

Note: Model compatibility depends on your system configuration.
Please choose a model best suited for your hardware.
You can ask ChatGPT or Gemini to suggest the most compatible Ollama models based on your CPU specs.

2️⃣ Start Ollama
- After installation, ensure the Ollama server is running:
    ollama serve

- Then run the following command (it will auto-download the model if not already present):
    ollama run llama3.2

3️⃣ Run TypoGenie
- Make sure Python 3.10 is installed.
- Install required dependencies:
   pip install -r requirements.txt
- Then run TypoGenie:
   python main.py
- From the popup menu, click the settings icon ⚙️ and enter your model name (e.g., llama3.2).
- If you're using ChatGPT or Gemini, make sure to enter your API key.
- If you're using Ollama, no key is needed — just the model name.

🎉 Congratulations! TypoGenie is now running in the background and will automatically fix your copied text!
---

## ⚙️ Settings Panel

Click the ⚙️ icon in the popup to:
- Choose your AI model: **Ollama**, **ChatGPT**, or **Gemini**
- Enter API keys if using ChatGPT/Gemini
- Customize default settings

---

## ⌨️ Hotkeys

| Key Combo          | Action                       |
|--------------------|------------------------------|
| `Ctrl + C`         | Copy (TypoGenie will correct)|
| `Ctrl + E`         | Toggle TypoGenie on/off      |

---

## 🧠 Smart Behavior

- Ignores very short or unimportant clipboard text
- Automatically skips re-correction of already processed text
- Corrects silently without interrupting your workflow

---

## 🔒 Privacy First

- All corrections happen **locally** by default (Ollama)
- API-based models (ChatGPT, Gemini) only activate when you choose them from settings
- **Your clipboard is never shared online** unless you configure it that way

---

## 💬 Feedback & Contributions

Have feedback or want to contribute?  
Open an issue, fork the repo, or submit a pull request!

---

### © 2024 TypoGenie – Your text, your magic. 🧞‍♂️
