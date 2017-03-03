#!env/bin/python
# -*- coding: UTF-8 -*-
from lib import html2text
html2textCall = html2text.html2text.html2text
import sys, re
from openpyxl import load_workbook
reload(sys)
sys.setdefaultencoding('utf8')

workbookInRAM = load_workbook('data/defaultData.xlsx')
worksheetInRAM = workbookInRAM.active


# Functions validateLists
# Validation of Name lists
def validateLists(strNameList):
    outputList = []
    inputList = re.split(',|;|/| and ',strNameList)
    # Removing email like <for.bar@example.com>
    for strName in inputList:
        strName = re.split('<',strName)[0]
        strName = re.split('\(',strName)[0]
        if strName.startswith(' '):
            strName = strName[1:]
        outputList.append(strName)
        # print strName
    return outputList


# Filter and Convert description from html to plain string here:
columnZ = []
for cell in worksheetInRAM['Z']:
    columnZ.append(html2textCall(cell.value))

# filter names of Developer
columnU = []
for cell in worksheetInRAM['U']:
    if cell.value == None:
        columnU.append([])
    else:
        columnU.append(validateLists(cell.value))

# filter names of InnovatorName
columnF = []
for cell in worksheetInRAM['F']:
    if cell.value == None:
        columnF.append([])
    else :
        columnF.append(validateLists(cell.value))

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
        columnT.append(cell.value)
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
#

# Insert data

Developer = columnU
InnovatorName = columnF
Description = columnZ
ToolName = columnE
KeyWords = columnT
ToolUrlOnLightHouse = columnAA
Rates = columnAB
DownloadTimes = columnP
ServiceArea = columnD

print Rates
