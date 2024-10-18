from prettytable import PrettyTable
import os
from .botoptions import main, delete_server_options, test, MainCords

Bot_Cfg_Path = '../src/config/cfg.js'

def MultiToolCommands():
    command_table = PrettyTable()
    command_table.field_names = ["Command", "Overview"]
    command_table.add_row(["SpawnCords", "Set spawn coordinates"])
    command_table.add_row(["AddChestCoordinates", "Add chest coordinates to item counter"])
    command_table.add_row(["DelchestCordinates", "Deleting chest cordinates"])
    command_table.add_row(["CordsLog", "Show all coordinates"])
    command_table.add_row(["BotOptions", "set your nickname, server ip"])
    command_table.add_row(["NewBotOptions", "Set new Bot options"])
    command_table.add_row(["DelBotOptions", "Delete actual bot options"])
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
        UserInput = input(":> ")
        if UserInput == "SpawnCords":
           MainCords()
        if UserInput == "BotOptions":
            main()
        elif UserInput == "NewBotoptions":
            delete_server_options()
            main()
        elif UserInput == "--test":
            test()
        elif UserInput == "DelBotOptions":
            delete_server_options()

