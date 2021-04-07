#Created by SharkBaitBilly

import time
import requests
from mcstatus import MinecraftServer
from pynput.mouse import Button, Controller

mouse = Controller()

#serverInput = input("Enter Server IP!")
serverInput = "stoneworks.mcserv.fun"
server = MinecraftServer.lookup(serverInput)

status = server.status()
# print("The server has {0} players and replied in {1} ms".format(status.players.online, status.latency))
playerCount = status.players.online
print(playerCount)

while True:
    status = server.status()
    playerCount = status.players.online
    # print("The server has {0} players and replied in {1} ms".format(status.players.online, status.latency))
    if playerCount < 100:
        print('Server Open! There are only {0} player(s) online!'.format(status.players.online))
        mouse.click(Button.right, 1)
        url = "https://discord.com/api/webhooks/829110060834881586/lm0SXZHSg09kf2YKjlbwp3w-1RwvOLyOmOTpx-tJu93hx-oDz1bR-ey2yNTBFPrOZxKe"

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
        print('Server full currently with {0} players!'.format(status.players.online))
    
    time.sleep(0.1)
