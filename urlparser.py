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




def getsyn(word):
	synonyms=[]				#list of synonyms for each word with search word as key
	
	page = requests.get('http://www.synonym.com/synonyms/%s/'% word)#gets html of page
	tree = html.fromstring(page.text)#forms a tree of html
	#print page


	synon = tree.xpath('//span[@class="equals"]/text()') #fetch the required element from its xpath
	
	
	if len(synon)==0:
		notfound.append(word)
	#print notfound
		
	try:
		#synonyms.append(re.sub(r'\(.*?\)', '',synon.split(',',[0])))
		synonyms.extend(re.sub(r'\(.*?\)', '',synon.split(',',[0])))
		"""
		Test append and extend
		"""
		print synonyms[0]
		
		syn.update({word:synon})
		#syn.update({word:synon[0]})
		#print syn
	
	
	except IndexError:
		pass


def write2file():
    f = open ('synonymdict.txt', 'w')
    f.write(str(syn))
    f.close()
    
    
    


def openfile():
    h = open('synonymdict.txt', 'r')
    newdict = eval(h.read())
    print newdict
    print len(newdict)
    h.close()  

def main():
	#f = open('test.txt')
	##lines = f.readlines()
	#lines = [line.strip() for line in open('test.txt')]
	#for i in lines:


		#getsyn('%s' % i)
	
	
	#f.close()
	getsyn("angry")
	#print syn
	print notfound
	
	
	
	return 0

if __name__ == '__main__':
	main()

