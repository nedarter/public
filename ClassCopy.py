import os
import shutil
from datetime import date
import math

classStart = date(2021,6,15)
today = date.today()

daysBetween = today - classStart
weekNum = ("0" + str(math.floor(daysBetween.days / 7) + 1))[-2:]

rootDir = 'C:\\Users\\dpesa\\OneDrive\\Documents\\GitHub\\DataViz-Lesson-Plans\\01-Lesson-Plans'
targetDir = "C:\\Projects\\ClassFileCopy"

for i in os.listdir(rootDir):    
    if i[0:2] == weekNum:
        rootDir = rootDir + '\\' + i

print(rootDir)
for [current, dirList, fileList] in os.walk(rootDir):
    newDir = current.replace(rootDir, targetDir)

    if not os.path.exists(newDir):
        os.mkdir(newDir)

    for file in fileList: 
        shutil.copyfile(os.path.join(current,file), os.path.join(newDir,file))
        

    


