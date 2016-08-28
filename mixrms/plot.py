from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from collections import namedtuple
import soundfile as sf
import numpy as np
import tkinter as tk
import matplotlib
matplotlib.use('TkAgg')


RMSAnalysis = namedtuple('RMSAnalysis', ['rms', 'time'])


class AnalysisController:
    def __init__(self, root_view):
        self.root_view = root_view
        self.current_plot = None

    def plot_analysis(self, filepath):
        if self.current_plot is not None:
            self.current_plot.destroy()

        rms_analysis = self.generate_analysis(filepath)
        rms_plot = RMSPlot(self.root_view, rms_analysis)
        rms_plot.grid(row=0, column=0, sticky='nsew')
        rms_plot.tkraise()

        self.current_plot = rms_plot


    def generate_analysis(self, filepath):
        with sf.SoundFile(filepath) as f:
            blocksize = 44100 * 60
            overlap = blocksize // 2
            rms = [20 * np.log10(np.sqrt(np.mean(block**2))) for block in
                   f.blocks(blocksize=blocksize, overlap=overlap)]
            time = [(number * overlap) / f.samplerate for number in range(1, len(rms) + 1)]

            return RMSAnalysis(rms=rms, time=time)


class RMSPlot(tk.Frame):
    def __init__(self, parent, rms_analysis):
        tk.Frame.__init__(self, parent)
        figure = Figure()
        subplot = figure.add_subplot(111)
        subplot.plot(rms_analysis.time, rms_analysis.rms)
        subplot.set_ylim(-96, 0)

        canvas = FigureCanvasTkAgg(figure, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
