import tkinter as tk
from tkinter import filedialog
from modules import global_vars as gv


class NewScenarioWindow(tk.Toplevel):
    """New Scenario window."""

    def on_map_file_btn(self):
        """Map File button action."""
        fn = filedialog.askopenfilename(initialdir=gv.app_folder,
                                        filetypes=(('SimPlot Map Files',
                                                    '*.map'),
                                                   ('Text Files', '*.txt'),
                                                   ('JSON Files', '*.json')))
        if fn:
            self.map_filename.set(fn)
        else:
            self.map_filename.set('No file selected.')
        self.focus()

    def on_cancel_btn(self):
        """Cancel button action."""
        self.destroy()

    def on_ok_btn(self):
        """OK button action."""
        self.app.title(f'SimPlot3 -- {gv.scenario_name}')
        gv.scenario_name = self.scenario_name_entry.get()
        gv.scenario_filename = self.scenario_filename.get()
        gv.set_scenario_folder(self.scenario_folder.get())
        gv.map_filename = self.map_filename.get()
        self.destroy()

    def __init__(self, window):
        """New Scenario window constructor."""
        super().__init__()
        self.title('New Scenario')
        # self.geometry('400x500')
        # self.minsize(width=400, height=500)
        # self.maxsize(width=400, height=500)
        self.app = window

        # Scenario name and file frame.
        self.name_frame = tk.LabelFrame(self, text='')
        self.scenario_name_label = tk.Label(self.name_frame,
                                            text='Scenario Name')
        self.scenario_name_label.grid(row=0, column=0, padx=5, pady=5,
                                      sticky=tk.W + tk.N)
        self.scenario_name_entry = tk.Entry(self.name_frame, width=30)
        self.scenario_name_entry.grid(row=0, column=1, padx=(0, 5), pady=5,
                                      sticky=tk.W + tk.N)
        self.scenario_filename_label = tk.Label(self.name_frame,
                                                text='Scenario Filename')
        self.scenario_filename_label.grid(row=1, column=0, padx=5, pady=(0, 5),
                                          sticky=tk.W + tk.N)
        self.scenario_filename = tk.StringVar()
        self.scenario_filename_entry = tk.Entry(self.name_frame, width=30,
                                                textvariable=
                                                self.scenario_filename)
        self.scenario_filename_entry.grid(row=1, column=1, padx=(0, 5),
                                          pady=(0, 5), sticky=tk.W + tk.N)
        self.scenario_folder_label = tk.Label(self.name_frame,
                                              text='Scenario Folder')
        self.scenario_folder_label.grid(row=2, column=0, padx=5, pady=(0, 5),
                                        sticky=tk.W + tk.N)
        self.scenario_folder = tk.StringVar()
        self.scenario_folder_entry = tk.Entry(self.name_frame, width=30,
                                              textvariable=self.scenario_folder)
        self.scenario_folder_entry.grid(row=2, column=1, padx=(0, 5),
                                        pady=(0, 5), sticky=tk.W + tk.N)
        self.name_frame.grid(row=0, column=0, sticky=tk.N + tk.W, padx=5,
                             pady=5)

        # Date frame.
        self.date_frame = tk.LabelFrame(self, text='Date')
        self.day_label = tk.Label(self.date_frame, text='Day')
        self.day_label.grid(row=0, column=0, padx=5, pady=5)
        self.day_entry = tk.Entry(self.date_frame, width=2)
        self.day_entry.grid(row=0, column=1, padx=(0, 5), pady=5)
        self.month_label = tk.Label(self.date_frame, text='Month')
        self.month_label.grid(row=0, column=2, padx=5, pady=5)
        self.month_entry = tk.Entry(self.date_frame, width=2)
        self.month_entry.grid(row=0, column=3, padx=(0, 5), pady=5)
        self.year_label = tk.Label(self.date_frame, text='Year')
        self.year_label.grid(row=0, column=4, padx=5, pady=5)
        self.year_entry = tk.Entry(self.date_frame, width=4)
        self.year_entry.grid(row=0, column=5, padx=(0, 5), pady=5)
        self.date_frame.grid(row=1, column=0, sticky=tk.N + tk.W, padx=5,
                             pady=(0, 5))

        # Scenario time frame.
        self.time_frame = tk.LabelFrame(self, text='Time')
        self.time_label = tk.Label(self.time_frame, text='Time (HHMM)')
        self.time_label.grid(row=0, column=0, padx=5, pady=5)
        self.time_entry = tk.Entry(self.time_frame, width=4)
        self.time_entry.grid(row=0, column=1, padx=(0, 5), pady=5)

        self.time_frame.grid(row=2, column=0, sticky=tk.N + tk.W, padx=5,
                             pady=(0, 5))

        # Wind speed, direction, and sea state frame.
        self.wind_frame = tk.LabelFrame(self, text='Wind and Sea State')
        self.wind_dir_label = tk.Label(self.wind_frame, text='Wind Direction '
                                                             '(degrees)')
        self.wind_dir_label.grid(row=0, column=0, padx=5, pady=5)
        self.wind_dir_entry = tk.Entry(self.wind_frame, width=3)
        self.wind_dir_entry.grid(row=0, column=1, padx=(0, 5), pady=5)
        self.wind_spd_label = tk.Label(self.wind_frame, text='Wind Speed ('
                                                             'knots)')
        self.wind_spd_label.grid(row=0, column=2, padx=5, pady=5)
        self.wind_speed_entry = tk.Entry(self.wind_frame, width=3)
        self.wind_speed_entry.grid(row=0, column=3, padx=(0, 5), pady=5)

        self.sea_state_label = tk.Label(self.wind_frame, text='Sea State')
        self.sea_state_label.grid(row=1, column=0, padx=5, pady=(0, 5),
                                  sticky=tk.W + tk.N)
        self.sea_state_entry = tk.Entry(self.wind_frame, width=2)
        self.sea_state_entry.grid(row=1, padx=(0, 5), pady=(0, 5))
        self.wind_frame.grid(row=3, column=0, sticky=tk.N + tk.W, padx=5,
                             pady=(0, 5))

        # Optional map frame.
        self.map_frame = tk.LabelFrame(self, text='Optional Map')
        self.map_file_btn = tk.Button(self.map_frame, text='Choose Map File',
                                      command=self.on_map_file_btn)
        self.map_file_btn.grid(row=0, column=0, sticky=tk.N + tk.W, padx=5,
                               pady=5)
        self.map_filename = tk.StringVar(self, value='No file selected.')
        self.file_name_label = tk.Label(self.map_frame,
                                        textvariable=self.map_filename)
        self.file_name_label.grid(row=0, column=1, sticky=tk.N + tk.W,
                                  padx=(0, 5), pady=5)
        self.map_frame.grid(row=4, column=0, sticky=tk.N + tk.W, padx=5,
                            pady=(0, 5))

        # Cancel and OK button frame.
        self.btn_frame = tk.Frame(self)
        self.cancel_btn = tk.Button(self.btn_frame, text='Cancel', width=10,
                                    command=self.on_cancel_btn)
        self.cancel_btn.grid(row=0, column=0, padx=5)
        self.ok_btn = tk.Button(self.btn_frame, text='OK', width=10,
                                command=self.on_ok_btn)
        self.ok_btn.grid(row=0, column=1)
        self.btn_frame.grid(row=5, sticky=tk.E, padx=5, pady=5)
