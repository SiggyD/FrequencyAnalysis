#! /usr/bin/python
import sys, getopt, string
'''
Performs monograph and digraph frequency calculations
'''		
print "*** Frequency Analysis *** Sigmundson ***" # 
if (len(sys.argv) < 2):
	print "Usage : FrequencyAnalsis.py <filename>"
	exit()
#import file
inputFile = open(sys.argv[1],"r")
cipherText = inputFile.read()
inputFile.close()
cipherText = cipherText.lower()

#decs
intArray = [0]*26
cleanText = ""

## MONOGRAPH ANALYSIS
print "### MONOGRAPHS ###"
for i in range(0,len(cipherText)):
	if ((ord(cipherText[i]) > 96) & (ord(cipherText[i]) < 123)):
		temp = ord(cipherText[i])-97
		intArray[temp]+=1
for i in range(0,26):
	print chr(i+97)+":",intArray[i]
#DIGRAPH ANALYSIS
print "### DIGRAPHS ### Minimum of 4 occurances"
for i in range(0,len(cipherText)):
	if ((ord(cipherText[i]) > 96) & (ord(cipherText[i]) < 122)):
		cleanText += cipherText[i]
for i in range(0,26):
	for j in range(0,26):
		searchTarget = string.ascii_lowercase[i] +string.ascii_lowercase[j]
		num = cleanText.count(searchTarget)
		if (num > 3):
			print string.ascii_lowercase[i] +string.ascii_lowercase[j] + ": ", num
			
		
