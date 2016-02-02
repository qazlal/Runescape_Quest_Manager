import RS_Quest_Data as data

def Get_Req(nQuest,bSRec=True,bQRec=True):
	#load skills from input quest
	SReq=data.quests[nQuest][2]
	if bSRec: SReq = Combine_SReq(SReq,data.quests[nQuest][3])

	#load quest req's from input quest
	QReq=data.quests[nQuest][4]
	if bQRec: QReq.extend(data.quests[nQuest][5])

	#loop through quest requirements until they're all gone
	while QReq:
		for q in QReq:
			print data.quests[q][1] #name of the quest it's looking at

			#take the skill req's of the quest and add to the total skill req's
			SReq = Combine_SReq(SReq,data.quests[q][2])
			if bSRec: SReq = Combine_SReq(SReq,data.quests[q][3])

			#add any prereq quests from THIS quest to the list to check
			QReq.extend(data.quests[q][4])
			if bQRec: QReq.extend(data.quests[q][5])

			#remove this quest from the list now that we're done
			QReq[:] = (value for value in QReq if value != q) #removes all instances of q from list
	return SReq

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
