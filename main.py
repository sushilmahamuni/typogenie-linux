import threading
import tkinter as tk
from pynput import keyboard
from popup_window import ClipboardProgressPopup
from clipboard_processor import process_clipboard

correction_enabled = True
current_keys = set()

def toggle_correction(popup):
    global correction_enabled
    correction_enabled = not correction_enabled
    status = "ENABLED" if correction_enabled else "DISABLED"
    print(f"\n🚀 Clipboard AI Correction is now {status}.\n")
    popup.update_message(f"🚀 AI Clipboard is {status}")

def on_copy_hotkey(popup):
    global correction_enabled
    if correction_enabled:
        threading.Thread(target=process_clipboard, args=(popup,), daemon=True).start()

def on_press(key, popup):
    try:
        if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            current_keys.add("ctrl")
        elif hasattr(key, 'char') and key.char:
            current_keys.add(key.char.lower())

        # Ctrl + C to trigger clipboard processing
        if "ctrl" in current_keys and "c" in current_keys:
            on_copy_hotkey(popup)
            current_keys.clear()

        # Ctrl + Shift + E to toggle
        if "ctrl" in current_keys and "e" in current_keys:
            toggle_correction(popup)
            current_keys.clear()
    except Exception as e:
        print(f"[Error] {e}")

def on_release(key):
    if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        current_keys.discard("ctrl")
    elif key == keyboard.Key.shift:
        current_keys.discard("shift")
    elif hasattr(key, 'char') and key.char:
        current_keys.discard(key.char.lower())

def start_keyboard_listener(popup):
    print("🚀 Clipboard AI Corrector is running (Press Ctrl+Shift+E to enable/disable)\n")
    with keyboard.Listener(
        on_press=lambda key: on_press(key, popup),
        on_release=on_release
    ) as listener:
        listener.join()

def main():
    root = tk.Tk()
    popup = ClipboardProgressPopup(root)
    threading.Thread(target=start_keyboard_listener, args=(popup,), daemon=True).start()
    root.mainloop()

if __name__ == "__main__":
    main()
