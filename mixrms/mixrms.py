import tkinter as tk
from .menubar import MenuBarController, MenuBar
from .plot import AnalysisController

import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure


class MixRMSApp:
    def __init__(self):
        self.root = tk.Tk()
        self.container = tk.Frame(self.root)
        self.container.pack(side='top', fill='both', expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

    def run(self):
        self.root.title('MixRMS')
        self.root.deiconify()
        self.build_file_menu()
        self.root.mainloop()

    def build_file_menu(self):
        menu_bar = MenuBar(
            self.root,
            MenuBarController(
                analysis_controller=AnalysisController(root_view=self.container)
            )
        )

        menu_bar.bind_to_window()


def main():
    app = MixRMSApp()
    app.run()
