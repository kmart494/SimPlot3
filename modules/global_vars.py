import datetime
import os

# Basic scenario information.
app_folder = ''
scenario_name = 'New Scenario'
scenario_filename = ''
scenario_folder = ''
map_filename = ''
map_folder = ''
scenario_date = datetime.date(2024,1,1)
scenario_time = datetime.time(9, 00, 00)

units = []


def set_application_folder(folder):
    global app_folder
    app_folder = folder
    print(f'Application Folder = {app_folder}')


def set_scenario_folder(folder):
    global scenario_folder
    global app_folder
    scenario_folder = os.path.join(app_folder, "Scenarios", folder)
    print(f'Scenario Folder = {scenario_folder}')


def set_map_folder():
    global map_folder
    global app_folder
    map_folder = os.path.join(app_folder, "Maps")
    print(f'Map Folder = {map_folder}')

