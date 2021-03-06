# quest ordering is mainly based off release date. the information was taken from
# http://runescape.wikia.com/wiki/List_of_quest_release_dates
# quests are owned by Jagex

''' 0: number
	1: name
	2: skill req
	3: skill rec
	4: quest req
	5: quest rec
'''

quests = []

#this is an empty entry so that the indexing can start at 1 instead of 0
quests.append([0,'',{},{},[],[]])

quests.append([1,"Cook's Assistant",{},{},[],[]])
quests.append([2,'Demon Slayer',{},{},[],[]])
quests.append([3,'The Restless Ghost',{},{},[],[]])
quests.append([4,"Gunnar's Ground",{'CRAFTING':5},{},[],[]]) #used to be Romeo and Juliet

#note: this quest was released in between quest 166 and 167, but the indexing
#(at least on rs wiki) got messed up because sheep shearer and witch's potion
#became miniquests. because of that, i'm going to put these first two quests in
#the index where these discontinued quests would have gone, but this is
#arbitrary and is just to make sure the numbers turn out okay
# quests.append([5,'Discontinued: Sheep Shearer',{},{},[],[]])#now a miniquest
quests.append([5,'Quiet Before the Swarm',{'ATTACK':35,'STRENGTH':42},{},[9,88],[]])

quests.append([6,'Shield of Arrav',{},{},[],[]])
quests.append([7,'Ernest the Chicken',{},{},[],[]])
quests.append([8,'Vampyre Slayer',{},{},[],[]])
quests.append([9,'Imp Catcher',{},{},[],[]])
quests.append([10,'Stolen Hearts',{},{},[],[]])
quests.append([11,"What's Mine is Yours",{'SMITHING':5},{},[],[]])
quests.append([12,'The Death of Chivalry',{},{},[],[]])

#note: this quest was released in between quest 166 and 167, but the indexing
#(at least on rs wiki) got messed up because sheep shearer and witch's potion
#became miniquests. because of that, i'm going to put these first two quests in
#the index where these discontinued quests would have gone, but this is
#arbitrary and is just to make sure the numbers turn out okay
# quests.append([13,'Discontinued: Witch's Potion',{},{},[],[]])#now a miniquest
quests.append([13,'Love Story',{'MAGIC':77,'CONSTRUCTION':68,'SMITHING':68,'CRAFTING':67},{},[104,100],[]])

quests.append([14,"The Knight's Sword",{'MINING':10},{},[],[]])
quests.append([15,'Goblin Diplomacy',{},{},[],[]])
quests.append([16,"Pirate's Treasure",{},{},[],[]])
quests.append([17,'Dragon Slayer',{'QUEST POINTS':33},{'MAGIC':33,'PRAYER':43},[],[]])
quests.append([18,'Druidic Ritual',{},{},[],[]])
quests.append([19,'Lost City',{'CRAFTING':31,'WOODCUTTING':36},{},[],[]])
quests.append([20,"Witch's House",{},{},[],[]])
quests.append([21,"Merlin's Crystal",{},{},[],[]])
quests.append([22,"Heroes' Quest",{'COOKING':53,'FISHING':53,'HERBLORE':25,'MINING':50,'DEFENCE':25,
	'QUEST POINTS':56},{},[6,19,17,21,18],[]])
quests.append([23,'Scorpion Catcher',{'PRAYER':31},{},[],[]])
quests.append([24,'Family Crest',{'CRAFTING':40,'SMITHING':40,'MINING':40,'MAGIC':59},{},[],[]])
quests.append([25,'Tribal Totem',{'THIEVING':21},{},[],[]])
quests.append([26,'Fishing Contest',{'FISHING':10},{},[],[]])
quests.append([27,"Monk's Friend",{},{},[],[]])
quests.append([28,'Temple of Ikov',{'THIEVING':42,'RANGED':40},{},[],[]])
quests.append([29,'Clock Tower',{},{},[],[]])
quests.append([30,'Holy Grail',{'ATTACK':30},{},[21],[]])
quests.append([31,'Tree Gnome Village',{},{},[],[]])
quests.append([32,'Fight Arena',{},{},[],[]])
quests.append([33,'Hazeel Cult',{},{},[],[]])
quests.append([34,'Sheep Herder',{},{},[],[]])
quests.append([35,'Plague City',{},{},[],[]])
quests.append([36,'Sea Slug',{'FIREMAKING':30},{},[],[]])
quests.append([37,'Waterfall Quest',{},{},[],[]])
quests.append([38,'Biohazard',{},{},[35],[]])
quests.append([39,'Jungle Potion',{'HERBLORE':3},{},[18],[]])
quests.append([40,'The Grand Tree',{},{},[],[31]])
quests.append([41,'Shilo Village',{'CRAFTING':20,'AGILITY':32},{'PRAYER':43},[39],[]])
quests.append([42,'Underground Pass',{'RANGED':25},{'MAGIC':34,'AGILITY':50,'PRAYER':43,'THIEVING':50},[38],[]])
quests.append([43,'Observatory Quest',{},{},[],[]])
quests.append([44,'The Tourist Trap',{'FLETCHING':10,'SMITHING':20},{},[],[]])
quests.append([45,'Watchtower',{'HERBLORE':14,'MAGIC':14,'TTHIEVING':15,'AGILITY':25,'MINING':40},{},[],[]])
quests.append([46,'Dwarf Cannon',{},{},[],[]])
quests.append([47,'Murder Mystery',{},{},[],[]])
quests.append([48,'The Dig Site',{'THIEVING':25,'AGILITY':10,'HERBLORE':10},{},[],[]])
quests.append([49,"Gertrude's Cat",{},{},[],[]])
quests.append([50,"Legends' Quest",{'AGILITY':50,'CRAFTING':50,'HERBLORE':45,'MINING':52,'PRAYER':42,
	'SMITHING':50,'STRENGTH':50,'THIEVING':50,'WOODCUTTING':50,'QUEST POINTS':108},{'PRAYER':43},[24,22,41,42,37],[]])
quests.append([51,'Rune Mysteries',{},{},[],[]])
quests.append([52,'Big Chompy Bird Hunting',{'COOKING':30,'RANGED':30,'FLETCHING':5},{},[],[]])
quests.append([53,'Elemental Workshop I',{'MINING':20,'SMITHING':20,'CRAFTING':20},{},[],[]])
quests.append([54,'Priest in Peril',{},{},[],[]])
quests.append([55,'Nature Spirit',{},{'CRAFTING':18,'PRAYER':10},[3,54],[]])
quests.append([56,'Death Plateau',{},{},[],[]])
quests.append([57,'Troll Stronghold',{'AGILITY':15,'THIEVING':30},{},[56],[]])
quests.append([58,'Tai Bwo Wannai Trio',{'AGILITY':15,'FISHING':5,'COOKING':30},{},[39],[]])
quests.append([59,'Regicide',{'AGILITY':56,'CRAFTING':10},{},[42],[]])
quests.append([60,"Eadgar's Ruse",{'HERBLORE':31,'AGILITY':15},{},[57,18],[]])
quests.append([61,"Shades of Mort'ton",{'CRAFTING':20,'FIREMAKING':5,'HERBLORE':15},{},[],[]])
quests.append([62,'The Fremennik Trials',{'CRAFTING':40,'FLETCHING':25,'WOODCUTTING':40},{},[],[]])
quests.append([63,'Horror from the Deep',{'AGILITY':35},{'PRAYER':43,'CONSTITUTION':50},[],[]])
quests.append([64,'Throne of Miscellania',{'HERBLORE':35,'FARMING':10,'WOODCUTTING':45,'FISHING':40,'MINING':30},{},[22,62],[]])
quests.append([65,'Monkey Madness',{},{'PRAYER':43,'THIEVING':10},[40,31],[]])
quests.append([66,'Haunted Mine',{'CRAFTING':35},{'AGILITY':15},[54,55],[]])#need to double check that priest in peril is required
quests.append([67,'Troll Romance',{'AGILITY':28},{'MAGIC':61,'PRAYER':43},[57],[]])
quests.append([68,'In Search of the Myreque',{'AGILITY':25},{},[55],[]])
quests.append([69,'Creature of Fenkenstrain',{'CRAFTING':20,'THIEVING':25},{'SMITHING':20},[],[]])
quests.append([70,'Roving Elves',{},{},[37,59],[]])
quests.append([71,'Ghosts Ahoy',{'AGILITY':25,'COOKING':20},{},[54,3],[]])
quests.append([72,'One Small Favour',{'HERBLORE':18,'CRAFTING':25,'SMITHING':30,'AGILITY':36},{},[51,41],[]])
quests.append([73,'Mountain Daughter',{'AGILITY':20},{},[],[]])
quests.append([74,'Between a Rock...',{'DEFENCE':30,'MINING':40,'SMITHING':50},{},[46,26],[]])
quests.append([75,'The Feud',{'THIEVING':30},{},[],[]])
quests.append([76,'The Golem',{'CRAFTING':20,'THIEVING':25},{},[],[]])
quests.append([77,'Desert Treasure',{'SLAYER':10,'FIREMAKING':50,'MAGIC':50,'THIEVING':53,'MINING':50},{'AGILITY':47},[48,44,28,54,57,37],[]])
quests.append([78,"Icthlarin's Little Helper",{},{},[3,49,185],[]])
quests.append([79,'Tears of Guthix',{'FIREMAKING':49,'MINING':20,'CRAFTING':20,'QUEST POINTS':44},{'SMITHING':49,'CRAFTING':49},[],[]])
quests.append([80,'Zogre Flesh Eaters',{'SMITHING':4,'HERBLORE':8,'STRENGTH':20,'RANGED':30},{'FLETCHING':30},[39,52],[]])
quests.append([81,'The Lost Tribe',{'AGILITY':13,'MINING':17,'THIEVING':13},{},[15],[]])
quests.append([82,'The Giant Dwarf',{'CRAFTING':12,'FIREMAKING':16,'MAGIC':33,'THIEVING':14},{},[],[]])
quests.append([83,'Recruitment Drive',{},{},[18],[]])
quests.append([84,"Mourning's Ends Part I",{'RANGED':60,'THIEVING':50},{},[52,34,70],[]])
quests.append([85,'Forgettable Tale of a Drunken Dwarf	',{'COOKING':22,'FARMING':17},{},[82,26],[]])
quests.append([86,'Garden of Tranquillity',{'FARMING':25},{},[69],[]])
quests.append([87,'A Tail of Two Cats',{},{},[78],[]])
quests.append([88,'Wanted!',{'QUEST POINTS':33},{},[54,81,83],[71]])
quests.append([89,"Mourning's Ends Part II",{},{'PRAYER':43,'AGILITY':60},[84],[]])
quests.append([90,'Rum Deal',{'FARMING':40,'CRAFTING':42,'PRAYER':47,'FISHING':50,'SLAYER':42},{},[54,80],[]])
quests.append([91,'Shadow of the Storm',{'CRAFTING':30},{},[2,76],[]])
quests.append([92,'Making History',{},{'CRAFTING':24,'SMITHING':40,'MINING':40},[3,54],[]])#not sure about priest in peril
quests.append([93,'Ratcatchers',{},{'HERBLORE':54},[78],[]])
quests.append([94,'Spirits of the Elid',{'MAGIC':33,'RANGED':37,'MINING':37,'THIEVING':37},{},[],[]])
quests.append([95,'Devious Minds',{'SMITHING':65,'RUNECRAFTING':50,'FLETCHING':50},{},[88,11,57],[]])
quests.append([96,'The Hand in the Sand',{'THIEVING':17,'CRAFTING':49},{},[],[]])
quests.append([97,"Enakhra's Lament",{'CRAFTING':50,'FIREMAKING':45,'MAGIC':13},{'MINING':45},[],[]])#wiki for details on skills
quests.append([98,'Cabin Fever',{'AGILITY':42,'CRAFTING':45,'SMITHING':50,'RANGED':40},{},[16,90],[]])
quests.append([99,'Fairy Tale I - Growing Pains',{},{},[19,55],[39]])
quests.append([100,'Recipe for Disaster',{'COOKING':70,'MAGIC':59,'THIEVING':53,'FISHING':53,'MINING':52,
	'CRAFTING':50,'FIREMAKING':50,'WOODCUTTING':50,'AGILITY':50,'RANGED':40,'HERBLORE':45,'FLETCHING':10,
	'SLAYER':10,'SMITHING':40,'QUEST POINTS':176},{},[1,15,26,49,91,52,38,2,47,55,20,19,50,65,77,63],[]])#dont know how to deal with this one
# quests.append([101,'In Aid of the Myreque',{},{},[],[]])
# quests.append([102,"A Soul's Bane",{},{},[],[]])
# quests.append([103,'Rag and Bone Man',{},{},[],[]])
# quests.append([104,'Swan Song',{},{},[],[]])
# quests.append([105,'Royal Trouble',{},{},[],[]])
quests.append([106,'Death to the Dorgeshuun',{'THIEVING':23,'AGILITY':23},{'COMBAT':80},[81],[]])
# quests.append([107,'A Fairy Tale Part II',{},{},[],[]])
# quests.append([108,'Lunar Diplomacy',{},{},[],[]])
# quests.append([109,'The Eyes of Glouphrie',{},{},[],[]])
# quests.append([110,'Darkness of Hallowvale',{},{},[],[]])
quests.append([111,'The Slug Menace',{'CRAFTING':30,'RUNECRAFTING':30,'SLAYER':30,'THIEVING':30},{},[36,88],[]])
# quests.append([112,'Elemental Workshop II',{},{},[],[]])
# quests.append([113,"My Arm's Big Adventure",{},{},[],[]])
# quests.append([114,'Enlightened Journey',{},{},[],[]])
# quests.append([115,"Eagles' Peak",{},{},[],[]])
# quests.append([116,'Animal Magnetism',{},{},[],[]])
# quests.append([117,'Contact!',{},{},[],[]])
# quests.append([118,'Cold War',{},{},[],[]])
# quests.append([119,'The Fremennik Isles',{},{},[],[]])
# quests.append([120,'Tower of Life',{},{},[],[]])
quests.append([121,'The Great Brain Robbery',{'CRAFTING':16,'CONSTRUCTION':30,'PRAYER':50},{},[69,100,98],[]])
# quests.append([122,'What Lies Below',{},{},[],[]])
# quests.append([123,"Olaf's Quest",{},{},[],[]])
quests.append([124,'Another Slice of H.A.M.',{'ATTACK':15,'PRAYER':25},{},[48,82,106],[]])
# quests.append([125,'Dream Mentor',{},{},[],[]])
# quests.append([126,'Grim Tales',{},{},[],[]])
# quests.append([127,"King's Ransom",{},{},[],[]])
# quests.append([128,'The Path of Glouphrie',{},{},[],[]])
# quests.append([129,'Back to my Roots',{},{},[],[]])
quests.append([130,'Land of the Goblins',{'PRAYER':30,'AGILITY':36,'FISHING':36,'THIEVING':36,'HERBLORE':37},{},[124,26],[]])
# quests.append([131,'Dealing with Scabaras',{},{},[],[]])
# quests.append([132,'Wolf Whistle',{},{},[],[]])
# quests.append([133,'As a First Resort',{},{},[],[]])
# quests.append([134,'Catapult Construction',{},{},[],[]])
# quests.append([135,"Kennith's Concerns",{},{},[],[]])
# quests.append([136,'Legacy of Seergaze',{},{},[],[]])
# quests.append([137,'Perils of Ice Mountain',{},{},[],[]])
# quests.append([138,'TokTz-Ket-Dill',{},{},[],[]])
# quests.append([139,'Smoking Kills',{},{},[],[]])
quests.append([140,'Rocking Out',{'AGILITY':60,'THIEVING':63,'CRAFTING':66,'SMITHING':69},{},[121],[]])
# quests.append([141,'Spirit of Summer',{},{},[],[]])
# quests.append([142,'Meeting History',{},{},[],[]])
# quests.append([143,'All Fired Up',{},{},[],[]])
# quests.append([144,"Summer's End",{},{},[],[]])
# quests.append([145,'Defender of Varrock',{},{},[],[]])
# quests.append([146,'Swept Away',{},{},[],[]])
# quests.append([147,'While Guthix Sleeps',{},{},[],[]])#
# quests.append([148,'Myths of the White Lands',{},{},[],[]])
# quests.append([149,'In Pyre Need',{},{},[],[]])
quests.append([150,'The Chosen Commander',{'AGILITY':46,'STRENGTH':46,'THIEVING':46},{},[130],[]])
# quests.append([151,'Glorious Memories',{},{},[],[]])
# quests.append([152,'The Tale of the Muspah',{},{},[],[]])
# quests.append([153,'Missing My Mummy',{},{},[],[]])
# quests.append([154,'Hunt for Red Raktuber',{},{},[],[]])
# quests.append([155,'The Curse of Arrav',{},{},[],[]])
# quests.append([156,"Fur 'n' Seek",{},{},[],[]])
# quests.append([157,'Forgiveness of a Chaos Dwarf	',{},{},[],[]])
# quests.append([158,'Within the Light',{},{},[],[]])
# quests.append([159,'The Temple at Senntisten',{},{},[],[]])#
# quests.append([160,'Blood Runs Deep',{},{},[],[]])
# quests.append([161,"Nomad's Requiem",{},{},[],[]])
# quests.append([162,'Rune Mechanics',{},{},[],[]])
# quests.append([163,'The Blood Pact',{},{},[],[]])
# quests.append([164,'Buyers and Cellars',{},{},[],[]])
# quests.append([165,'Fairy Tale III - Orks Rift',{},{},[],[]])#
# quests.append([166,'Elemental Workshop III',{},{},[],[]])
# quests.append([167,'A Void Dance',{},{},[],[]])#see entries 5 and 13
# quests.append([168,'The Void Stares Back',{},{},[],[]])#see entires 5 and 13
# quests.append([169,'Do No Evil',{},{},[],[]])
# quests.append([170,'King of the Dwarves',{},{},[],[]])
# quests.append([171,'The Prisoner of Glouphrie',{},{},[],[]])
# quests.append([172,'Elemental Workshop IV',{},{},[],[]])
# quests.append([173,'A Clockwork Syringe',{},{},[],[]])
# quests.append([174,'Deadliest Catch',{},{},[],[]])
# quests.append([175,'Salt in the Wound',{},{},[],[]])
# quests.append([176,'The Branches of Darkmeyer',{},{},[],[]])
quests.append([177,'Ritual of the Mahjarrat',{'CRAFTING':76,'AGILITY':77,'MINING':76},{},[147,159,87,111,140,33,32,165,97],[]])
# quests.append([178,'One Piercing Note',{},{},[],[]])
# quests.append([179,"The Firemaker's Curse",{},{},[],[]])#
# quests.append([180,'Let Them Eat Pie',{},{},[],[]])
# quests.append([181,'The Elder Kiln',{},{},[],[]])
# quests.append([182,'Song from the Depths',{},{},[],[]])
# quests.append([183,'Carnillean Rising',{},{},[],[]])
# quests.append([184,'Some Like it Cold',{},{},[],[]])
quests.append([185,'Diamond in the Rough',{},{},[10],[]])#isn't this just a remake??
# quests.append([186,'Rune Memories',{},{},[],[]])
# quests.append([187,'The Brink of Extinction',{},{},[],[]])
# quests.append([188,'The World Wakes',{},{},[],[]])#
# quests.append([189,'Bringing Home the Bacon',{},{},[],[]])
# quests.append([190,'Birthright of the Dwarves',{},{},[],[]])
quests.append([191,'Missing, Presumed Death',{},{},[],[188,150]])
# quests.append([192,'One of a Kind',{},{},[],[]])
quests.append([193,'Fate of the Gods',{'SUMMONING':67,'AGILITY':73,'DIVINATION':75,'SLAYER':76,'MAGIC':79},{},[191],[188,179,177]])
# quests.append([194,'A Shadow over Ashdale',{},{},[],[]])
# quests.append([195,'The Mighty Fall',{},{},[],[]])
# quests.append([196,"Plague's End",{},{},[],[]])
# quests.append([197,'Broken Home',{},{},[],[]])
# quests.append([198,'Heart of Stone',{},{},[],[]])
# quests.append([199,'Dishonour among Thieves',{},{},[],[]])
# quests.append([200,'Dimension of Disaster',{},{},[],[]])
# quests.append([201,"Hero's Welcome",{},{},[],[]])
# quests.append([202,'The Light Within',{},{},[],[]])
# quests.append([203,'The Lord of Vampyrium',{},{},[],[]])
# quests.append([204,'Call of the Ancestors',{},{},[],[]])
# quests.append([205,'Beneath Cursed Tides',{},{},[],[]])
# quests.append([206,'',{},{},[],[]])

# quests.append([0,'',{},{},[],[]])
