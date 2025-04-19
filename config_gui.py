import tkinter as tk
from config import get_config, save_config

class ConfigWindow(tk.Frame):
    def __init__(self, parent, root=None, **kwargs):
        super().__init__(parent, bg="#edf2f7", **kwargs)
        self.root = root
        self.config_data = get_config()
        self.fields = {}

        self.header = tk.Frame(self, bg="#edf2f7")
        self.header.pack(fill="x", pady=(5, 0))

        tk.Label(self.header, text="⚙️ Settings", font=("Segoe UI", 10, "bold"), bg="#edf2f7", fg="#2b6cb0").pack(side="left", padx=10)
        self.toggle_btn = tk.Button(self.header, text="⬆️", font=("Segoe UI", 8), command=self.toggle_visibility, bg="#edf2f7", bd=0)
        self.toggle_btn.pack(side="right", padx=10)

        self.form_frame = tk.Frame(self, bg="#edf2f7")
        self.form_frame.pack(padx=20, fill="x")

        self.add_dropdown("Select AI Model", ["ollama", "chatgpt", "gemini"], "model", "ollama", self.update_fields)

        self.dynamic_fields_frame = tk.Frame(self, bg="#edf2f7")
        self.dynamic_fields_frame.pack(padx=20, fill="x")
        self.update_fields()

        tk.Button(self, text="💾 Save Settings", command=self.save_config,
                  bg="#3182ce", fg="white", font=("Segoe UI", 9), relief="flat").pack(pady=10)

    def add_entry(self, frame, label, key, default="", hide=False):
        tk.Label(frame, text=label + ":", bg="#edf2f7", anchor="w", font=("Segoe UI", 9)).pack(fill="x", pady=(10, 2))
        entry = tk.Entry(frame, show="*" if hide else "")
        entry.insert(0, self.config_data.get(key, default))
        entry.pack(fill="x")
        self.fields[key] = entry

    def add_dropdown(self, label, options, key, default="", command=None):
        tk.Label(self.form_frame, text=label + ":", bg="#edf2f7", anchor="w", font=("Segoe UI", 9)).pack(fill="x", pady=(10, 2))
        var = tk.StringVar(value=self.config_data.get(key, default))
        dropdown = tk.OptionMenu(self.form_frame, var, *options)
        dropdown.config(font=("Segoe UI", 9), bg="white")
        dropdown.pack(fill="x")
        if command:
            var.trace("w", lambda *args: command())
        self.fields[key] = var

    def update_fields(self):
        # Clear dynamic frame and previous dynamic fields
        for widget in self.dynamic_fields_frame.winfo_children():
            widget.destroy()

        # Clean up dynamic keys from fields dict
        for key in list(self.fields.keys()):
            if key not in ["model"]:
                del self.fields[key]

        model = self.fields["model"].get()
        if model == "ollama":
            self.add_entry(self.dynamic_fields_frame, "Ollama Model", "ollama_model", "llama3.2")
        elif model == "chatgpt":
            self.add_entry(self.dynamic_fields_frame, "ChatGPT API Key", "chatgpt_key", "", hide=True)
            self.add_entry(self.dynamic_fields_frame, "ChatGPT Model", "chatgpt_model", "gpt-3.5-turbo")
        elif model == "gemini":
            self.add_entry(self.dynamic_fields_frame, "Gemini API Key", "gemini_key", "", hide=True)
            self.add_entry(self.dynamic_fields_frame, "Gemini Model", "gemini_model", "gemini-pro")

    def save_config(self):
        new_config = {}
        for key, widget in self.fields.items():
            new_config[key] = widget.get() if not isinstance(widget, tk.StringVar) else widget.get()
        save_config(new_config)

    def toggle_visibility(self):
        if self.winfo_ismapped():
            self.pack_forget()
            self.toggle_btn.config(text="⬇️")
            if self.root:
                self.root.geometry("400x150+1000+600")  # shrink when hidden
        else:
            self.pack(fill="both", expand=True)
            self.toggle_btn.config(text="⬆️")
            if self.root:
                self.root.geometry("400x360+1000+600")  # expand when shown
