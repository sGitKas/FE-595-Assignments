# get requests library
import requests
import re

batRegex = re.compile('<P>(.+?)</P>')
f = open("female.txt", "w")
m = open ("male.txt", "w")

def getWebString():
    r = requests.get('https://theyfightcrime.org')
    m2 = batRegex.findall(r.text)
    splitstrs = m2[0].split('.')
    return splitstrs

def getLineFromWeb():
    strs = getWebString()
    m.write(strs[0]+'\n')
    f.write(strs[1]+'\n')

def getAllData():
    for x in range(1,51):
        print(" Getting Strings "+ str(x) )
        getLineFromWeb()


getAllData()


# make rest calls to theyfightcrime.org

# Write a HTML Parser that extracts the first and second line of the message in HTML

# Save the data into different files

