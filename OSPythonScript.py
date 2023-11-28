#Shebangline
#!/usr/bin/env python3


#IMPORTS
import re
import csv
import operator 


#DICTIONARIES
per_user = {}
errors = {}


logfile = ‘syslog.log’
f = open(logfile, ‘r’)
for log in f:
result = re.search(r”ticky: (INFO|ERROR) (.+?)\((.+)\)”,log)
if result.group(1) == ‘INFO’:
	category = result.group(1)
	message = result.group(2)
	name = result.group(3) 
	if name in per_user:
		user = per_user[name]
		user[category] += 1
	else: 
		per_user[name] = {'INFO':1, 'ERROR':0}
elif result.group(1) == ‘ERROR’:
	category = result.group(1)
	message = result.group(2)
	name = result.group(3) 
	if name in per_user:
		user = per_user[name]
		user[category] += 1
	else: 
		per_user[name] = {'INFO':0, 'ERROR':1}
sorted_messages = [("Error", "Count")] + sorted(error_messages.items(), key = operator.itemgetter(1), reverse=True)
sorted_users = [("Username", "INFO", "ERROR")] + sorted(per_user.items())[0:8]


with open("error_message.csv", "w") as error_file:
	for line in sorted_messages:
		error_file.write("{}, {}\n".format(line[0], line[1]))
with open("user_statistics.csv", "w") as user_file:
	for line in sorted_users:
		if isinstance(line[1], dict):
			user_file.write("{}, {}, {}\n".format(line[0], line[1].get("INFO"), line[1].get("ERROR")))
		else:
			user_file.write("{}, {}, {}\n".format(line[0], line[1], line[2]))
