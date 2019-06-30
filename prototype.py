import os
import pickle
import datetime

# Constants
girlsSaveFilesDirectory = "girlsFiles"
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
gunTypes = {"HG", "SMG", "RF", "AR", "MG", "SG"}

# Todo: add additional rewards (T-doll contracts, etc.)
# Maybe move this to json?
logisticsMissions = {"0-1" : {"manpower" : 0, "ammo" : 145, "rations" : 145, "parts" : 0, "Time" : 5/6},
			 "0-2" : {"manpower" : 550, "ammo" : 0, "rations" : 0, "parts" : 350, "Time" : 3},
			 "0-3" : {"manpower" : 900, "ammo" : 900, "rations" : 900, "parts" : 250, "Time" : 12},
			 "0-4" : {"manpower" : 0, "ammo" : 1200, "rations" : 800, "parts" : 750, "Time" : 24},
			 "1-1" : {"manpower" : 10, "ammo" : 30, "rations" : 15, "parts" : 0, "Time" : 0.25},
			 "1-2" : {"manpower" : 0, "ammo" : 40, "rations" : 60, "parts" : 0, "Time" : 0.5},
			 "1-3" : {"manpower" : 30, "ammo" : 0, "rations" : 30, "parts" : 10, "Time" : 1},
			 "1-4" : {"manpower" : 160, "ammo" : 160, "rations" : 0, "parts" : 0, "Time" : 2},
			 "2-1" : {"manpower" : 100, "ammo" : 0, "rations" : 0, "parts" : 30, "Time" : 2/3},
			 "2-2" : {"manpower" : 60, "ammo" : 200, "rations" : 80, "parts" : 0, "Time" : 1.5},
			 "2-3" : {"manpower" : 10, "ammo" : 10, "rations" : 10, "parts" : 230, "Time" : 4},
			 "2-4" : {"manpower" : 0, "ammo" : 250, "rations" : 600, "parts" : 60, "Time" : 6},
			 "3-1" : {"manpower" : 50, "ammo" : 0, "rations" : 75, "parts" : 0, "Time" : 1/3},
			 "3-2" : {"manpower" : 0, "ammo" : 120, "rations" : 70, "parts" : 30, "Time" : 0.75},
			 "3-3" : {"manpower" : 0, "ammo" : 300, "rations" : 0, "parts" : 0, "Time" : 1.5},
			 "3-4" : {"manpower" : 0, "ammo" : 0, "rations" : 300, "parts" : 300, "Time" : 5},
			 "4-1" : {"manpower" : 0, "ammo" : 185, "rations" : 185, "parts" : 0, "Time" : 1},
			 "4-2" : {"manpower" : 0, "ammo" : 0, "rations" : 0, "parts" : 210, "Time" : 2},
			 "4-3" : {"manpower" : 850, "ammo" : 550, "rations" : 0, "parts" : 0, "Time" : 6},
			 "4-4" : {"manpower" : 400, "ammo" : 400, "rations" : 400, "parts" : 150, "Time" : 8},
			 "5-1" : {"manpower" : 0, "ammo" : 0, "rations" : 100, "parts" : 45, "Time" : 0.5},
			 "5-2" : {"manpower" : 0, "ammo" : 600, "rations" : 300, "parts" : 0, "Time" : 2.5},
			 "5-3" : {"manpower" : 800, "ammo" : 400, "rations" : 400, "parts" : 0, "Time" : 4},
			 "5-4" : {"manpower" : 100, "ammo" : 0, "rations" : 0, "parts" : 700, "Time" : 7},
			 "6-1" : {"manpower" : 300, "ammo" : 300, "rations" : 0, "parts" : 100, "Time" : 2},
			 "6-2" : {"manpower" : 0, "ammo" : 200, "rations" : 550, "parts" : 100, "Time" : 3},
			 "6-3" : {"manpower" : 0, "ammo" : 0, "rations" : 200, "parts" : 500, "Time" : 5},
			 "6-4" : {"manpower" : 800, "ammo" : 800, "rations" : 800, "parts" : 0, "Time" : 12},
			 "7-1" : {"manpower" : 650, "ammo" : 0, "rations" : 650, "parts" : 0, "Time" : 2.5},
			 "7-2" : {"manpower" : 0, "ammo" : 650, "rations" : 0, "parts" : 300, "Time" : 4},
			 "7-3" : {"manpower" : 900, "ammo" : 600, "rations" : 600, "parts" : 0, "Time" : 5.5}, 
			 "7-4" : {"manpower" : 250, "ammo" : 250, "rations" : 250, "parts" : 600, "Time" : 8},
			 "8-1" : {"manpower" : 150, "ammo" : 150, "rations" : 150, "parts" : 0, "Time" : 1},
			 "8-2" : {"manpower" : 0, "ammo" : 0, "rations" : 0, "parts" : 450, "Time" : 3},
			 "8-3" : {"manpower" : 400, "ammo" : 800, "rations" : 400, "parts" : 0, "Time" : 6},
			 "8-4" : {"manpower" : 1500, "ammo" : 400, "rations" : 400, "parts" : 100, "Time" : 9}}

# Classes 
class Girls:
	def __init__(self, girls):
		self.girls = girls
	
	@staticmethod
	def newGirls():
		return __init__({})

	def getGunType(self, girl):
		return self.girls[girl].getGunType()
	
	def getCurrentLevel(self, girl):
		return self.girls[girl].getCurrentLevel()
	
	def getCurrentExp(self, girl):
		return self.girls[girl].getCurrentExp()

	def getCurrentTime(self, girl): 
		return self.girls[girl].getCurrentTime()
	
	def getExpToNextLevel(self, girl):
		return self.girls[girl].getExpToNextLevel()

	def addGirlToHaremWithConsent(self):
		girl = userResponse("Enter girl's name:")
		if (girl not in self.girls): 
			gunType = getGunTypeFromInput()
			level = getLevelFromInput()
			exp = getExpFromInput()
			self.girls[girl] = Girl(gunType, level, exp)
			print("Added!")
		else:
			print("Your girl is already in the database")
		newLine()

	def deleteGirl(self, girl):
		if (girl not in self.girls):
			print("Your girl is not there...")
		else:
			del self.girls[girl]

	def updateGirl(self, girlToUpdate):
		if (girlToUpdate not in self.girls): 
			print("Girl not found: try again")
			self.updateGirl(self, girls)
		else:
			level = int(userResponse("Enter level:"))
			exp = int(userResponse("Enter exp:"))
			self.girls[girlToUpdate].updateGirl(level, exp)
			return

	def listGirls(self):
		if (len(self.girls) == 0): 
			print("You currently have no girls :(")
			newLine()
		else:
			print("Here's the list of your girls: ")
			for girl in self.girls:
				print("Name: " + girl)
				gunType = self.getGunType(girl)
				currentLevel = self.getCurrentLevel(girl)
				currentExp = self.getCurrentExp(girl)
				currentTime = self.getCurrentTime(girl)
				print("Gun Type: " + gunType)
				print("Current Level: " + str(currentLevel))
				print("Exp To Next Level: " + str(self.getExpToNextLevel(girl)))
				print("Last updated: " + str(currentTime))
				newLine()

class Girl:
	def __init__(self, gunType, level, exp):
		self.gunType = gunType
		self.levels = [level]
		self.exps = [exp]
		self.times = [datetime.datetime.now()]

	def getGunType(self): return self.gunType

	def getCurrentLevel(self):
		return self.levels[-1]

	def getCurrentExp(self):
		return self.exps[-1]

	def getCurrentTime(self):
		return self.times[-1]

	def getExpToNextLevel(self):
		return expToNextLevel[self.getCurrentLevel()] - self.getCurrentExp()

	def updateGirl(self, level, exp):
		# Shares name with another method. Change name maybe?
		self.levels += [level]
		self.exps += [exp]
		self.times += [datetime.datetime.now()]

# Utility functions
def getSaveFilePath(fileName):
	return girlsSaveFilesDirectory + "/" + fileName

def confirmedWithMessage(message):
	return userResponse(message + " (y/n):") == "y"

def userResponse(message):
	# Honestly input is such a weird function name: 
	# It makes sense, but also doesn't make sense
	return input(message + " ")

def newLine():
	# Lmao
	print()

def getGunTypeFromInput():
	gunType = None
	try:
		gunType = userResponse("Enter gun type (HG, SMG, RF, AR, MG, SG):")
		if (gunType not in gunTypes): raise ValueError
	except ValueError:
		print("You entered an invalid gun type, please try again.")
		getGunTypeFromInput()
	return gunType

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
	updateGirlsDatabase(filePath, Girls())

def readGirlsIn(f):
	return pickle.load(open(f, "rb"))

def yeetGirls(girls):
	# Clears the dictionary of girls
	if (confirmedWithMessage(yeetMessage)):
		girls.clear()
		print("No more girls in your life sad ")

def deleteGirl(girls):
	girlToDelete = userResponse("Who would you like to delete? (Press q to go back to selection menu):")
	if (girlToDelete == "q"): return
	else:
		girls.deleteGirl(girlToDelete)
	newLine()

def updateGirl(girls):
	girlToUpdate = userResponse("Who would you like to update? (Press q to go back to selection menu):")
	if (girlToUpdate == "q"): return
	else:
		girls.updateGirl(girlToUpdate)

def getResource(mission, resourceType):
	if resourceType.lower() in {"m", "manpower"}: return mission["manpower"]
	elif resourceType.lower() in {"a", "ammo"}: return mission["ammo"]
	elif resourceType.lower() in {"r", "rations"}: return mission["rations"]
	elif resourceType.lower() in {"p", "parts"}: return mission["parts"]
	elif resourceType.lower() == "all": return mission["manpower"] + mission["ammo"] + mission["rations"] + mission["parts"]

def logisticHelpScreen():
	print("m or manpower: Optimize for manpower")
	print("a or ammo: Optimize for ammo")
	print("r or rations: Optimize for rations")
	print("p or parts: Optimize for parts")
	print("all: Optimize for all resources")
	print("h or help: Shows this screen")
	newLine()

possibleResourceTypeChoices = {"m", "a", "r", "p", "manpower", "ammo",
							   "rations", "parts", "all"}		
def logisticsScreen():
	resourceType = None
	while (True):
		resourceType = userResponse("Which resource would you like to get? (help for list of commands):")
		if resourceType in {"h", "help"}: logisticHelpScreen()
		elif resourceType in possibleResourceTypeChoices: break
		else: print("You entered an invalid resource type, try again")
	
	if (resourceType in {"h", "help"}): 
		logisticHelpScreen()

	# Currently only prints the first 4
	allResourcesPerHourMissions = []
	for missionName in logisticsMissions:
		mission = logisticsMissions[missionName]
		timeHours = mission["Time"]
		allResourcesPerHour = getResource(mission, resourceType) / timeHours
		allResourcesPerHourMissions.append((missionName, allResourcesPerHour, timeHours))

	itemsToPrint = 4
	allResourcesPerHourMissions.sort(key = lambda x: x[1], reverse = True)
	newLine()
	print("Top " + str(itemsToPrint) + " Missions " + "(" + resourceType + ")")
	print("-------------------------")
	for logisticMission in allResourcesPerHourMissions[:itemsToPrint]:
		print(logisticMission[0] + ": " + str(round(logisticMission[1], 2)) + " (" + str(logisticMission[2]) + " hours)")
	newLine()

def helpScreen():
	print("d or delete: Removes a girl")
	print("c or clear: Clears all of your girls. Use with caution")
	print("a or add: Adds a new girl to your list")
	print("u or update: Updates an existing girl")
	print("ls or list: Prints out all of the girls that you have")
	print("q or quit: Quits the application")
	print("h or help: Shows this screen")
	print("l or logistics: " "Takes you to logistics page")
	newLine()

def selectionLoop(girls):
	selection = userResponse("What would you like to do? (help for list of commands):")
	newLine()

	if (selection in {"q", "quit"}):
		return
	elif (selection in {"d", "delete"}):
		deleteGirl(girls)
	elif (selection in {"u", "update"}):
		updateGirl(girls)
	elif (selection in {"c", "clear"}): 
		yeetGirls(girls)
		newLine()
	elif (selection in {"ls", "list"}): girls.listGirls()
	elif (selection in {"a", "add"}): girls.addGirlToHaremWithConsent()
	elif (selection in {"l", "logistics"}): logisticsScreen()
	elif (selection in {"h", "help"}): helpScreen()
	else: 
		print("Do you think I got time to support your girls??")
		newLine()

	selectionLoop(girls)

def main():
	filePath = None
	fileName = None

	# Automatically generate save files
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
	girls.listGirls()
	selectionLoop(girls)
	updateGirlsDatabase(filePath, girls)
	print("Have a nice day!")

if __name__ == "__main__":
	main()
