import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk


def run_animation(self, parent):
    self.fig, self.ax = plt.subplots()
    self.canvas = FigureCanvasTkAgg(self.fig, master=parent)
    self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

    def animate(i):
        # reading from csv file
        data = pd.read_csv("./data/data.csv")
        x = data["x_value"]
        y1 = data["total_1"]
        y2 = data["total_2"]

        plt.cla()
        plt.plot(x, y1, label="Channel 1")
        plt.plot(x, y2, label="Channel 2")
        plt.legend(loc="upper left")

        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("Voltage (V)")
        self.ax.grid(True)

    self.animation = FuncAnimation(
        plt.gcf(), animate, interval=1000, cache_frame_data=False
    )

    plt.tight_layout()
