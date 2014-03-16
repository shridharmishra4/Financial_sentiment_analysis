#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  polarity.py
#  
#  Copyright 2014 Shridhar Mishra <shridhar@shridhar>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

#text_file = open("polar.txt", "r")
#lines = text_file.read().split('   ') or text_file.read().split(" ") 
#print lines[1::2]
#print len(lines)
#text_file.close()
polarity= {}

count=0
import csv
with open('polar.txt', 'r') as f:
    reader = csv.reader(f,dialect='excel', delimiter='\t')
    #print len(row)
    for row in reader:
        polarity.update({row[0]:row[1]})
        #print polarity
        count +=1
#print count
#print polarity
#print len(polarity)
a=str(raw_input("enter a word:"))

print ("polarity of word is " + polarity[a] )




def write2file():
    f = open ('polardictionary.txt', 'w')
    f.write(str(polarity))
    f.close()


def openfile():
    h = open('mydict.txt', 'r')
    newdict = eval(h.read())
    
    print newdict
    print len(newdict)
    h.close()




def main():
    #write2file()
    
    return 0

if __name__ == '__main__':
    main()

