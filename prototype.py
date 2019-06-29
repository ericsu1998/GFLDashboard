import pickle
import datetime

girlsFileLine = "girls.pickle"
yeetMessage = "Would you like to yeet your girls?"

# Utility functions
def confirmedWithMessage(message):
	return userResponse(message + " (y/n):") == "y"

def userResponse(message):
	# Honestly input is such a weird function name: 
	# It makes sense, but also doesn't make sense
	return input(message + " ");

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
	if (len(girls) == 0): 
		print("You currently have no girls :(")
		newLine()
	else:
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
	girl = userResponse("Enter girl's name:")

	if (girl not in girls): 
		level = int(userResponse("Enter level:"))
		girls[girl] = {"Levels" : [level], "updateTimes" : [datetime.datetime.now()]}
		print("Added!")
	else:
		print("Your girl is already in the database")
	if (confirmedWithMessage("Add more girls?")): addGirlToHaremWithConsent(girls)

def updateGirl(girls):
	printGirlsPrettily(girls)
	girlToUpdate = userResponse("Who would you like to update? (Press q to go back to selection menu):")
	if (girlToUpdate == "q"): return
	elif (girlToUpdate not in girls): 
		print("Girl not found: try again")
		updateGirl(girls)
	else:
		level = int(userResponse("Enter level:"))
		girls[girlToUpdate]["Levels"] += [level]
		girls[girlToUpdate]["updateTimes"] += [datetime.datetime.now()]

def helpScreen():
	print("Options: yeet/add/update/list/exit/help")
	print("------------------------------------------")
	print("yeet: Clears all of your girls. Use with caution")
	print("add: Adds a new girl to your list")
	print("update: Updates an existing girl")
	print("list: Prints out all of the girls that you have")
	print("exit: Quits the application")
	print("help: Shows this screen")
	newLine()

def selectionLoop(girls):
	print("What would you like to do?")
	selection = userResponse("Options [clear, add, update, list, exit, help]:")
	newLine()

	if (selection == "exit"):
		return
	elif (selection == "update"):
		updateGirl(girls)
	elif (selection == "clear"): 
		yeetGirls(girls)
		newLine()
	elif (selection == "list"): printGirlsPrettily(girls)
	elif (selection == "add"): addGirlToHaremWithConsent(girls)
	elif (selection == "help"): helpScreen()
	else: print("Do you think I got time to support your girls??")
	selectionLoop(girls)

def main():
	print("Welcome to GFL Level Tracker!")
	newLine()
	girls = readGirlsIn()
	printGirlsPrettily(girls)
	selectionLoop(girls)
	updateGirlsDatabase(girls)
	print("Have a nice day!")

if __name__ == "__main__":
	main()
