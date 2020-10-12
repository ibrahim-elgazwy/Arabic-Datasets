# -*- coding: utf-8 -*-
##
##import polyglot
##from polyglot.text import Text, Word
##from polyglot.downloader import downloader
##print(downloader.supported_languages_table("pos2"))


import csv

with open('RES1.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    dates = []
    colors = []
    for row in readCSV:
        print (row[0])
        print(row[1].decode('UTF-8'))
    
        
            
            
        
##        color = row[1]
##        date = row[0]
##
##        dates.append(date)
##        colors.append(color)
##    for w in dates:
##        print(w)
    
    


##        words.append(word)
##        polarity.append(polarity)
##
##    print(dates)
##    print(colors)


##words = ["preprocessing", "processor", "invaluable", "thankful", "crossed"]
##for w in words:
##  w = Word(w, language="en")
##  print("{:<20}{}".format(w, w.morphemes))
