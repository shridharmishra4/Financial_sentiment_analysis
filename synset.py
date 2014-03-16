#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  synset.py
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



from nltk.corpus import wordnet as wn
#nltk.download()
syn=wn.synset('tired.n.1')
print wn.synsets('tired.n.1')
print syn.lemma_names
#,syn.hypernyms()
#for i,j in enumerate(wn.synsets('good')):
  #print "Meaning",i, "NLTK ID:", j.name
  #print "Definition:",j.definition

#from nltk.corpus import wordnet
#from nltk.stem.wordnet import WordNetLemmatizer
#import itertools


#def Synonym_Checker(word1, word2):
    #"""Checks if word1 and word2 and synonyms. Returns True if they are, otherwise False"""
    #equivalence = WordNetLemmatizer()
    #word1 = equivalence.lemmatize(word1)
    #word2 = equivalence.lemmatize(word2)

    #word1_synonyms = wordnet.synsets(word1)
    #word2_synonyms = wordnet.synsets(word2)

    #scores = [i.wup_similarity(j) for i, j in list(itertools.product(word1_synonyms, word2_synonyms))]
    #max_index = scores.index(max(scores))
    #best_match = (max_index/len(word1_synonyms), max_index % len(word1_synonyms)-1)

    #word1_set = word1_synonyms[best_match[0]].lemma_names
    #word2_set = word2_synonyms[best_match[1]].lemma_names
    #match = False
    #match = [match or word in word2_set for word in word1_set][0]

    #return match

#print Synonym_Checker("tomato", "Lycopersicon_esculentum")


def main():
	
	return 0

if __name__ == '__main__':
	main()

