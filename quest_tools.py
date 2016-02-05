import quest_data as data
import itertools
import math

def Get_Req(nQuest,bSRec=True,bQRec=True):
	#load skills from input quest
	SReq=data.quests[nQuest][2] #this is a dictionary
	if bSRec: SReq = Combine_SReq(SReq,data.quests[nQuest][3])

	#load quest req's from input quest
	QReq=data.quests[nQuest][4]
	if bQRec: QReq.extend(data.quests[nQuest][5])

	#QReq_final is a set of all quests required, that this func. will fill
	QReq_final = set()

	#TO DO: investigate if using sets instead of lists would benefit this function
	#loop through quest requirements until they're all gone
	while QReq:
		for q in QReq:
			# print data.quests[q][1] #name of the quest it's looking at

			#take the skill req's of the quest and add to the total skill req's
			SReq = Combine_SReq(SReq,data.quests[q][2])
			if bSRec: SReq = Combine_SReq(SReq,data.quests[q][3])

			#add any prereq quests from THIS quest to the list to check
			QReq.extend(data.quests[q][4])
			if bQRec: QReq.extend(data.quests[q][5])

			#add this quest to a list of all quest requirements
			QReq_final.add(q)#reminder that this is a set datatype

			#remove this quest from the list now that we're done
			QReq[:] = (value for value in QReq if value != q) #removes all instances of q from list
	return [SReq,QReq_final]

#this is mostly an internal function for Get_Req
def Combine_SReq(d1,d2):
	d3 = {}
	for key in d1:
		if key in d2:
			d3[key]=max(d1[key],d2[key])
		else:
			d3[key]=d1[key]
	for key in d2:
		if key in d1:
			d3[key]=max(d1[key],d2[key])
		else:
			d3[key]=d2[key]
	return d3

#get the name of a quest from its index
def Quest_Name(nQuest):
	return data.quests[nQuest][1]

#prints a list in a multi-column format
def Column_PrintList(lRaw,nColumn=4,spacing=25):
	toZip = []

	#for across then down order
	# for i in range(nColumn):
		# toZip.append(lRaw[i::nColumn])

	#for down then across order
	#ciel rounds up; need to convert to float first though or it'll truncate
	nRow = int(math.ceil(len(lRaw)/float(nColumn))) #needs to be int for slicing
	for i in range(nColumn):
		toZip.append(lRaw[i*nRow:(i+1)*nRow])

	#generate a format string for however many columns
	#makes something like: '{:<20}{:<20}{:<}'
	formatString=''
	for i in range(nColumn-1):
		formatString = formatString + '{:<'+str(spacing)+'}'
	formatString = formatString + '{:<}'

	#the asterix "unpacks" the list of lists
	for abc in itertools.izip_longest(*toZip):
		abc = [x if x else "" for x in abc] #replaces None with empty string
		print formatString.format(*abc)

#prints a set datatype of quests in a pretty way
def Display_QuestList(toPrint):
	listPrint = list(toPrint[1]) #get a list version of the set of quests
	listPrint.sort() #sort it numerically
	#my simple way:
	# for quest in listPrint:
	# 	print data.quests[quest][1] #print the name of each quest
	#adapted from stackechange:
	listFinal = []
	for q in listPrint:
		listFinal.append(data.quests[q][1])
	print("Quest Requirements:")
	Column_PrintList(listFinal)

#prints a dictionary datatype of skills requirements in a pretty way
def Display_SkillList(toPrint):
	print("Skill Requirements:")
	for skill in toPrint[0]:
		#string.title() makes all lowercase besides first letter of words
		print skill.title() + " " + str(toPrint[0][skill])

#UNTESTED; pseudocode. Quest data not functional at the moment.
# def lFindNotCompleted(nQuest):
	#find all quests with nQuest as requirement
		#put each of those in lists lIncomplete and lUnchecked
	#while lUnchecked is not empty
		#get one of the quests from lUnchecked
			#find all quests with THAT quest as requirement that aren't yet in lIncomplete
				#put each of those into lIncomplete and lUnchecked
			#remove the quest from lUnchecked
	#return lIncomplete
