import tkinter as tk
from tkinter import filedialog
from .plot import AnalysisController
import soundfile as sf
import os


class MenuBar:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.menu_bar = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label='Open',
                                   command=self.controller.load_file)
        self.menu_bar.add_cascade(label='File', menu=self.file_menu)

    def bind_to_window(self):
        tk.Tk.config(self.root, menu=self.menu_bar)


class FileValidator:
    def is_valid_wav_file(self, filepath):
        file_exists = os.path.isfile(filepath)
        file_is_wav = os.path.splitext(filepath)[1] == '.wav'
        return file_exists and file_is_wav


class MenuBarController:
    def __init__(self, file_validator=FileValidator(),
                 analysis_controller=AnalysisController()):
        self.file_validator = file_validator
        self.analysis_controller = analysis_controller

    def load_file(self):
        filepath = filedialog.askopenfilename(
            filetypes=(("Audio files", "*.wav"), ("all files", "*.*")))

        if self.file_validator.is_valid_wav_file(filepath):
            self.analysis_controller.plot_analysis(filepath=filepath)
