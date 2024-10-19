import os
import subprocess

def create_server_options(nickname, server_ip):
    js_file_path = 'src/config/serverOptions.js'
    
    js_content = f"""const mineflayer = require('mineflayer');

const host = "{server_ip}";     
const nickname = "{nickname}"; 
const tag = "[Brikaine]"; 


async function ServerOptions() {{
    const bot = mineflayer.createBot({{
        username: "{nickname}",
        host: "{server_ip}",
    }});
}}

module.exports = {{
    ServerOptions
}};
"""
    with open(js_file_path, 'w') as js_file:
        js_file.write(js_content)

def serverTest(nickname, server_ip):
    js_file_path = 'src/config/serverOptions.js'
    
    js_content = f"""const mineflayer = require('mineflayer');

const host = "localhost";    
const nickname = "{nickname}"; 
const tag = "[Brikaine]"; 


async function ServerOptions() {{
    const bot = mineflayer.createBot({{
        username: "{nickname}",
        host: "{server_ip}",
    }});
}}

module.exports = {{
    ServerOptions
}};
"""
    with open(js_file_path, 'w') as js_file:
        js_file.write(js_content)



js_file_path = 'src/Brikaine.js'


def delete_server_options():
    js_file_path = 'src/config/serverOptions.js'
    if os.path.exists(js_file_path):
        os.remove(js_file_path)
        print(f"File {js_file_path} has been deleted.")
    else:
        print(f"File {js_file_path} not found.")








def main():
    nickname = input("Nickname: ")
    server_ip = input("Server: ")
    create_server_options(nickname, server_ip)




def test():
    serverTest("Brikaine", "localhost")



Bot_Cfg_Path = 'src/config/SpawnCords.js'
def MainCords():
    print("Enter bot main cordiantes")
    AddSpawnPointCords = input(":> ")
    x, y, z = map(float, AddSpawnPointCords.split(","))
    main_cords = f"\nSpawnPoint = new vec3({x}, {y}, {z});\n"
    with open(Bot_Cfg_Path, 'w') as js_file:
        js_file.write(main_cords)
        print(f"SpawnPoint updated")


def delete():
    spawn_file_path = 'src/config/SpawnCordinates.js'
    if os.path.exists(spawn_file_path):
        os.remove(spawn_file_path)
        print(f"File {spawn_file_path} has been deleted.")
    else:
        print(f"File {spawn_file_path} not found.")




def AddAdmin():
    spawn_file_path = 'src/config/adminList.js'
    print("Enter admin usernames separated by commas (e.g., user1,user2,user3)")
    AddAdmin = input(":> ")
    One, Two, Three = AddAdmin.split(",")
    main_cords = f"""const admins = ["{One.strip()}", "{Two.strip()}", "{Three.strip()}"];

module.exports = {{
    admins
}};
    """
    
    with open(spawn_file_path, 'a') as js_file:
        js_file.write(main_cords)
        print("Admin list updated")




def deleteadminlist():
    adminlist = 'src/config/adminList.js'
    if os.path.exists(adminlist):
        os.remove(adminlist)
        print(f"File {adminlist} has been deleted.")
    else:
        print(f"File {adminlist} not found.")