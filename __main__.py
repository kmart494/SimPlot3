import tkinter
from modules import map_colors as mc
from modules import map_draw as md


class App(tkinter.Tk):
    """
    Main application window.
    """

    def load_scenario(self):
        """
        Load scenario menu action.
        """
        print("Load Scenario Menu Item")

    def __init__(self):
        """
        Application window constructor.
        """
        super().__init__()
        self.title("SimPlot3")
        self.geometry("1280x720")
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=0)
        self.rowconfigure(3, weight=1)

        main_menu = tkinter.Menu(self)
        self.config(menu=main_menu)

        file_menu = tkinter.Menu(main_menu, tearoff=0)
        main_menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New Scenario")
        file_menu.add_command(label="Load Scenario", command=self.load_scenario)
        file_menu.add_command(label="Save Scenario")

        customize_menu = tkinter.Menu(main_menu, tearoff=0)
        main_menu.add_cascade(label="Customize", menu=customize_menu)
        customize_menu.add_command(label="Controls")
        customize_menu.add_command(label="Color Options")
        customize_menu.add_command(label="Display Options")

        # Create map canvas.
        self.map_canvas = tkinter.Canvas(self, background=mc.background,
                                         width=1070, height=720)
        self.map_canvas.grid(row=0, column=0, rowspan=4,
                             sticky=tkinter.E + tkinter.W + tkinter.N +
                                    tkinter.S)

        # Create game information frame.
        self.scenario_info_frame = tkinter.LabelFrame(self, width=200,
                                                      height=200,
                                                      text="Scenario "
                                                           "Information")
        self.scenario_info_frame.grid(row=0, column=1,
                                      sticky=tkinter.E + tkinter.N)

        # Create selected unit frame.
        self.selected_unit_frame = tkinter.LabelFrame(self, width=200,
                                                      height=300,
                                                      text="Selected Unit "
                                                           "Information")
        self.selected_unit_frame.grid(row=1, column=1,
                                      sticky=tkinter.E + tkinter.S + tkinter.N)

        # Create move button frame.
        self.move_frame = tkinter.LabelFrame(self, width=200, height=200,
                                             text="Movement")
        self.move_frame.grid(row=2, column=1,
                             sticky=tkinter.E + tkinter.S)

    def update_map(self):
        md.update_map(self.map_canvas)


app = App()
# app.update_map()
app.mainloop()
