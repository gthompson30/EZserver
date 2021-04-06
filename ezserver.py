# -*- coding: utf-8 -*-

print('Welcome to the EZServer setup!\n')

from configobj import ConfigObj
import Tkinter as tk
import urllib2
import os
import webbrowser
from pyngrok import ngrok
import thread
import subprocess

print('Imported modules ...')

options_list = [
    'view-distance',
    'max-build-height',
    'level-seed',
    'gamemode',
    'enable-command-block',
    'allow-nether',
    'server-port',
    'motd',
    'hardcore',
    'pvp',
    'spawn-npcs',
    'spawn-animals',
    'generate-structures',
    'snooper-enabled',
    'difficulty',
    'level-type',
    'spawn-monsters',
    'max-players',
    'spawn-protection',
    'online-mode',
    'allow-flight'
    ]

defaults = {
    'view-distance': '10',
    'max-build-height': '256',
    'level-seed': '',
    'gamemode': '0',
    'enable-command-block': 'false',
    'allow-nether': 'true',
    'server-port': '25565',
    'motd': 'A Minecraft Server',
    'hardcore': 'false',
    'pvp': 'true',
    'spawn-npcs': 'true',
    'spawn-animals': 'true',
    'generate-structures': 'true',
    'snooper-enabled': 'true',
    'difficulty': '1',
    'level-type': 'DEFAULT',
    'spawn-monsters': 'false',
    'max-players': '20',
    'spawn-protection': '16',
    'online-mode': 'false',
    'allow-flight': 'true'
    }

os.system('mkdir Server')

if not os.path.isfile('server.properties'):
    filedata = urllib2.urlopen('https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.16.5.jar')
    datatowrite = filedata.read()
    
    with open('craftbukkit-1.16.5.jar', 'wb') as f:
        f.write(datatowrite)
    
    print('Downloaded Server Software (Bukkit) ...')

    os.system('java -jar craftbukkit-1.16.5.jar')
    print('Ran Server Software (Bukkit) ...')

entries = []

def callback(url):
    webbrowser.open_new(url)

def start_ngrok(port):
    print('Setting up Ngrok tunnel ...')
    tunnel = ngrok.connect(port, 'tcp')
    print(tunnel[6:])

def start_bukkit(x):
    subprocess.call(['java', '-jar', 'craftbukkit-1.16.5.jar'])

def set_server_properties():
    config = ConfigObj("server.properties")
    config['view-distance'] = view_distance.get()
    config['max-build-height'] = max_build_height.get()
    config['level-seed'] = level_seed.get()
    config['gamemode'] = gamemode_var.get()
    config['enable-command-block'] = enable_command_block_var.get()
    config['allow-nether'] = allow_nether_var.get()
    config['server-port'] = server_port.get()
    config['motd'] = motd.get()
    config['hardcore'] = hardcore_var.get()
    config['pvp'] = pvp_var.get()
    config['spawn-npcs'] = spawn_npcs_var.get()
    config['spawn-animals'] = spawn_animals_var.get()
    config['generate-structures'] = generate_structures_var.get()
    config['snooper-enabled'] = snooper_enabled_var.get()
    config['difficulty'] = difficulty_var.get()
    config['level-type'] = level_type_var.get()
    config['spawn-monsters'] = spawn_monsters_var.get()
    config['max-players'] = max_players.get()
    config['spawn-protection'] = spawn_protection.get()
    config['online-mode'] = online_mode_var.get()
    config['allow-flight'] = allow_flight_var.get()
    config.write()

    data1 = ""
    
    with open('server.properties', 'r') as file:
        data1 = file.read()
    with open('server.properties', 'w') as file:
        file.write(data1.replace('""', ''))
    file.close()

    with open('eula.txt', 'r') as file:
        data = file.readlines()

    data[2] = 'eula=' + str(eula.get()).lower() + '\n'

    with open('eula.txt', 'w') as file:
        file.writelines( data )
    print('Running Server Software...')
    thread.start_new_thread(start_bukkit, (5,))
    print('Ran Server Software (Bukkit) ...')
    thread.start_new_thread(start_ngrok, (int(server_port.get()),))
    print('Started ngrok')
    #master.destroy()

master = tk.Tk()
master.title('EZServer 1.0')

for index, option in enumerate(options_list):
    tk.Label(master,
             text=option).grid(row=2+index)

gamemode = []
enable_command_block = []
allow_nether = []
hardcore = []
pvp = []
spawn_npcs = []
spawn_animals = []
generate_structures = []
snooper_enabled = []
difficulty = []
level_type = []
spawn_monsters = []
online_mode = []
allow_flight = []

view_distance = tk.Scale(master, from_=3, to=32, length=350, orient=tk.HORIZONTAL)
view_distance.grid(row=2, column=1, columnspan=10)
view_distance.set(10)

max_build_height = tk.Scale(master, from_=8, to=256, length=350, resolution=8, orient=tk.HORIZONTAL)
max_build_height.grid(row=3, column=1, columnspan=10)
max_build_height.set(256)

level_seed = tk.Entry(master, width=38)
level_seed.grid(row=4, column=1, columnspan=10)
level_seed.insert(tk.END, '(leave blank for random)')

gamemode_var = tk.IntVar()
gamemode.append(tk.Checkbutton(master, onvalue = 0, variable = gamemode_var, text='survival'))
gamemode.append(tk.Checkbutton(master, onvalue = 1, variable = gamemode_var, text='creative'))
gamemode.append(tk.Checkbutton(master, onvalue = 2, variable = gamemode_var, text='adventure'))
gamemode.append(tk.Checkbutton(master, onvalue = 3, variable = gamemode_var, text='spectator'))
gamemode[0].place(x=160, y=108)
gamemode[1].place(x=249, y=105)
gamemode[2].place(x=330, y=105)
gamemode[3].place(x=428, y=105)

enable_command_block_var = tk.IntVar()
enable_command_block.append(tk.Checkbutton(master, onvalue = 1, variable = enable_command_block_var, text='on'))
enable_command_block.append(tk.Checkbutton(master, onvalue = 0, variable = enable_command_block_var, text='off'))
enable_command_block[0].place(x=160, y=127)
enable_command_block[1].place(x=249, y=127)

allow_nether_var = tk.IntVar()
allow_nether.append(tk.Checkbutton(master, onvalue = 1, variable = allow_nether_var, text='on'))
allow_nether.append(tk.Checkbutton(master, onvalue = 0, variable = allow_nether_var, text='off'))
allow_nether[0].place(x=160, y=150)
allow_nether[1].place(x=249, y=150)

server_port = tk.Entry(master, width=38)
server_port.insert(tk.END, '25565')
server_port.grid(row=8, column=1, columnspan=10)

motd = tk.Entry(master, width=38)
motd.insert(tk.END, 'A Minecraft Server')
motd.grid(row=9, column=1, columnspan=10)

hardcore_var = tk.IntVar()
hardcore.append(tk.Checkbutton(master, onvalue = 1, variable = hardcore_var, text='on'))
hardcore.append(tk.Checkbutton(master, onvalue = 0, variable = hardcore_var, text='off'))
hardcore[0].place(x=160, y=228)
hardcore[1].place(x=249, y=228)
hardcore[1].select()

pvp_var = tk.IntVar()
pvp.append(tk.Checkbutton(master, onvalue = 1, variable = pvp_var, text='on'))
pvp.append(tk.Checkbutton(master, onvalue = 0, variable = pvp_var, text='off'))
pvp[0].place(x=160, y=251)
pvp[1].place(x=249, y=251)
pvp[0].select()

spawn_npcs_var = tk.IntVar()
spawn_npcs.append(tk.Checkbutton(master, onvalue = 1, variable = spawn_npcs_var, text='on'))
spawn_npcs.append(tk.Checkbutton(master, onvalue = 0, variable = spawn_npcs_var, text='off'))
spawn_npcs[0].place(x=160, y=273)
spawn_npcs[1].place(x=249, y=273)
spawn_npcs[0].select()

spawn_animals_var = tk.IntVar()
spawn_animals.append(tk.Checkbutton(master, onvalue = 1, variable = spawn_animals_var, text='on'))
spawn_animals.append(tk.Checkbutton(master, onvalue = 0, variable = spawn_animals_var, text='off'))
spawn_animals[0].place(x=160, y=294)
spawn_animals[1].place(x=249, y=294)
spawn_animals[0].select()

generate_structures_var = tk.IntVar()
generate_structures.append(tk.Checkbutton(master, onvalue = 1, variable = generate_structures_var, text='on'))
generate_structures.append(tk.Checkbutton(master, onvalue = 0, variable = generate_structures_var, text='off'))
generate_structures[0].place(x=160, y=315)
generate_structures[1].place(x=249, y=315)
generate_structures[0].select()

snooper_enabled_var = tk.IntVar()
snooper_enabled.append(tk.Checkbutton(master, onvalue = 1, variable = snooper_enabled_var, text='on'))
snooper_enabled.append(tk.Checkbutton(master, onvalue = 0, variable = snooper_enabled_var, text='off'))
snooper_enabled[0].place(x=160, y=337)
snooper_enabled[1].place(x=249, y=337)
snooper_enabled[0].select()

difficulty_var = tk.IntVar()
difficulty.append(tk.Checkbutton(master, onvalue = 0, variable = difficulty_var, text='peaceful'))
difficulty.append(tk.Checkbutton(master, onvalue = 1, variable = difficulty_var, text='easy'))
difficulty.append(tk.Checkbutton(master, onvalue = 2, variable = difficulty_var, text='normal'))
difficulty.append(tk.Checkbutton(master, onvalue = 3, variable = difficulty_var, text='hard'))
difficulty[0].place(x=160, y=358)
difficulty[1].place(x=249, y=358)
difficulty[2].place(x=330, y=358)
difficulty[3].place(x=428, y=358)
difficulty[2].select()

level_type_var = tk.StringVar()
level_type.append(tk.Checkbutton(master, onvalue = 'default', variable = level_type_var, text='default'))
level_type.append(tk.Checkbutton(master, onvalue = 'flat', variable = level_type_var, text='superflat'))
level_type.append(tk.Checkbutton(master, onvalue = 'largeBiomes', variable = level_type_var, text='largeBiomes'))
level_type.append(tk.Checkbutton(master, onvalue = 'amplified', variable = level_type_var, text='amplified'))
level_type[0].place(x=160, y=380)
level_type[1].place(x=249, y=380)
level_type[2].place(x=330, y=380)
level_type[3].place(x=428, y=380)
level_type[0].select()

spawn_monsters_var = tk.IntVar()
spawn_monsters.append(tk.Checkbutton(master, onvalue = 1, variable = spawn_monsters_var, text='on'))
spawn_monsters.append(tk.Checkbutton(master, onvalue = 0, variable = spawn_monsters_var, text='off'))
spawn_monsters[0].place(x=160, y=402)
spawn_monsters[1].place(x=249, y=402)
spawn_monsters[0].select()

max_players = tk.Entry(master, width=5)
max_players.insert(tk.END, '10')
max_players.place(x=160, y=422)

spawn_protection = tk.Scale(master, from_=0, to=32, length=350, orient=tk.HORIZONTAL)
spawn_protection.grid(row=20, column=1, columnspan=10)
spawn_protection.set(3)

online_mode_var = tk.IntVar()
online_mode.append(tk.Checkbutton(master, onvalue = 1, variable = online_mode_var, text='on'))
online_mode.append(tk.Checkbutton(master, onvalue = 0, variable = online_mode_var, text='off'))
online_mode[0].place(x=160, y=486)
online_mode[1].place(x=249, y=486)
online_mode[0].select()

allow_flight_var = tk.IntVar()
allow_flight.append(tk.Checkbutton(master, onvalue = 1, variable = allow_flight_var, text='on'))
allow_flight.append(tk.Checkbutton(master, onvalue = 0, variable = allow_flight_var, text='off'))
allow_flight[0].place(x=160, y=508)
allow_flight[1].place(x=249, y=508)
allow_flight[0].select()

link = tk.Label(master,
         text='\nEULA (set this\nto "true" to accept)', fg='blue', cursor='hand2')
link.grid(row=25)
link.bind('<Button-1>', lambda e: callback('https://account.mojang.com/documents/minecraft_eula'))

eula = tk.StringVar()
eulaEntry = tk.Entry(master, textvariable=eula).place(x=160, y=556)  

tk.Label(master,
         text='').grid(row=26)

tk.Label(master,
         text='Ngrok Authtoken', fg='red').grid(row=27)

password = tk.StringVar()
passwordEntry = tk.Entry(master, textvariable=password, show='•').place(x=160, y=605)  

tk.Label(master,
         text='').grid(row=28)

start = tk.Button(master, 
          text='Start Server', command=set_server_properties)

start.grid(row=29, column=1, sticky=tk.W, pady=4)

tk.Button(master, 
          text='Quit', command=master.destroy).grid(row=30, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)

tk.mainloop()
