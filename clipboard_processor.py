
import pyperclip
import time
import re
from model_handlers import get_corrected_text

cache = {
    "last_input": None,
    "last_output": None
}

def count_meaningful_tokens(text):
    clean_text = text.strip()
    tokens = re.findall(r"\b[\w'-]+\b", clean_text)
    return len(tokens)

def is_more_than_two_words(text):
    token_count = count_meaningful_tokens(text)
    print(f"🧩 Token count: {token_count}")
    return token_count > 2

def process_clipboard(popup):
    time.sleep(0.2)
    text = pyperclip.paste()
    if not isinstance(text, str) or not text.strip():
        return

    print(f"📋 Detected copied text:\n{text}\n")

    if not is_more_than_two_words(text):
        print("⚠️ Text has two or fewer words. Skipping processing.\n")
        popup.update_message("⚠️ Text too short. Skipped.")
        return

    popup.update_message("⚙️ Processing Clipboard...")
    corrected_text = get_corrected_text(text)

    if corrected_text != text:
        pyperclip.copy(corrected_text)
        print(f"✅ Clipboard updated with corrected text:\n{corrected_text}\n")
        popup.update_message("✅ Clipboard Processed!")
        popup.update_message("✅ Press Ctrl+V to paste")
    else:
        print("ℹ️ No corrections were necessary.\n")
        popup.update_message("ℹ️ No corrections needed or Error")
