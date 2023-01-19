import tkinter as tk
from tkinter import ttk
from mclpiezopy import MCLPiezo

ROOT_TITLE = "MCL Piezo Z-Controller"


class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.__initialize_piezo()

        self.title(ROOT_TITLE)

        # variables
        init_z = self.piezo.mcl_read(3)
        self.__current_z = tk.DoubleVar(value=init_z)
        self.__current_z_str = tk.StringVar()
        self.__update_z_str()

        # grid settings
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)

        self.__create_widgets()

    def __initialize_piezo(self) -> None:
        self.piezo = MCLPiezo()
        self.__max_z = self.piezo.get_calibration(3)

    def __create_widgets(self) -> None:
        self.z_slider = ttk.Scale(
            self, from_=0, to=self.__max_z, length=200,
            orient=tk.HORIZONTAL, variable=self.__current_z,
            command=self.__handle_z_slider)
        self.z_slider.grid(column=0, row=0)

        label = ttk.Label(self, textvariable=self.__current_z_str)
        label.grid(column=0, row=1)

    def __update_z_str(self) -> None:
        self.__current_z_str.set(f"{self.__current_z.get():.2f}")

    def __handle_z_slider(self, *args) -> None:
        self.piezo.goz(self.__current_z.get())
        self.piezo.mcl_read(3)  # dummy
        self.__current_z.set(self.piezo.mcl_read(3))
        self.__update_z_str()


if __name__ == '__main__':
    app = App()
    app.mainloop()
