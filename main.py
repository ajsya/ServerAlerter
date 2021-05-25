from tkinter import *
import os
import time
import requests
# from mcstatus import MinecraftServer
# from pynput.mouse import Button, Controller

os.system('clear')

# GUI

root = Tk()
root.title('Python App - Demo')
root.geometry("600x400")

# Settings
SendDiscordMessage = False #Send a discord message when server open (True/False)
DiscordWebhookURL = "" #Set a webhook url for the discord message to be sent to. Leave blank if SendDiscordMessage is set to False

# mouse = Controller()
# server = MinecraftServer.lookup(serverInput)

# status = server.status()
# playerCount = status.players.online
# maxPlayerCount = status.players.max
print("Minecraft Server Alerter \n \nCreated by SharkBaitBilly \nhttps://github.com/ajsya/ServerAlerter")

def start():
  status_label = Label(root, text="Hello " + myTextbox.get())
  status_label.pack()

myLabel = Label(root, text="Enter Server IP!")
myLabel.pack()

myTextbox = Entry(root, width=30)
myTextbox.pack()

myButton = Button(root, text="Submit", command=start)
myButton.pack()

while True:
    # status = server.status()
    # playerCount = status.players.online
    # print("The server has {0} players and replied in {1} ms".format(status.players.online, status.latency))
    if playerCount < maxPlayerCount:
        print('Server Open! There are only {0} player(s) online!'.format(status.players.online))
        # mouse.click(Button.right, 1)
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
    
root.mainloop()
