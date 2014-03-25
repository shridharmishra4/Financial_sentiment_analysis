#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  urlparser.py
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

from lxml import html
import requests
import re


syn={}						#dictionary of each word with word as key and synonyms as its key elements
notfound=[]					#list of words not found in synonyms.com
count=0





def getsyn(word):
	global count
	#print "function initiated"
	synonyms=[]				#list of synonyms for each word with search word as key
	withoutbracket=''
	
	page = requests.get('http://www.synonym.com/synonyms/%s/'% word)#gets html of page
	tree = html.fromstring(page.text)#forms a tree of html
	#print page


	synon = tree.xpath('//span[@class="equals"]/text()') #fetch the required element from its xpath
	
	
	if len(synon)==0:
		notfound.append(word)
		count = count+1
		pass
	#print notfound
	else:	
		try:
			count =count+1
			
			for items in synon[0:2]:
				synonyms.extend((removebracket(items).split(",")))
			
			syn.update({word:synonyms})
			#syn.update({word:synon[0]})
			#print syn
			print count,"  ",(count/2007.0)
		
		
		except IndexError:
			pass


def write2file():
    f = open ('/home/shridhar/Financial_sentiment_analysis/txtfiles/positivesyndict.txt', 'w')
    f.write(str(syn))
    f.close()
    
    
    


def openfile():
    h = open('positivesyndict.txt', 'r')
    newdict = eval(h.read())
    print newdict
    print len(newdict)
    h.close()  
    
def removebracket(word):
	return re.sub(r'\(.*?\)', '',word)
	

def main():
	filename = open('/home/shridhar/Financial_sentiment_analysis/txtfiles/positive.txt')
	lines = [line.strip() for line in filename]
	
	
	for i in lines:
		getsyn('%s' % i)
	filename.close()
	write2file()
	#getsyn("angry")
	print syn
	print notfound
	#print len(syn)
	#print len(notfound)
	#print counter
	
	
	return 0

if __name__ == '__main__':
	main()

