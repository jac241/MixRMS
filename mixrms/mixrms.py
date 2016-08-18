import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import soundfile as sf

import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure


class MixRMSApp:
    def __init__(self):
        self.root = tk.Tk()

    def run(self):
        self.root.title('MixRMS')
        self.root.deiconify()
        self.build_file_menu()
        self.root.mainloop()

    def build_file_menu(self):
        menu_bar = MenuBar(self.root, MenuBarController())
        menu_bar.bind_to_window()


class MenuBar:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.menu_bar = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label='Open', command=self.controller.load_file)
        self.menu_bar.add_cascade(label='File', menu=self.file_menu)

    def bind_to_window(self):
        tk.Tk.config(self.root, menu=self.menu_bar)


class MenuBarController:
    def load_file(self):
        filename = filedialog.askopenfilename(filetypes=(("Audio files", "*.wav"), ("all files", "*.*")))
        print(sf.SoundFile(filename))


def main():
    app = MixRMSApp()
    app.run()
