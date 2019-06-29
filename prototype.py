import os
import pickle
import datetime

girlsSaveFilesDirectory = "girlsFiles"
girlsFileLine = "girls.pickle"
yeetMessage = "Would you like to yeet your girls?"
noGirls = {}

expToNextLevel = { 1: 100, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600, 7: 700, 8: 800, 9: 900, 10: 1000,
				   11: 1100, 12: 1200, 13: 1300, 14: 1400, 15: 1500, 16: 1600, 17: 1700, 18: 1800, 19: 1900, 20: 2000,
				   21: 2100, 22: 2200, 23: 2300, 24: 2400, 25: 2500, 26: 2600, 27: 2800, 28: 3100, 29: 3400, 30: 4200,
				   31: 4600, 32: 5000, 33: 5400, 34: 5800, 35: 6300, 36: 6700, 37: 7200, 38: 7700, 39: 8200, 40: 8800,
				   41: 9300, 42: 9900, 43: 10500, 44: 11100, 45: 11800, 46: 12500, 47: 13100, 48: 13900, 49: 14600, 
				   50: 15400, 51: 16100, 52: 16900, 53: 17700, 54: 18600, 55: 19500, 56: 20400, 57: 21300, 58: 22300, 59: 23300,
				   60: 24300, 61: 25300, 62: 26300, 63: 27400, 64: 28500, 65: 29600, 66: 30800, 67: 32000, 68: 33200, 69: 34400,
				   70: 45100, 71: 46800, 72: 48600, 73: 50400, 74: 52200, 75: 54000, 76: 55900, 77: 57900, 78: 59800, 79: 61800,
				   80: 63900, 81: 66600, 82: 68100, 83: 70300, 84: 72600, 85: 74800, 86: 77100, 87: 79500, 88: 81900, 89: 84300,
				   90: 112600, 91: 116100, 92: 119500, 93: 123100, 94: 126700, 95: 130400, 96: 134100, 97: 137900, 98: 1419900, 99: 145700, 100: 0}

# Utility functions
def getSaveFilePath(fileName):
	return girlsSaveFilesDirectory + "/" + fileName

def confirmedWithMessage(message):
	return userResponse(message + " (y/n):") == "y"

def userResponse(message):
	# Honestly input is such a weird function name: 
	# It makes sense, but also doesn't make sense
	return input(message + " ");

def newLine():
	# Lmao
	print()

def getLevelFromInput():
	level = None
	try:
		level = int(userResponse("Enter level (1-100):"))
		if (level < 1 or level > 100): raise ValueError
	except ValueError:
		print("Level must be between 1 and 100!")
		getLevelFromInput()
	return level

def getExpFromInput():
	maxExp = 145699
	exp = None
	try:
		exp = int(userResponse("Enter exp (0-" + str(maxExp) + "):"))
		if (exp < 0 or exp > maxExp): raise ValueError
	except ValueError:
		print("Exp must be betwewen 0 and " + str(maxExp))
		getExpFromInput()
	return exp

# Database Functions
def updateGirlsDatabase(f, girls):
	pickle.dump(girls, open(f, "wb"), pickle.HIGHEST_PROTOCOL)
	
def initFile(fileName):
	filePath = getSaveFilePath(fileName)
	open(filePath, "w+")
	updateGirlsDatabase(filePath, noGirls)

def openGirlsForWrite():
	return open(girlsFileLine, "wb")

def readGirlsIn(f):
	return pickle.load(open(f, "rb"))

def printGirlsPrettily(girls):
	if (len(girls) == 0): 
		print("You currently have no girls :(")
		newLine()
	else:
		print("Here's the list of your girls: ")
		for girl in girls:
			print("Name: " + girl)
			currentLevel = girls[girl]["Levels"][-1]
			currentExp = girls[girl]["Exp"][-1]
			print("Current Level: " + str(currentLevel))
			print("Exp To Next Level: " + str(expToNextLevel[currentLevel] - currentExp))
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
		level = getLevelFromInput()
		exp = getExpFromInput()
		girls[girl] = {"Levels" : [level], "Exp" : [exp], "updateTimes" : [datetime.datetime.now()]}
		print("Added!")
	else:
		print("Your girl is already in the database")
	newLine()

def updateGirl(girls):
	girlToUpdate = userResponse("Who would you like to update? (Press q to go back to selection menu):")
	if (girlToUpdate == "q"): return
	elif (girlToUpdate not in girls): 
		print("Girl not found: try again")
		updateGirl(girls)
	else:
		level = int(userResponse("Enter level:"))
		exp = int(userResponse("Enter exp:"))
		girls[girlToUpdate]["Levels"] += [level]
		girls[girlToUpdate]["updateTimes"] += [datetime.datetime.now()]
		girls[girlToUpdate]["Exp"] += [exp]
		return

def deleteGirl(girls):
	girlToDelete = userResponse("Who would you like to delete? (Press q to go back to selection menu):")
	if (girlToDelete == "q"): return
	elif (girlToDelete not in girls):
		print("Your girl is not there...")
	else:
		del girls[girlToDelete]
	newLine()

def helpScreen():
	print("delete: Removes a girl")
	print("clear: Clears all of your girls. Use with caution")
	print("add: Adds a new girl to your list")
	print("update: Updates an existing girl")
	print("list: Prints out all of the girls that you have")
	print("exit: Quits the application")
	print("help: Shows this screen")
	newLine()

def selectionLoop(girls):
	print("What would you like to do?")
	selection = userResponse("Options [delete, clear, add, update, list, exit, help]:")
	newLine()

	if (selection == "exit"):
		return
	elif (selection == "delete"):
		deleteGirl(girls)
	elif (selection == "update"):
		updateGirl(girls)
	elif (selection == "clear"): 
		yeetGirls(girls)
		newLine()
	elif (selection == "list"): printGirlsPrettily(girls)
	elif (selection == "add"): addGirlToHaremWithConsent(girls)
	elif (selection == "help"): helpScreen()
	else: 
		print("Do you think I got time to support your girls??")
		newLine()

	selectionLoop(girls)

def main():
	filePath = None
	fileName = None

	if (not os.path.exists(girlsSaveFilesDirectory)): os.makedirs("girlsFiles")
	if (len(os.listdir(girlsSaveFilesDirectory)) == 0):
		print("It seems like you don't have any save files yet. ")
		fileName = userResponse("Choose a file name:")
		initFile(fileName)
	elif (len(os.listdir(girlsSaveFilesDirectory)) == 1):
		fileName = os.listdir(girlsSaveFilesDirectory)[0]
	else:
		print("Unimplented: Multiple save files")

	print("Welcome to GFL Level Tracker!")
	newLine()
	filePath = getSaveFilePath(fileName)
	girls = readGirlsIn(filePath)
	printGirlsPrettily(girls)
	selectionLoop(girls)
	updateGirlsDatabase(filePath, girls)
	print("Have a nice day!")

if __name__ == "__main__":
	main()
