from prettytable import PrettyTable
import os
import subprocess
from .botoptions import main, delete_server_options, test, MainCords, delete, AddAdmin, deleteadminlist

js_file_path = 'src/Brikaine.js'

def MultiToolCommands():
    command_table = PrettyTable()
    command_table.field_names = ["Command", "Overview"]
    command_table.add_row(["MainCords", "Set main coordinates"])
    command_table.add_row(["AddChestCoordinates", "Add chest coordinates to item counter"])
    command_table.add_row(["DelChestCordinates", "Delete chest coordinates"])
    command_table.add_row(["CordsLog", "Show all coordinates"])
    command_table.add_row(["BotOptions", "Set your nickname, server IP"])
    command_table.add_row(["NewBotOptions", "Set new Bot options"])
    command_table.add_row(["DelBotOptions", "Delete current bot options"])
    print(command_table)

def medias():
    media_table = PrettyTable()
    media_table.field_names = ["Platform", "Url"]
    media_table.add_row(["Youtube", "youtube.com/@FlyingLexmi"])
    media_table.add_row(["GitHub", "https://github.com/FlyingLexmi"])
    media_table.add_row(["Discord", "Url"])
    print(media_table)

def UserInput():
    while True:
        user_input = input(":> ")
        
        if user_input == "SpawnCords":
            delete()
            MainCords()
        elif user_input == "BotOptions":
            main()
        elif user_input == "NewBotOptions":
            delete_server_options()
            main()
        elif user_input == "--test":
            test()
        elif user_input == "DelBotOptions":
            delete_server_options()
        elif user_input == "AddAdmin":
                AddAdmin()
        elif user_input == "DelAdminList":
            deleteadminlist()
