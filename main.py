#Created by SharkBaitBilly
#https://github.com/ajsya/ServerAlerter

import time
import requests
from mcstatus import MinecraftServer
from pynput.mouse import Button, Controller

# Settings
SendDiscordMessage = False #Send a discord message when server open (True/False)
DiscordWebhookURL = "" #Set a webhook url for the discord message to be sent to. Leave blank if SendDiscordMessage is set to False
serverInput = input("Enter Server IP!")
#serverInput = "" #OPTIONAL Enter a predefined server here than delete the hashtag and line above

mouse = Controller()
server = MinecraftServer.lookup(serverInput)

status = server.status()
playerCount = status.players.online
maxPlayerCount = status.players.max
print("Minecraft Server Alerter \n \nCreated by SharkBaitBilly \nhttps://github.com/ajsya/ServerAlerter")

while True:
    status = server.status()
    playerCount = status.players.online
    # print("The server has {0} players and replied in {1} ms".format(status.players.online, status.latency))
    if playerCount < maxPlayerCount:
        print('Server Open! There are only {0} player(s) online!'.format(status.players.online))
        mouse.click(Button.right, 1)
        if SendDiscordMessage == True:
            url = DiscordWebhookURL
            
            data = {
                "content" : 'Server Open! There are only {0} player(s) online! ||@here||'.format(status.players.online),
                "username" : serverInput
            }
            
            result = requests.post(url, json = data)
            
            try:
                result.raise_for_status()
            except requests.exceptions.HTTPError as err:
                print(err)
            else:
                print("Message sent successfully, code {}.".format(result.status_code))
    else:
        print('Server currently full with {0} players online!'.format(status.players.online))
    
    time.sleep(0.1) # Set the time interval between each request (in seconds)
