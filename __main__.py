import tkinter


class App(tkinter.Tk):
    """
    Main application window.
    """
    def __init__(self):
        """
        Application window constructor.
        """
        super().__init__()
        self.title("SimPlot3")
        self.geometry("1280x720")
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.rowconfigure(0, weight=1)

        main_menu = tkinter.Menu(self)
        self.config(menu=main_menu)

        file_menu = tkinter.Menu(main_menu, tearoff=0)
        main_menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New Scenario")
        file_menu.add_command(label="Load Scenario")
        file_menu.add_command(label="Save Scenario")

        customize_menu = tkinter.Menu(main_menu, tearoff=0)
        main_menu.add_cascade(label="Customize", menu=customize_menu)
        customize_menu.add_command(label="Controls")
        customize_menu.add_command(label="Color Options")
        customize_menu.add_command(label="Display Options")

        map_canvas = tkinter.Canvas(self, width=1075, height=720, background="#464646")
        map_canvas.grid(row=0, column=0, sticky=tkinter.E + tkinter.W + tkinter.N + tkinter.S)

        info_canvas = tkinter.Canvas(self, width=200, height=720, background="blue")
        info_canvas.grid(row=0, column=1, sticky=tkinter.E + tkinter.N + tkinter.S)


app = App()
app.mainloop()
