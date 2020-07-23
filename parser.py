# Configuration options
# file name of the log file
f_name = "log.txt"
# time at which to start logging which players were online
start_log_time = "2020-07-21 21:31:08"
# time at which to stop logging which players were online
stop_log_time = "2020-07-22 08:32:06"

from colorama import *
init()

with open(f_name, "r") as f:
    lines = f.readlines()

players_online = []

stop_rem = False
stop_add = False

print("\nJoins and leaves:")

for line in lines:
    if "Player connected" in line:
        player = line.split(":")[3].replace(", xuid", "")[1:]
        time = f"{line.split(']')[0]}]".replace(" INFO", "")
        if not stop_add:
            players_online.append(player)
        print(f"{time} {Style.BRIGHT}{Fore.GREEN}join  + {player}{Style.RESET_ALL}")
    elif "Player disconnected" in line:
        player = line.split(":")[3].replace(", xuid", "")[1:]
        time = f"{line.split(']')[0]}]".replace(" INFO", "")
        if not stop_rem:
            players_online.pop(players_online.index(player))
        print(f"{time} {Style.BRIGHT}{Fore.RED}leave - {player}{Style.RESET_ALL}")

    if stop_log_time in line:
        stop_add = True

    if start_log_time in line:
        stop_rem = True

print("\nPlayers online during the given timeframe:")

for player in list(dict.fromkeys(players_online)):
    print(player)

deinit()
