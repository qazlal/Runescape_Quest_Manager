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

# r is a string but i need a list >:(
#wrote my own parser. could be cleaner but it does the trick
lPlayer = []
lSkill = []
sEntry = ""
for character in sRaw:
	if character == "," or character == "\n":
		lSkill.append(sEntry)
		sEntry = ""
		if character == "\n":
			lPlayer.append(lSkill)
			lSkill = []
	else:
		sEntry = sEntry + character

print lPlayer #now formatted in a nice 2-D list!