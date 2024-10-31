import datetime
import os

# Basic scenario information.
app_folder = ''
app_scenario_folder = ''
app_map_folder = ''
scenario_name = 'New Scenario'
scenario_filename = ''
scenario_folder = ''
map_filename = ''
scenario_date = datetime.date(2024,1,1)
scenario_time = datetime.time(9, 00, 00)
wind_direction = 0
wind_speed = 0
sea_state = 0

#
units = []


def set_application_folders(root_folder):
    global app_folder
    global app_scenario_folder
    global app_map_folder
    app_folder = root_folder
    app_scenario_folder = os.path.join(app_folder, 'data', 'scenarios')
    app_map_folder = os.path.join(app_folder, 'data', 'maps')
    print(f'\nApplication Folder = {app_folder}')
    print(f'Application Scenario Folder = {app_scenario_folder}')
    print(f'Application Map Folder = {app_map_folder}')


def set_scenario_folder(folder):
    global scenario_folder
    scenario_folder = folder
    print(f'\nScenario Folder = {scenario_folder}')


def set_scenario_filename(file):
    global scenario_filename
    global scenario_folder
    scenario_filename = os.path.join(scenario_folder, file)
    print(f'\nScenario File = {scenario_filename}')

