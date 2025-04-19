import tkinter as tk
import itertools
from config_gui import ConfigWindow

class ClipboardProgressPopup:
    def __init__(self, root):
        self.root = root
        self.root.title("TypoGenie")
        self.root.geometry("400x150+1000+600")
        self.root.configure(bg="#e7ecff")
        self.root.attributes("-topmost", True)
        self.root.resizable(False, False)

        # Popup Frame
        self.popup_frame = tk.Frame(self.root, bg="#ffffff", bd=2, relief="ridge")
        self.popup_frame.pack(padx=10, pady=(10, 0), fill="x")

        # Settings Frame Placeholder
        self.config_frame = None

        # Menu Bar
        self.menu_bar = tk.Frame(self.popup_frame, bg="#ffffff")
        self.menu_bar.pack(fill="x", anchor="n")

        tk.Button(self.menu_bar, text="⚙️", command=self.toggle_settings, bd=0, bg="#ffffff", fg="#666",
                  font=("Segoe UI", 10)).pack(side="right", padx=5, pady=4)

        # Main Message
        self.icon_message = tk.Frame(self.popup_frame, bg="#ffffff")
        self.icon_message.pack(pady=1)
        tk.Label(self.icon_message, text="🤖", font=("Segoe UI Emoji", 22), bg="#ffffff").pack(side="left", padx=(0, 10))
        self.label = tk.Label(self.icon_message, text="Press Ctrl+C to copy", font=("Segoe UI", 11, "bold"),
                              fg="#333", bg="#ffffff", wraplength=300, justify="left")
        self.label.pack(side="left")

        # Loading Indicator
        self.loading_label = tk.Label(self.popup_frame, text="", font=("Segoe UI", 10), bg="#ffffff", fg="#6366f1")
        self.loading_label.pack(pady=(5, 0))

        self.animate_dots = itertools.cycle(["", ".", "..", "..."])
        self.animate_loading()

        # Settings Component
        self.settings_window = None

        self.root.after(100, self.root.lift)

    def minimize(self):
        self.root.iconify()

    def animate_loading(self):
        dots = next(self.animate_dots)
        self.loading_label.config(text="TypoGenie is running" + dots)
        self.root.after(500, self.animate_loading)

    def update_message(self, new_message):
        if "⚠️" in new_message or "missing" in new_message.lower():
            self.label.config(text=new_message, fg="#d32f2f")
            self.loading_label.config(text="")
        else:
            self.label.config(text=new_message, fg="#333")
        self.root.update_idletasks()

    def toggle_settings(self):
        if self.settings_window and self.settings_window.winfo_ismapped():
            self.settings_window.pack_forget()
            self.config_frame.pack_forget()
            self.root.geometry("400x150+1000+600")  # back to original Y=600
        else:
            if not self.config_frame:
                self.config_frame = tk.Frame(self.root, bg="#edf2f7", bd=2, relief="ridge")
                self.settings_window = ConfigWindow(self.config_frame, root=self.root)
            self.config_frame.pack(padx=10, pady=(5, 10), fill="x")
            self.settings_window.pack(fill="both", expand=True)
            self.root.geometry("400x400+1000+450")  # move up to Y=450 when expanded
