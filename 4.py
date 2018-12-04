import re

def parseLine(content):
	m = re.search('\[\d{4}-\d{2}-\d{2} \d{2}:(\d{2})\] (falls|wakes|Guard #(\d*))', line)
	return m.groups()

file = open("input4.txt", "r")
content = file.readlines()
content.sort()
currentGuard = 0
asleep = False
guards = dict()
#loop through the lines, adding 1 to each minute that a guard is asleep
for line in content:
	[minute, change, guardID] = parseLine(line)
	if guardID is not None:
		if asleep is not False:
			for i in range(asleep, 60):
				guards[currentGuard][i] = guards[currentGuard][i] + 1
		currentGuard = int(guardID)
		asleep = False
		if not currentGuard in guards:
			guards[currentGuard] = [0 for x in range(60)] 
		continue
	if change == 'falls' and asleep is False:
		asleep = int(minute)
	elif asleep is not False:
		for i in range(asleep, int(minute)):
			guards[currentGuard][i] = guards[currentGuard][i] + 1
		asleep = False

#Find which guard slept the most total minutes
mostest = 0
sleepiest = 0
for (guard, minutes) in guards.items():
	total = 0
	for i, value in enumerate(minutes):
		total = total + value
	if total > mostest:
		mostest = total
		sleepiest = guard

#Find on which minute that guard slept the most
mostest = 0
sleepiestMinute = 0
for minute, value in enumerate(guards[sleepiest]):
	if value > mostest:
		mostest = value
		sleepiestMinute = minute

print sleepiestMinute * sleepiest

#Find which guard was asleep the most on any minute
mostest = 0
sleepiest = 0
minute = 0
for (guard, minutes) in guards.items():
	for i, value in enumerate(minutes):
		if value > mostest:
			mostest = value
			sleepiest = guard
			minute = i

print sleepiest * minute
