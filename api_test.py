#API documentation at http://services.runescape.com/m=rswiki/en/Hiscores_APIs
######
import urllib2
######

#runescape constants. these will make later released skills easy to implement, including future elite skills
rMaxLevelXP = 13034431#xp for 99 on regular skills
eMaxLevelXP = 36073511 #xp for 99 for elite skills
rNumSkills = 26 #number of regular skills
eNumSkills = 1 #number of elite skills
nMaxcapeXP = rMaxLevelXP*rNumSkills + eMaxLevelXP*eNumSkills

#these are ordered in the order of the runescape high scores API, for reference
lSkillIndices=['OVERALL','ATTACK','DEFENCE','STRENGTH','CONSTITUTION','RANGED',
	'PRAYER','MAGIC','COOKING','WOODCUTTING','FLETCHING','FISHING',
	'FIREMAKING','CRAFTING','SMITHING','MINING','HERBLORE','AGILITY',
	'THIEVING','SLAYER','FARMING','RUNECRAFTING','HUNTER','CONSTRUCTION',
	'SUMMONING','DUNGEONEERING','DIVINATION','INVENTION']

#runescape high scores API parser
def highScoresAPI(sUsername):
	sRaw=urllib2.urlopen("http://services.runescape.com/m=hiscore/index_lite.ws?player="+sUsername).read()
	lFinal = []
	lSkill = []
	sEntry = ""
	for character in sRaw:
		if character == "," or character == "\n":
			lSkill.append(int(sEntry))
			sEntry = ""
			if character == "\n":
				lFinal.append(lSkill)
				lSkill = []
		else:
			sEntry = sEntry + character
	return lFinal

#takes an integer and turns it into a string with commas every 3 digits
def commaifier(iInput):
	sInput = str(iInput)
	sOutput = ""
	iCounter = 0
	for character in range(len(sInput)-1,-1,-1):
		iCounter += 1
		if iCounter == 4:
			sOutput = "," + sOutput
			iCounter = 1
		sOutput = sInput[character] + sOutput
	return sOutput

#percent of total xp in 99's
def xpTowardsMax(inputPlayer):
	nTotalXPTowardsMax = 0
	for skill in range(1,rNumSkills+eNumSkills+1):
		if inputPlayer[skill][1] >= 99:
			nTotalXPTowardsMax += rMaxLevelXP
		else:
			nTotalXPTowardsMax += inputPlayer[skill][2]
	return nTotalXPTowardsMax

#####Examples and Tests#####
player = "Qazlal"
lPlayer = highScoresAPI(player)

#examples to get things from the list
print "\n"
print player
#the 0 is for total level, the 1 is for the level
print "Overall: " + str(lPlayer[0][1])
#the 0 is for total level, the 2 is for the xp
print "Total xp: " + commaifier(lPlayer[0][2])
#the 27 is for invention, the 1 is for the level
print "Invention: " + str(lPlayer[27][1])
print "\n"

print commaifier(xpTowardsMax(lPlayer))
print commaifier(nMaxcapeXP)

print str(round(100*float(xpTowardsMax(lPlayer))/float(nMaxcapeXP)))+"% until maxcape"
