#Big-Quest-Series Quest Planner
#Started by Qazlal August 2015.

# import numpy as np
# import quest_data as data #so far don't need this
import quest_tools as tools

InputQuest = int('100')

# print ""
print "This is the quest " + tools.Quest_Name(InputQuest)
print ""

outputRequirements = tools.Get_Req(InputQuest)
tools.Display_QuestList(outputRequirements)
print ""
tools.Display_SkillList(outputRequirements)

print ""
