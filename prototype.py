import pickle
import datetime

girlsFileLine = "girls.pickle"
yeetMessage = "Would you like to yeet your girls?"

# Utility functions
def confirmedWithMessage(message):
	return userResponse(message + " (y/n): ") == "y"

def userResponse(message):
	# Honestly input is such a weird function name: 
	# It makes sense, but also doesn't make sense
	return input(message);

def newLine():
	# Lmao
	print()

# Database Functions
def openGirlsForWrite():
	return open(girlsFileLine, "wb")

def readGirlsIn():
	return pickle.load(open(girlsFileLine, "rb"))

def updateGirlsDatabase(girls):
	pickle.dump(girls, open(girlsFileLine, "wb"), pickle.HIGHEST_PROTOCOL)

# Girls Functions
def printGirlsPrettily(girls):
	print("Here's the list of your girls: ")
	for girl in girls:
		print("Name: " + girl)
		print("Current Level: " + str(girls[girl]["Levels"][-1]))
		print("Last updated: " + str(girls[girl]["updateTimes"][-1]))
		newLine()

def yeetGirls(girls):
	# Clears the dictionary of girls
	if (confirmedWithMessage(yeetMessage)):
		girls.clear()
		print("No more girls in your life sad ")

def addGirlToHaremWithConsent(girls):
	girl = userResponse("Enter your girl: ")
	level = int(userResponse("Enter your level: "))

	if (confirmedWithMessage("Add?")): 
		if (girl not in girls): 
			girls[girl] = {"Levels" : [level], "updateTimes" : [datetime.datetime.now()]}
		else:
			girls[girl]["Levels"] += [level]
			girls[girl]["updateTimes"] += [datetime.datetime.now()]
	
		print("Added!")
		newLine()
		printGirlsPrettily(girls)

	if (confirmedWithMessage("Add more girls? ")): addGirlToHaremWithConsent(girls)

def selectionLoop(girls):
	print("What would you like to do?")
	selection = userResponse("Options (type to select): [yeet, add]: ")
	newLine()

	if (selection == "yeet"): 
		yeetGirls(girls)
		newLine()
	elif (selection == "add"): addGirlToHaremWithConsent(girls)
	else: print("Do you think I got time to support your girls??")

	if (confirmedWithMessage("Do you want to do anything else?")): selectionLoop(girls)

def main():
	print("Welcome to GFL Level Tracker!")
	newLine()
	girls = readGirlsIn()
	printGirlsPrettily(girls)
	selectionLoop(girls)
	updateGirlsDatabase(girls)

if __name__ == "__main__":
	main()
