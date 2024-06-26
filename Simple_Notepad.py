import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

class Notepad:
    def __init__(self, master):
        self.master = master
        self.master.title("Test Notepad")
        self.file_path = None
        
        self.text_area = scrolledtext.ScrolledText(self.master, undo=True)
        self.text_area.pack(fill=tk.BOTH, expand=1)

        self.menu_bar = tk.Menu(self.master)
        self.master.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", accelerator="Ctrl+N", command=self.new_file)
        self.file_menu.add_command(label="Open...", accelerator="Ctrl+O", command=self.open_file)
        self.file_menu.add_command(label="Save", accelerator="Ctrl+S", command=self.save_file)
        self.file_menu.add_command(label="Save As...", accelerator="Ctrl+Shift+S", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_editor)
        
        self.master.bind("<Control-n>", self.new_file)
        self.master.bind("<Control-o>", self.open_file)
        self.master.bind("<Control-s>", self.save_file)
        self.master.bind("<Control-Shift-S>", self.save_as_file)
        

def new_file(self, event=None):
    self.text_area.delete(1.0, tk.END)
    with open(path, "r") as file:
                self.text_area.insert(tk.END, file.read())
            self.master.title(f"{self.file_path} - Simple Notepad")

    def save_file(self, event=None):
        if self.file_path:
            content = self.text_area.get(1.0, tk.END)
            with open(self.file_path, "w") as file:
                file.write(content)
            self.master.title(f"{self.file_path} - Simple Notepad")
        else:
            self.save_as_file()


