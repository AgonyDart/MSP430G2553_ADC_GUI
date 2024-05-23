import threading
import shutil
import os
import serial
from datetime import datetime
import tkinter as tk
import modules.live_data as live_data
import modules.msp430 as msp430

# import modules.data_gen as data_gen

ser = serial.Serial("COM3")
ser.baudrate = 9600
ser.timeout = 1
flag = threading.Event()


def init_root():
    def _quit():
        flag.set()
        root.quit()
        root.destroy()

    root = tk.Tk()
    root.protocol("WM_DELETE_WINDOW", _quit)

    width_screen = root.winfo_screenwidth()
    width_window = 1280
    height_screen = root.winfo_screenheight()
    height_window = 832

    root.title("MSP430G2553 ADC Data Grapher")
    root.geometry(
        f"{width_window}x{height_window}+{int((width_screen - width_window) / 2)}+{int((height_screen - height_window) / 2)}"
    )
    root.resizable(False, False)
    MainApplication(root)

    mps430_thread = threading.Thread(
        target=msp430.init_serial_com,
        args=(
            ser,
            flag,
        ),
    )
    mps430_thread.start()
    # data_gen_thread = threading.Thread(target=data_gen.generate_data, args=(flag,))
    # data_gen_thread.start()

    root.mainloop()


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.parent = parent
        self.parent.configure(bg="#FFFFFF")
        self.parent.iconbitmap("./icons/msp430.ico")

        # <Mathplotlib Logic>
        live_data.run_animation(self, self.parent)

        # <Buttons Logic>
        def change_channel():
            msp430.button(ser)

        def save():
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            new_filename = f"./data/data_{timestamp}.csv"
            print(f"File saved as: {new_filename}")
            shutil.copy2("./data/data.csv", new_filename)
            print(f"File copied to: {new_filename}")

        def clear():
            live_data.clear_data(self)

        def create_button(
            parent,
            text,
            command,
            font=("Inter", 24),
            bg="#5980BD",
            fg="white",
            bd=5,
            justify="center",
            relief="flat",
        ):
            button = tk.Button(
                parent,
                text=text,
                command=command,
                font=font,
                bg=bg,
                fg=fg,
                bd=bd,
                justify=justify,
                relief=relief,
            )
            button.pack(side="left", padx=10, pady=10)
            return button

        # <create the rest of your GUI here>

        btn_change_channel = create_button(
            self.parent,
            "Change Channel",
            change_channel,
        )
        btn_save = create_button(self.parent, "Save", save)
        btn_clear = create_button(self.parent, "Clear", clear, bg="#BD598F")


if __name__ == "__main__":
    init_root()
