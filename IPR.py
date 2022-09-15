import string
import urllib.request as urllib2
import csv

# API url
url = "http://ip-api.com/line/"

# open the api url
response = urllib2.urlopen(str(url))

data = response.read()

# write the results in a csv file
with open('IPlookup.csv', 'wb') as f:
    f.write(data)

testfile = open("IPlookup.csv","r")#opens grades text file and reads from it
for line in testfile:#for loop
    myListOfSplitLine = line.strip('\n').split(" ")#splits each index by a space and strips new line characters 
    Studentname = myListOfSplitLine[0]#stores first index of list

    print (Studentname)
