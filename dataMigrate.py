#!env/bin/python
# -*- coding: UTF-8 -*-
import html2text
html2textCall = html2text.html2text
html2text.BYPASS_TABLES = True
import sys, re
from openpyxl import load_workbook
reload(sys)
sys.setdefaultencoding('utf8')

from app import db, models
from sqlalchemy.sql import exists

workbookInRAM = load_workbook('data/defaultData.xlsx')
worksheetInRAM = workbookInRAM.active


# Functions validateLists
# Validation of Name lists
def validateNameLists(strNameList):
    outputList = []
    inputList = re.split(',|;|/| and ',strNameList)
    # Removing email like <for.bar@example.com>
    for strName in inputList:
        strName = re.split('<',strName)[0]
        strName = re.split('\(',strName)[0]
        if strName.startswith(' '):
            strName = strName[1:]
        outputList.append(strName)
    return outputList

def validateKeyWordLists(strKeyWordList):
    outputList = []
    inputList = re.split(',|;|/|\s|\'',strKeyWordList)
    # Removing email like <for.bar@example.com>
    for strKeyWord in inputList:
        if strKeyWord.startswith(' '):
            strKeyWord = strKeyWord[1:]
        if len(strKeyWord) > 1:
            outputList.append(strKeyWord)
    return outputList

# Filter and Convert description from html to plain string here:
columnZ = []
for cell in worksheetInRAM['Z']:
    columnZ.append(html2textCall(cell.value))
#    columnZ.append(cell.value)
# filter names of Developer
columnU = []
for cell in worksheetInRAM['U']:
    if cell.value == None:
        columnU.append([])
    else:
        columnU.append(validateNameLists(cell.value))

# filter names of InnovatorName
columnF = []
for cell in worksheetInRAM['F']:
    if cell.value == None:
        columnF.append([])
    else :
        columnF.append(validateNameLists(cell.value))

# filter names of ToolName
columnE = []
for cell in worksheetInRAM['E']:
    if cell.value == None:
        columnE.append(None)
    else :
        columnE.append(cell.value)
# filter KeyWords
columnT = []
for cell in worksheetInRAM['T']:
    if cell.value == None:
        columnT.append([])
    else :
        columnT.append(validateKeyWordLists(cell.value))
# filter ToolUrlOnLightHouse
columnAA = []
for cell in worksheetInRAM['AA']:
    if cell.value == None:
        columnAA.append(None)
    else :
        columnAA.append(cell.value)
# filter Rates
columnAB = []
for cell in worksheetInRAM['AB']:
    if cell.value == None:
        columnAB.append(None)
    else :
        columnAB.append(cell.value)
# filter DownloadTimes
columnP = []
for cell in worksheetInRAM['P']:
    columnP.append(cell.value)
# filter ServiceArea
columnD = []
for cell in worksheetInRAM['D']:
    if cell.value == None:
        columnD.append(None)
    else :
        columnD.append(cell.value)
# filter ImplementedDate
columnI = []
for cell in worksheetInRAM['I']:
    if cell.value == None:
        columnI.append(None)
    else :
        columnI.append(cell.value.split(".")[0])

# Validated data

data_Developer = columnU
data_InnovatorName = columnF
data_Description = columnZ
data_ToolName = columnE
data_KeyWords = columnT
data_ToolUrlOnLightHouse = columnAA
data_Rates = columnAB
data_DownloadTimes = columnP
data_ServiceArea = columnD
data_ImplementedDate = columnI


# Function exists

def existsInDB_GotID(className, objectName):
    internal_name = className.NameString
#   test with: print className.query.filter(internal_name == objectName).first().id
    if db.session.query(exists().where(internal_name == objectName)).scalar():
        return className.query.filter(internal_name == objectName).first().id
    else:
        return False  


for toolIndex in range(1, len(data_ToolName)):
    thisTool = models.Tool(
        ServiceArea  = data_ServiceArea[toolIndex] , 
        NameString  = data_ToolName[toolIndex] , 
        DeveloperList  = ", ".join(data_Developer[toolIndex]) , 
        KeyWordList  = ", ".join(data_KeyWords[toolIndex]) , 
        InnovatorName  = ", ".join(data_InnovatorName[toolIndex]) , 
        Description  = data_Description[toolIndex] , 
        ToolUrlOnLightHouse  = data_ToolUrlOnLightHouse[toolIndex] , 
        Rates  = data_Rates[toolIndex] , 
        DownloadTimes  = data_DownloadTimes[toolIndex] , 
        ImplementedDate  = data_ImplementedDate[toolIndex] 
        )
#   print ", ".join(data_KeyWords[toolIndex])
#   print thisTool
    
    db.session.add(thisTool)
    #db.session.commit()
    if len(data_Developer[toolIndex]) != 0:
        for developerName in data_Developer[toolIndex]:
            if not existsInDB_GotID(models.Developer,developerName):
                thisDeveloper = models.Developer(NameString = developerName)
                db.session.add(thisDeveloper)
                #db.session.commit()
            developer_tool_mapping = models.Developer_tool_map(tool_id = thisTool.id, developer_id = existsInDB_GotID(models.Developer,developerName))
            db.session.add(developer_tool_mapping)
            #db.session.commit()

    if len(data_KeyWords[toolIndex]) != 0:
        for keywordName in data_KeyWords[toolIndex]:
            if not existsInDB_GotID(models.Keyword,keywordName):
                keyword = models.Keyword(NameString = keywordName)
                db.session.add(keyword)
                #db.session.commit()
            keyword_tool_mapping = models.Keyword_tool_map(tool_id = thisTool.id, keyword_id = existsInDB_GotID(models.Keyword,keywordName))
            db.session.add(keyword_tool_mapping)
            #db.session.commit()
db.session.commit()





    

