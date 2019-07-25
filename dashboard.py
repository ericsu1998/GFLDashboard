import os
import pickle
import datetime

# Constants
girlsSaveFilesDirectory = "girlsFiles"
yeetMessage = "Would you like to yeet your girls?"
noGirls = {}

girlsDatabaseHighRarity = { 
	"Grizzly" : {"Type" : "HG", "Rarity" : 5}, "M950A" : {"Type" : "HG", "Rarity" : 5},
	"Welrod Mk II" : {"Type" : "HG", "Rarity" : 5}, "Contender" : {"Type" : "HG", "Rarity" : 5}, 
	"SAA" : {"Type" : "HG", "Rarity" : 4}, "Stechkin" : {"Type" : "HG", "Rarity" : 4},
	"Gr Mk23" : {"Type" : "HG", "Rarity" : 4}, "P7" : {"Type" : "HG", "Rarity" : 4},
	"Spitfire" : {"Type" : "HG", "Rarity" : 4}, "K5" : {"Type" : "HG", "Rarity" : 4}, 
	"Jericho" : {"Type" : "HG", "Rarity" : 4}, "M9" : {"Type" : "HG", "Rarity" : 3},
	"Tokarev" : {"Type" : "HG", "Rarity" : 3}, "Makarov" : {"Type" : "HG", "Rarity" : 3},
	"P08" : {"Type" : "HG", "Rarity" : 3}, "C96" : {"Type" : "HG", "Rarity" : 3},
	"Type92" : {"Type" : "HG", "Rarity" : 3}, "Astra" : {"Type" : "HG", "Rarity" : 3},
	"P99" : {"Type" : "HG", "Rarity" : 3}, "M1911" : {"Type" : "HG", "Rarity" : 2},
	"M1895" : {"Type" : "HG", "Rarity" : 2}, "P38" : {"Type" : "HG", "Rarity" : 2},
	"PPK" : {"Type" : "HG", "Rarity" : 2}, "FF FNP9" : {"Type" : "HG", "Rarity" : 2},
	"MP-446" : {"Type" : "HG", "Rarity" : 2}, "Bren Ten" : {"Type" : "HG", "Rarity" : 2},
	"Gr USPCompact" : {"Type" : "HG", "Rarity" : 2},
			  
	"Thompson" : {"Type" : "SMG", "Rarity" : 5}, "Vector" : {"Type" : "SMG", "Rarity" : 5},
	"Gr G36c" : {"Type" : "SMG", "Rarity" : 5}, "Suomi" : {"Type" : "SMG", "Rarity" : 5},
	"Type79" : {"Type" : "SMG", "Rarity" : 5}, "SR-3MP" : {"Type" : "SMG", "Rarity" : 5},
	"C-MS" : {"Type" : "SMG", "Rarity" : 5}, "100 Shiki" : {"Type" : "SMG", "Rarity" : 5},
	"PP-90" : {"Type" : "SMG", "Rarity" : 4}, "GR-MP5" : {"Type" : "SMG", "Rarity" : 4},
	"UMP9" : {"Type" : "SMG", "Rarity" : 4}, "UMP45" : {"Type" : "SMG", "Rarity" : 4},
	"PP-19-01" : {"Type" : "SMG", "Rarity" : 4}, "Shipka" : {"Type" : "SMG", "Rarity" : 4},
	"Ingram" : {"Type" : "SMG", "Rarity" : 3}, "PPS-43" : {"Type" : "SMG", "Rarity" : 3},
	"Skorpion" : {"Type" : "SMG", "Rarity" : 3}, "STEN MK II" : {"Type" : "SMG", "Rarity" : 3},
	"Micro Uzi" : {"Type" : "SMG", "Rarity" : 3},
	"M3" : {"Type" : "SMG", "Rarity" : 2}, "PPsh-41" : {"Type" : "SMG", "Rarity" : 2},
	"PP-2000" : {"Type" : "SMG", "Rarity" : 2}, "MP-40" : {"Type" : "SMG", "Rarity" : 2},
	"M38" : {"Type" : "SMG", "Rarity" : 2}, "m45" : {"Type" : "SMG", "Rarity" : 2},
	"Spectre M4" : {"Type" : "SMG", "Rarity" : 2}, "IDW" : {"Type" : "SMG", "Rarity" : 2}, "Type64" : {"Type" : "SMG", "Rarity" : 2},

	"Kar98K" : {"Type" : "RF", "Rarity" : 5}, "WA2000" : {"Type" : "RF", "Rarity" : 5},
	"Lee Enfield" : {"Type" : "RF", "Rarity" : 5}, "NTW-20" : {"Type" : "RF", "Rarity" : 5},
	"M99" : {"Type" : "RF", "Rarity" : 5}, "IWS 2000" : {"Type" : "RF", "Rarity" : 5},
	"Carcano M1891" : {"Type" : "RF", "Rarity" : 5}, "Carcano M91/38" : {"Type" : "RF", "Rarity" : 5},
	"M200" : {"Type" : "RF", "Rarity" : 5}, 
	"Springfield" : {"Type" : "RF", "Rarity" : 4}, "Mosin-Nagant" : {"Type" : "RF", "Rarity" : 4}, 
	"PTRD" : {"Type" : "RF", "Rarity" : 4}, "SVD" : {"Type" : "RF", "Rarity" : 4},
	"T-5000" : {"Type" : "RF", "Rarity" : 4}, "SPR A3G" : {"Type" : "RF", "Rarity" : 4},
	"M1 Garand" : {"Type" : "RF", "Rarity" : 3}, "M14" : {"Type" : "RF", "Rarity" : 3},
	"SV-98" : {"Type" : "RF", "Rarity" : 3}, "Type88" : {"Type" : "RF", "Rarity" : 3},
	"SVT-38" : {"Type" : "RF", "Rarity" : 2}, "SKS" : {"Type" : "RF", "Rarity" : 2},
	"G43" : {"Type" : "RF", "Rarity" : 2}, "FF FN49" : {"Type" : "RF", "Rarity" : 2},
	"VM59" : {"Type" : "RF", "Rarity" : 2},
	
	"GR G41" : {"Type" : "AR", "Rarity" : 5}, "416" : {"Type" : "AR", "Rarity" : 5},
	"FAL" : {"Type" : "AR", "Rarity" : 5}, "GR G11" : {"Type" : "AR", "Rarity" : 5},
	"Type95" : {"Type" : "AR", "Rarity" : 5}, "Type97" : {"Type" : "AR", "Rarity" : 5},
	"Am RFB" : {"Type" : "AR", "Rarity" : 5}, "T91" : {"Type" : "AR", "Rarity" : 5},
	"K2" : {"Type" : "AR", "Rarity" : 5}, "Zas M21" : {"Type" : "AR", "Rarity" : 5},
	"MDR" : {"Type" : "AR", "Rarity" : 5}, "K11" : {"Type" : "AR", "Rarity" : 5},
	"64 Shiki" : {"Type" : "AR", "Rarity" : 5}, "AS Val" : {"Type" : "AR", "Rarity" : 4}, "Gr G36" : {"Type" : "AR", "Rarity" : 4},
	"Type 56-1" : {"Type" : "AR", "Rarity" : 4}, "FR FAMAS" : {"Type" : "AR", "Rarity" : 4},
	"TAR-21" : {"Type" : "AR", "Rarity" : 4}, "9A-91" : {"Type" : "AR", "Rarity" : 4},
	"Ribeyrolles" : {"Type" : "AR", "Rarity" : 4}, "XM8" : {"Type" : "AR", "Rarity" : 4},
	"AK-47" : {"Type" : "AR", "Rarity" : 3}, "StG44" : {"Type" : "AR", "Rarity" : 3}, 
	"FF FNC" : {"Type" : "AR", "Rarity" : 3}, "OTs-12" : {"Type" : "AR", "Rarity" : 3}, 
	"Gr G3" : {"Type" : "AR", "Rarity" : 2}, "L85Al" : {"Type" : "AR", "Rarity" : 2},	
	"Galil" : {"Type" : "AR", "Rarity" : 2}, "SIG-510" : {"Type" : "AR", "Rarity" : 2},
	"FF F2000" : {"Type" : "AR", "Rarity" : 2}, "Type63" : {"Type" : "AR", "Rarity" : 2},
	
	"GR MG5" : {"Type" : "MG", "Rarity" : 5}, "Negev" : {"Type" : "MG", "Rarity" : 5},
	"Gr MG4" : {"Type" : "MG", "Rarity" : 5}, "PKP" : {"Type" : "MG", "Rarity" : 5},
	"M1918" : {"Type" : "MG", "Rarity" : 4}, "M60" : {"Type" : "MG", "Rarity" : 4},
	"PK" : {"Type" : "MG", "Rarity" : 4}, "MG3" : {"Type" : "MG", "Rarity" : 4},
	"MK48" : {"Type" : "MG", "Rarity" : 4}, "AEK-999" : {"Type" : "MG", "Rarity" : 4},
	"Ameli" : {"Type" : "MG", "Rarity" : 4}, "Type80" : {"Type" : "MG", "Rarity" : 4},
	"M2HB" : {"Type" : "MG", "Rarity" : 3}, "M1919A4" : {"Type" : "MG", "Rarity" : 3}, 
	"MG42" : {"Type" : "MG", "Rarity" : 3},  "Bren" : {"Type" : "MG", "Rarity" : 3}, 
	"LWMMG" : {"Type" : "MG", "Rarity" : 2}, "DP28" : {"Type" : "MG", "Rarity" : 2},
	"MG34" : {"Type" : "MG", "Rarity" : 2}, "FG42" : {"Type" : "MG", "Rarity" : 2},
	"AAT-52" : {"Type" : "MG", "Rarity" : 2},

	"Am KSG" : {"Type" : "SG", "Rarity" : 5}, "AA-12" : {"Type" : "SG", "Rarity" : 5},
	"S.A.T.8" : {"Type" : "SG", "Rarity" : 5}, "M37" : {"Type" : "SG", "Rarity" : 4},
	"M590" : {"Type" : "SG", "Rarity" : 4}, "Super-Shorty" : {"Type" : "SG", "Rarity" : 4},
	"SPAS-12" : {"Type" : "SG", "Rarity" : 4}, "M1014" : {"Type" : "SG", "Rarity" : 4},
	"USAS-12" : {"Type" : "SG", "Rarity" : 4}, "M500" : {"Type" : "SG", "Rarity" : 3},
	"KS-23" : {"Type" : "SG", "Rarity" : 3}, "RMB-93" : {"Type" : "SG", "Rarity" : 3},
	"NS2000" : {"Type" : "SG", "Rarity" : 3},		  
}

expToNextLevel = { 
	 1:    100,  2:    200,  3:    300,  4:    400,  5:   500,   6:    600,  7:    700,  8:    800,  9:    900,  10:  1000,
	11:   1100, 12:   1200, 13:   1300, 14:   1400, 15:  1500,  16:   1600, 17:   1700, 18:   1800, 19:   1900,  20:   2000,
	21:   2100, 22:   2200, 23:   2300, 24:   2400, 25:  2500,  26:   2600, 27:   2800, 28:   3100, 29:   3400,  30:   4200,
	31:   4600, 32:   5000, 33:   5400, 34:   5800, 35:  6300,  36:   6700, 37:   7200, 38:   7700, 39:   8200,  40:   8800,
	41:   9300, 42:   9900, 43:  10500, 44:  11100, 45:  11800, 46:  12500, 47:  13100, 48:  13900, 49:  14600,  50:  15400, 
	51:  16100, 52:  16900, 53:  17700, 54:  18600, 55:  19500, 56:  20400, 57:  21300, 58:  22300, 59:  23300,  60:  24300, 
	61:  25300, 62:  26300, 63:  27400, 64:  28500, 65:  29600, 66:  30800, 67:  32000, 68:  33200, 69:  34400,  70:  45100, 
	71:  46800, 72:  48600, 73:  50400, 74:  52200, 75:  54000, 76:  55900, 77:  57900, 78:  59800, 79:  61800,  80:  63900, 
	81:  66600, 82:  68100, 83:  70300, 84:  72600, 85:  74800, 86:  77100, 87:  79500, 88:  81900, 89:  84300,  90: 112600, 
	91: 116100, 92: 119500, 93: 123100, 94: 126700, 95: 130400, 96: 134100, 97: 137900, 98: 141800, 99: 145700, 100:      0
}

gunTypes = {"HG", "SMG", "RF", "AR", "MG", "SG"}

# Todo: add additional rewards (T-doll contracts, etc.)
# Maybe move this to json?
logisticsMissions = { 
	"0-1" : {"manpower" :    0, "ammo" :  145, "rations" :  145, "parts" :   0, "Time" : 5/6},
	"0-2" : {"manpower" :  550, "ammo" :    0,  "rations" :   0, "parts" : 350, "Time" : 3},
	"0-3" : {"manpower" :  900, "ammo" :  900, "rations" :  900, "parts" : 250, "Time" : 12},
	"0-4" : {"manpower" :    0, "ammo" : 1200, "rations" :  800, "parts" : 750, "Time" : 24},
	"1-1" : {"manpower" :   10, "ammo" :   30, "rations" :   15, "parts" :   0, "Time" : 0.25},
	"1-2" : {"manpower" :    0, "ammo" :   40, "rations" :   60, "parts" :   0, "Time" : 0.5},
	"1-3" : {"manpower" :   30, "ammo" :    0, "rations" :   30, "parts" :  10, "Time" : 1},
	"1-4" : {"manpower" :  160, "ammo" :  160, "rations" :    0, "parts" :   0, "Time" : 2},
	"2-1" : {"manpower" :  100, "ammo" :    0, "rations" :    0, "parts" :  30, "Time" : 2/3},
	"2-2" : {"manpower" :   60, "ammo" :  200, "rations" :   80, "parts" :   0, "Time" : 1.5},
	"2-3" : {"manpower" :   10, "ammo" :   10, "rations" :   10, "parts" : 230, "Time" : 4},
	"2-4" : {"manpower" :    0, "ammo" :  250, "rations" :  600, "parts" :  60, "Time" : 6},
	"3-1" : {"manpower" :   50, "ammo" :    0, "rations" :   75, "parts" :   0, "Time" : 1/3},
	"3-2" : {"manpower" :    0, "ammo" :  120, "rations" :   70, "parts" :  30, "Time" : 0.75},
	"3-3" : {"manpower" :    0, "ammo" :  300, "rations" :    0, "parts" :   0, "Time" : 1.5},
	"3-4" : {"manpower" :    0, "ammo" :    0, "rations" :  300, "parts" : 300, "Time" : 5},
	"4-1" : {"manpower" :    0, "ammo" :  185, "rations" :  185, "parts" :   0, "Time" : 1},
	"4-2" : {"manpower" :    0, "ammo" :    0, "rations" :    0, "parts" : 210, "Time" : 2},
	"4-3" : {"manpower" :  850, "ammo" :  550, "rations" :    0, "parts" :   0, "Time" : 6},
	"4-4" : {"manpower" :  400, "ammo" :  400, "rations" :  400, "parts" : 150, "Time" : 8},
	"5-1" : {"manpower" :    0, "ammo" :    0, "rations" :  100, "parts" :  45, "Time" : 0.5},
	"5-2" : {"manpower" :    0, "ammo" :  600, "rations" :  300, "parts" :   0, "Time" : 2.5},
	"5-3" : {"manpower" :  800, "ammo" :  400, "rations" :  400, "parts" :   0, "Time" : 4},
	"5-4" : {"manpower" :  100, "ammo" :    0, "rations" :    0, "parts" : 700, "Time" : 7},
	"6-1" : {"manpower" :  300, "ammo" :  300, "rations" :    0, "parts" : 100, "Time" : 2},
	"6-2" : {"manpower" :    0, "ammo" :  200, "rations" :  550, "parts" : 100, "Time" : 3},
	"6-3" : {"manpower" :    0, "ammo" :    0, "rations" :  200, "parts" : 500, "Time" : 5},
	"6-4" : {"manpower" :  800, "ammo" :  800, "rations" :  800, "parts" :   0, "Time" : 12},
	"7-1" : {"manpower" :  650, "ammo" :    0, "rations" :  650, "parts" :   0, "Time" : 2.5},
	"7-2" : {"manpower" :    0, "ammo" :  650, "rations" :    0, "parts" : 300, "Time" : 4},
	"7-3" : {"manpower" :  900, "ammo" :  600, "rations" :  600, "parts" :   0, "Time" : 5.5}, 
	"7-4" : {"manpower" :  250, "ammo" :  250, "rations" :  250, "parts" : 600, "Time" : 8},
	"8-1" : {"manpower" :  150, "ammo" :  150, "rations" :  150, "parts" :   0, "Time" : 1},
	"8-2" : {"manpower" :    0, "ammo" :    0, "rations" :    0, "parts" : 450, "Time" : 3},
	"8-3" : {"manpower" :  400, "ammo" :  800, "rations" :  400, "parts" :   0, "Time" : 6},
	"8-4" : {"manpower" : 1500, "ammo" :  400, "rations" :  400, "parts" : 100, "Time" : 9},
	"9-1" : {"manpower" : 0, "ammo" : 0, "rations" : 100, "parts" : 50, "Time" : 0.5},
	"9-2" : {"manpower" : 180, "ammo" : 0, "rations" : 180, "parts" : 100, "Time" : 1.5},
	"9-3" : {"manpower" : 750, "ammo" : 750, "rations" : 0, "parts" : 0, "Time" : 4.5},
	"9-4" : {"manpower" : 500, "ammo" : 600, "rations" : 900, "parts" : 0, "Time" : 7}
}

#Logistics missions to be added
"""

"10-1" : {"manpower" : 140, "ammo" : 200, "rations" : 0, "parts" : 0, "Time" : 2/3}
"10-2" : {"manpower" : 0, "ammo" : 240, "rations" : 180, "parts" : 0, "Time" : 1 + 2/3}
"10-3" : {"manpower" : 0, "ammo" : 480, "rations" : 480, "parts" : 300, "Time" : 5 + 1/3}
"10-4" : {"manpower" : 660, "ammo" : 660, "rations" : 660, "parts" : 330, "Time" : 10}
"11-1" : {"manpower" : 350, "ammo" : 1050, "rations" : 0, "parts" : 0, "Time" : 4}
"11-2" : {"manpower" : 360, "ammo" : 540, "rations" : 540, "parts" : 0, "Time" : 4}
"11-3" : {"manpower" : 0, "ammo" : 750, "rations" : 1500, "parts" : 250, "Time" : 8}
"11-4" : {"manpower" : 0, "ammo" : 1650, "rations" : 0, "parts" : 900, "Time" : 10}
"""

"""
Assumes the following # of battles per map:
4-3E: 4 battles,
5-4: 5 battles
5-2E: 5 battles,
0-2: 5 battles 
"""
expPerPopularLevelingMap = { "4-3E" : 1480, "5-4" : 1900, "5-2E" : 2050, "0-2" : 2450}

"""
Assumes the following # of battles per map:
4-3E: 4 battles,
5-4: 5 battles
5-2E: 5 battles,
0-2: 5 battles 
"""
expPerPopularLevelingMap = { "4-3E" : 1480, "5-4" : 1900, "5-2E" : 2050, "0-2" : 2450}

# Classes 
class Girls:
	def __init__(self, girls={}):
		self.girls = girls

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

	def listGirls(self, gunTypes):
		for girl in self.girls:
			if (self.getGunType(girl) in gunTypes):
				currentLevel = self.getCurrentLevel(girl)
				currentExp = self.getCurrentExp(girl)
				currentTime = self.getCurrentTime(girl)
				print(girl + " (" + self.getGunType(girl) + ")")
				print("Level " + str(currentLevel), end = " ")
				print("(Exp To Next Level: " + str(self.getExpToNextLevel(girl)) + ")")
				print("Last updated: " + str(currentTime))
				newLine()		

	def listAllGirls(self):
		if (len(self.girls) == 0): 
			print("You currently have no girls :(")
			newLine()
		else:
			print("Here's the list of your girls: ")
			for girl in self.girls:
				print(girl + " (" + self.getGunType(girl) + ")")
				currentLevel = self.getCurrentLevel(girl)
				currentExp = self.getCurrentExp(girl)
				currentTime = self.getCurrentTime(girl)
				print("Level " + str(currentLevel), end = " ")
				print("(Exp To Next Level: " + str(self.getExpToNextLevel(girl)) + ")")
				print("Last updated: " + str(currentTime))
				newLine()
		
class Girl:
	def __init__(self, gunType, level, exp):
		self.gunType = gunType
		self.levels = [level]
		self.exps = [exp]
		self.times = [datetime.datetime.now()]
		self.isTracking = False

	def getGunType(self): return self.gunType

	def getCurrentLevel(self):
		return self.levels[-1]

	def getCurrentExp(self):
		return self.exps[-1]

	def getCurrentTime(self):
		return self.times[-1]

	def isTracking(self):
		return self.isTracking

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

def getResource(mission, resourceTypes):
	sum = 0
	for resourceType in resourceTypes:
		if resourceType.lower() in {"m", "manpower"}: sum += mission["manpower"]
		elif resourceType.lower() in {"a", "ammo"}: sum += mission["ammo"]
		elif resourceType.lower() in {"r", "rations"}: sum += mission["rations"]
		elif resourceType.lower() in {"p", "parts"}: sum += mission["parts"]
		
	return sum

def logisticHelpScreen():
	print("Logistics Help Page")
	print("------------------------------------------------------")
	print("m or manpower: Optimize for manpower")
	print("a or ammo: Optimize for ammo")
	print("r or rations: Optimize for rations")
	print("p or parts: Optimize for parts")
	print("all: Optimize for all resources")
	print("q or quit: Goes back to dashboard page")
	print("h or help: Shows this screen")
	print("------------------------------------------------------")

possibleResourceTypeChoices = {"m", "a", "r", "p", "manpower", "ammo",
							   "rations", "parts", "all"}		
							   
def logisticsScreen(args):
	print("You are on the Logistics Page")
	print("------------------------------------------------------------------")
	
	resourceTypes = None
	timeLimit = None
	for arg in args:
		argument = arg.split("=")[0]
		if (argument == "r"): resourceTypes = [x.strip() for x in arg.split("=")[1].split(",")]
		elif (argument == "t"): timeLimit = int(arg.split("=")[1])

	# Currently only prints the first 4
	allResourcesMissions = []
	for missionName in logisticsMissions:
		mission = logisticsMissions[missionName]
		timeHours = mission["Time"]
		
		if timeLimit == None: #Get max resources/hr
			allResourcesPerHour = getResource(mission, resourceTypes) / timeHours
			allResourcesMissions.append((missionName, allResourcesPerHour, timeHours))
		elif timeHours <= timeLimit:
			allResources = getResource(mission, resourceTypes)
			allResourcesMissions.append((missionName, allResources, timeHours))

	itemsToPrint = 4
	allResourcesMissions.sort(key = lambda x: x[1], reverse = True)
	newLine()
	print("Top " + str(itemsToPrint) + " Missions " + "(" + ",".join(resourceTypes) + ")")
	print("-------------------------")
	for logisticMission in allResourcesMissions[:itemsToPrint]:
		hrsRounded = round(logisticMission[2], 2)
		print(logisticMission[0] + ": " + str(round(logisticMission[1], 2)) + " (" + str(hrsRounded) + " hours)")
	newLine()

def listGirls(girls, selection):
	arguments = selection.split("-")[1:]
	if len(arguments) == 0: girls.listAllGirls()
	
	#Find type argument TODO: document this in a////??? help section
	for arg in arguments:
		if ('type' in arg or 't' in arg):
			gunTypes = arg.split("=")[1].split(",")
			girls.listGirls(gunTypes)

def helpScreen():
	print("Dashboard Help Page")
	print("------------------------------------------------------")
	print("d or delete: Removes a girl")
	print("c or clear: Clears all of your girls. Use with caution")
	print("a or add: Adds a new girl to your list")
	print("u or update: Updates an existing girl")
	print("ls or list: Prints out all of the girls that you have")
	print("q or quit: Quits the application")
	print("h or help: Shows this screen")
	print("l or logistics: " "Takes you to logistics page")
	print("------------------------------------------------------")
	newLine()

def dashboardPage(girls):
	print("You are on the Home Page")
	print("------------------------------------------------------")
	selection = userResponse("What would you like to do? (help for list of commands):")
	newLine()

	command = selection.split("-")[0].strip()
	arguments = set(selection.split("-")[1:])
	if (command in {"q", "quit"}):
		return
	elif (command in {"d", "delete"}):
		deleteGirl(girls)
	elif (command in {"u", "update"}):
		updateGirl(girls)
	elif (command in {"c", "clear"}): 
		yeetGirls(girls)
		newLine()
	elif (command in {"ls", "list"}): listGirls(girls, selection)
	elif (command in {"a", "add"}): girls.addGirlToHaremWithConsent()
	elif (command in {"l", "logistics"}): logisticsScreen(arguments)
	elif (command in {"h", "help"}): helpScreen()
	else: 
		print("Do you think I got time to support your girls??")
		newLine()

	dashboardPage(girls)

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

	print("--------------------------")
	print("Welcome to GFL Dashboard!")
	print("---------------------------")
	newLine()
	filePath = getSaveFilePath(fileName)
	girls = readGirlsIn(filePath)
	dashboardPage(girls)
	updateGirlsDatabase(filePath, girls)
	print("Have a nice day!")

if __name__ == "__main__":
	main()
