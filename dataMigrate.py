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

# Convert description from html to plain string here:
for cell in worksheetInRAM['Z']:
    cell.value = html2textCall(cell.value)
# Validation of Name lists

def validateNameLists(strNameList):
    outputList = list()
    outputList = re.split(r'(?:,|;|\s)\s*',strNameList)a
    # Removing email like <for.bar@example.com>
    for strName in outputList:
        strName = strName.split("<")[0]
    return outputList


# Insert data
