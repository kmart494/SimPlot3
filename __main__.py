import os
import tkinter as tk
import images
from modules import map_colors as mc
from modules import map_draw as md
from modules import global_vars as gv
from modules import new_scenario_window


class App(tk.Tk):
    """Main application window."""

    def on_new_scenario(self):
        """New Scenario menu action."""
        new_scenario_win = new_scenario_window.NewScenarioWindow(self)

    def on_load_scenario(self):
        """Load Scenario menu action."""
        print('Load Scenario Menu Item')
        self.title(f'SimPlot3 -- {gv.scenario_name}')

    def __init__(self):
        """Application window constructor."""
        super().__init__()
        self.app_icon = tk.PhotoImage(file=images.APP_LOGO_32)
        self.iconphoto(True, self.app_icon)
        self.title('SimPlot3 -- No Scenario')
        self.geometry('1280x720')
        self.minsize(width=1280, height=720)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=0)
        self.rowconfigure(3, weight=1)
        gv.set_application_folders(os.getcwd())

        # Create application main menu.

        main_menu = tk.Menu(self)
        self.config(menu=main_menu)

        # Create File menus.

        file_menu = tk.Menu(main_menu, tearoff=0)
        main_menu.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label='New Scenario',
                              command=self.on_new_scenario)
        file_menu.add_command(label='Load Scenario',
                              command=self.on_load_scenario)
        file_menu.add_command(label='Save Scenario')

        # Create Customize menus.

        customize_menu = tk.Menu(main_menu, tearoff=0)
        main_menu.add_cascade(label='Customize', menu=customize_menu)
        customize_menu.add_command(label='Controls')
        customize_menu.add_command(label='Color Options')
        customize_menu.add_command(label='Display Options')

        # Create map canvas.

        self.map_canvas = tk.Canvas(self, background=mc.background,
                                    width=1070, height=720)
        self.map_canvas.grid(row=0, column=0, rowspan=4,
                             sticky=tk.E + tk.W + tk.N + tk.S)

        # Create game information frame.

        self.scenario_info_frame = tk.LabelFrame(self, width=200, height=200,
                                                 text='Scenario Information')
        self.scenario_info_frame.grid(row=0, column=1, sticky=tk.E + tk.N)

        # Create selected unit frame.

        self.selected_unit_frame = tk.LabelFrame(self, width=200, height=300,
                                                 text='Selected Unit '
                                                      'Information')
        self.selected_unit_frame.grid(row=1, column=1,
                                      sticky=tk.E + tk.S + tk.N)

        # Create move button frame.

        self.move_frame = tk.LabelFrame(self, width=200, height=200,
                                        text='Movement')
        self.move_frame.grid(row=2, column=1, sticky=tk.E + tk.S)

    def update_map(self):
        md.update_map(self.map_canvas)


app = App()
# app.update_map()
app.mainloop()
