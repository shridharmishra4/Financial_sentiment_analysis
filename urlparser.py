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


syn={}
notfound=[]




def getsyn(word):
	
	page = requests.get('http://www.synonym.com/synonyms/%s/'% word)
	tree = html.fromstring(page.text)
	#print page


	synon = tree.xpath('//span[@class="equals"]/text()')
	
	#print synon
	#print len(synon)
	if len(synon)==0:
		notfound.append(word)
	#print notfound
		
	try:
		syn.update({word:synon[0]})
		#print syn
	
	
	except IndexError:
		pass




def main():
	f = open('test.txt')
	#lines = f.readlines()
	lines = [line.strip() for line in open('test.txt')]
	for i in lines:


		getsyn('%s' % i)
	
	
	f.close()
	#getsyn("angry")
	print syn
	print notfound
	
	
	
	return 0

if __name__ == '__main__':
	main()

