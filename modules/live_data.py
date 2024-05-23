import msvcrt
import pandas as pd
import msp430 as msp430
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
        y1 = data["channel_1"]
        y2 = data["channel_2"]
        y3 = data["channel_3"]

        # Conversion to volt values

        plt.cla()
        plt.plot(x, y1, label="Channel 1")
        plt.plot(x, y2, label="Channel 2")
        plt.plot(x, y3, label="Channel 3")
        plt.legend(loc="upper left")

        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("Voltage (V)")
        self.ax.grid(True)

    self.animation = FuncAnimation(
        plt.gcf(), animate, interval=1000, cache_frame_data=False
    )

    plt.tight_layout()
    # plt.show()


def clear_data(self):
    # Clear the axis object
    self.ax.clear()
    # Redraw the plot with empty data
    self.fig.canvas.draw_idle()
    # Lock and clear the csv file
    with open("./data/data.csv", "w") as file:
        # Acquire a lock on the file
        msvcrt.locking(file.fileno(), msvcrt.LK_LOCK, 0)

        # Truncate the file to clear its contents
        file.truncate(0)

        # Release the lock
        msvcrt.locking(file.fileno(), msvcrt.LK_UNLCK, 0)
