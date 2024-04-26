import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

class Notepad:
    def __init__(self, master):
        self.master = master
        self.master.title("Test Notepad")
        self.file_path = None

       