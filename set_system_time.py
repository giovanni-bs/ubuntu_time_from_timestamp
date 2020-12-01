import json
import datetime
import subprocess
import shlex

current_dir = "/home/.../"

try:
	with open(current_dir + 'gps.json') as json_file:
		gps = json.load(json_file)
	timestamp = (datetime.datetime.fromtimestamp(gps['timestamp']))
	systemtime = timestamp.strftime('%d %b %Y %H:%M:%S%f')[:-6]
	print(systemtime)
	subprocess.call(shlex.split("timedatectl set-ntp false"))
	subprocess.call(shlex.split("sudo date -s '%s'" % systemtime))
	subprocess.call(shlex.split("sudo hwclock -w"))

except:
	print("\nJson error\n")
