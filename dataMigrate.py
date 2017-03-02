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


# Functions validateNameLists
# Validation of Name lists
def validateNameLists(strNameList):
    outputList = []
    outputList = re.split(',|;|/| and ',strNameList)
    # Removing email like <for.bar@example.com>
    for strName in outputList:
        strName = re.split('<',strName)[0]
        if strName.startswith(' '):
            strName = strName[1:]
        # print strName
    return outputList




# Convert description from html to plain string here:
for cell in worksheetInRAM['Z']:
    cell.value = html2textCall(cell.value)

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

print len(columnU)
print columnF

# Insert data
