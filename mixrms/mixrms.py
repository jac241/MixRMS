import tkinter as tk
from .menubar import MenuBarController, MenuBar

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


def main():
    app = MixRMSApp()
    app.run()
