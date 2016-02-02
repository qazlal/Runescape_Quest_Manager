#API documentation at http://services.runescape.com/m=rswiki/en/Hiscores_APIs
######example to access runescape API in python
import urllib2

player = "Qazlal"

sRaw=urllib2.urlopen("http://services.runescape.com/m=hiscore/index_lite.ws?player="+player).read()
######

# overall, Attack, Defence, Strength, Constitution, Ranged, Prayer,
# Magic, Cooking, Woodcutting, Fletching, Fishing, Firemaking, Crafting, Smithing,
# Mining, Herblore, Agility, Thieving, Slayer, Farming, Runecrafting, Hunter,
# Construction, Summoning, Dungeoneering, Divination.

#r is a string but i need a list >:(
#wrote my own parser. could be cleaner but it does the trick
lPlayer = []
lSkill = []
sEntry = ""
for character in sRaw:
	if character == "," or character == "\n":
		lSkill.append(int(sEntry))
		sEntry = ""
		if character == "\n":
			lPlayer.append(lSkill)
			lSkill = []
	else:
		sEntry = sEntry + character

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

#runescape constants. these will make later released skills easy to implement, including future elite skills
rMaxLevelXP = 13034431#xp for 99 on regular skills
eMaxLevelXP = 36073511 #xp for 99 for elite skills
rNumSkills = 26 #number of regular skills
eNumSkills = 1 #number of elite skills
nMaxcapeXP = rMaxLevelXP*rNumSkills + eMaxLevelXP*eNumSkills

print "\n"
#examples to get things from the list
print player
print "Overall: " + str(lPlayer[0][1])
print "Total xp: " + commaifier(lPlayer[0][2])
print "Invention: " + str(lPlayer[rNumSkills+eNumSkills][1])
print "\n"

#percent of total xp in 99's
nTotalXPTowardsMax = 0
for skill in range(1,28):
	if lPlayer[skill][1] >= 99:
		nTotalXPTowardsMax += rMaxLevelXP
	else:
		nTotalXPTowardsMax += lPlayer[skill][2]

print commaifier(nTotalXPTowardsMax)
print commaifier(nMaxcapeXP)

print str(round(100*float(nTotalXPTowardsMax)/float(nMaxcapeXP)))+"% until maxcape"
