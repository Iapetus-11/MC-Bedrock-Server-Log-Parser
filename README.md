# MC-Bedrock-Edition-Server-Log-Parser
## A log parser for vanilla Minecraft Bedrock Edition servers
* Lists all joins and leaves
* Gets all users online in the given timeframe
* Useful for figuring out who was on, and when they were

## Setup / Usage:
First, clone the repository:
```
git clone https://github.com/Iapetus-11/MC-Bedrock-Editon-Server-Log-Parser.git
cd MC-Bedrock-Editon-Server-Log-Parser
```

Then, open up parser.py and edit the file_name, start_log_time, and stop_log_time variables. Example:
```
# file name of the log file
file_name = "log.txt"

# time at which to start logging which players were online
start_log_time = "2020-07-21 21:31:08"

# time at which to stop logging which players were online
stop_log_time = "2020-07-22 08:32:06"
```

Then, just run the python file as one normally would (either `py parser.py` or `python3 parser.py` depending on whether you have windows or linux respectively)
