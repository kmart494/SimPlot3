import os
import tkinter as tk
from tkinter import filedialog
from modules import global_vars as gv


class NewScenarioWindow(tk.Toplevel):
    """New Scenario window."""

    def on_scenario_folder_button(self):
        """Scenario folder button action."""
        folder = filedialog.askdirectory(
            initialdir=gv.app_scenario_folder)
        if folder:
            self.scenario_folder.set(os.path.abspath(folder))
        else:
            self.scenario_folder.set('No folder selected.')
        self.focus()

    def on_map_file_btn(self):
        """Map File button action."""
        fn = filedialog.askopenfilename(
            initialdir=gv.app_map_folder,
            filetypes=(('SimPlot Map Files', '*.map'),
                       ('Text Files', '*.txt'),
                       ('JSON Files', '*.json')))
        if fn:
            self.map_filename.set(os.path.abspath(fn))
        else:
            self.map_filename.set('No file selected.')
        self.focus()

    def on_cancel_btn(self):
        """Cancel button action."""
        self.destroy()

    def on_ok_btn(self):
        """OK button action."""
        gv.scenario_name = self.scenario_name.get()
        gv.set_scenario_folder(self.scenario_folder.get())
        gv.set_scenario_filename(self.scenario_filename.get())
        gv.map_filename = self.map_filename.get()
        if self.app:
            self.app.title(f'SimPlot3 -- {gv.scenario_name}')
            self.app.focus()
        self.destroy()

    def __init__(self, window=None):
        """New Scenario window constructor."""
        super().__init__()
        self.title('New Scenario')
        # self.geometry('400x500')
        # self.minsize(width=400, height=500)
        # self.maxsize(width=400, height=500)
        if window:
            self.app = window
        else:
            self.app = None

        # Scenario name and file frame.

        self.name_frame = tk.LabelFrame(self, text='')
        tk.Label(self.name_frame, text='Scenario Name'
                 ).grid(row=0, column=0, padx=5, pady=5, sticky=tk.W + tk.N)
        self.scenario_name = tk.StringVar()
        tk.Entry(self.name_frame, width=30, textvariable=self.scenario_name
                 ).grid(row=0, column=1, padx=(0, 5), pady=5,
                        sticky=tk.W + tk.N)
        tk.Label(self.name_frame, text='Scenario Filename'
                 ).grid(row=1, column=0, padx=5, pady=(0, 5),
                        sticky=tk.W + tk.N)
        self.scenario_filename = tk.StringVar()
        tk.Entry(self.name_frame, width=30, textvariable=self.scenario_filename
                 ).grid(row=1, column=1, padx=(0, 5), pady=(0, 5),
                        sticky=tk.W + tk.N)
        tk.Button(self.name_frame, text='Choose Scenario Folder',
                  command=self.on_scenario_folder_button
                  ).grid(row=2, column=0, padx=5, pady=(0, 5),
                         sticky=tk.W + tk.N)
        self.scenario_folder = tk.StringVar(value='No folder selected.')
        tk.Label(self.name_frame, textvariable=self.scenario_folder
                 ).grid(row=2, column=1, padx=(0, 5), pady=(0, 5),
                        sticky=tk.W + tk.N)
        self.name_frame.grid(row=0, column=0, sticky=tk.N + tk.W, padx=5,
                             pady=5)

        # Date frame.

        self.date_frame = tk.LabelFrame(self, text='Date')
        tk.Label(self.date_frame, text='Day'
                 ).grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(self.date_frame, width=2
                 ).grid(row=0, column=1, padx=(0, 5), pady=5)
        tk.Label(self.date_frame, text='Month'
                 ).grid(row=0, column=2, padx=5, pady=5)
        tk.Entry(self.date_frame, width=2
                 ).grid(row=0, column=3, padx=(0, 5), pady=5)
        tk.Label(self.date_frame, text='Year'
                 ).grid(row=0, column=4, padx=5, pady=5)
        tk.Entry(self.date_frame, width=4
                 ).grid(row=0, column=5, padx=(0, 5), pady=5)
        self.date_frame.grid(row=1, column=0, sticky=tk.N + tk.W, padx=5,
                             pady=(0, 5))

        # Scenario time frame.

        self.time_frame = tk.LabelFrame(self, text='Time')
        tk.Label(self.time_frame, text='Time (HHMM)'
                 ).grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(self.time_frame, width=4
                 ).grid(row=0, column=1, padx=(0, 5), pady=5)
        self.time_frame.grid(row=2, column=0, sticky=tk.N + tk.W, padx=5,
                             pady=(0, 5))

        # Wind speed, direction, and sea state frame.

        self.wind_frame = tk.LabelFrame(self, text='Wind and Sea State')
        tk.Label(self.wind_frame, text='Wind Direction (degrees)'
                 ).grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(self.wind_frame, width=3
                 ).grid(row=0, column=1, padx=(0, 5), pady=5)
        tk.Label(self.wind_frame, text='Wind Speed (knots)'
                 ).grid(row=0, column=2, padx=5, pady=5)
        tk.Entry(self.wind_frame, width=3
                 ).grid(row=0, column=3, padx=(0, 5), pady=5)
        tk.Label(self.wind_frame, text='Sea State'
                 ).grid(row=1, column=0, padx=5, pady=(0, 5),
                        sticky=tk.W + tk.N)
        tk.Entry(self.wind_frame, width=2
                 ).grid(row=1, padx=(0, 5), pady=(0, 5))
        self.wind_frame.grid(row=3, column=0, sticky=tk.N + tk.W, padx=5,
                             pady=(0, 5))

        # Optional map frame.

        self.map_frame = tk.LabelFrame(self, text='Optional Map')
        tk.Button(self.map_frame, text='Choose Map File',
                  command=self.on_map_file_btn
                  ).grid(row=0, column=0, sticky=tk.N + tk.W, padx=5, pady=5)
        self.map_filename = tk.StringVar(self, value='No file selected.')
        tk.Label(self.map_frame, textvariable=self.map_filename
                 ).grid(row=0, column=1, sticky=tk.N + tk.W, padx=(0, 5),
                        pady=5)
        self.map_frame.grid(row=4, column=0, sticky=tk.N + tk.W, padx=5,
                            pady=(0, 5))

        # Cancel and OK button frame.

        self.btn_frame = tk.Frame(self)
        tk.Button(self.btn_frame, text='Cancel', width=10,
                  command=self.on_cancel_btn
                  ).grid(row=0, column=0, padx=5)
        tk.Button(self.btn_frame, text='OK', width=10, command=self.on_ok_btn
                  ).grid(row=0, column=1)
        self.btn_frame.grid(row=5, sticky=tk.E, padx=5, pady=5)

        #

        self.focus()


# Testing.
if __name__ == '__main__':
    temp = NewScenarioWindow()
    temp.mainloop()
