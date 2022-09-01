# GOALS -
# Download static file from server every 500ms to test wifi strength
# save download time and current time to file

import time
import datetime
import requests

def startTest():
	"""
	Runs loop every 500 milliseconds testing connection and saving duration to file
	Loop ends when device cannot retrieve file anymore
	"""
	index = 0
	prevDuration = 0
	while (prevDuration > -1):
		print ("#" + str(index))
		index += 1
		duration = pingServer()
		if (duration == -1):
			saveToFile("Cannot get file")
		else:
			saveToFile(duration)
		prevDuration = duration
		time.sleep(.5)

def pingServer():
	"""
	Requests portal.myluxedo.com/static/luxedo/icons/hexagon.svg?vsn=3.18.0 returning amount of time it took to retrieve
	Returns: 
		(number): the amount of time it took to retreive icon or -1 if could not retrieve
	"""
	print('Pinging server.')

	before_time = currentTime()

	# If cannot get icon, return -1
	try:
		requests.get('https://portal.myluxedo.com/static/luxedo/icons/hexagon.svg?vsn=3.18.0')
	except:
		print('Cannot get icon!')
		return -1

	after_time = currentTime()
	return after_time - before_time


def saveToFile(duration):
	"""
	Saves duration to /wifi-test-results.txt with current timestamp

	Args:
		duration (number): an amount of time in milliseconds
	"""
	with open("RESULTS.txt", 'a+') as file:
		writeString = "[" + str(datetime.datetime.now()) + "]: " + str(duration) + "\n"
		file.write(writeString)

def currentTime():
	"""
	Gets current time in milliseconds
	"""
	return round(time.time() * 1000)


startTest()
