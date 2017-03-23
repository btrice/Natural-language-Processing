#! /usr/bin/env python
# -*- encoding: utf-8 -*-

import math , collections

class LaPlaceEmissionModel (object):
    """ """
    def __init__ (self, delta):
        """ """
        self.delta = delta
        self.unigramCounts = collections.defaultdict(lambda: self.delta)
        self.bigramCounts = collections.defaultdict(lambda: self.delta)
        self.wordTagCounts = collections.defaultdict(lambda: self.delta)

    def train (self, corpus):
        """ """
        for sentence in corpus.sentences:
            datums = sentence.words
            datums_size = len(datums)

            for index in range(datums_size): 
                word = datums[index].form
                tag = datums[index].pos
                self.unigramCounts[tag] = self.unigramCounts[tag] + 1 # Num times we see the tag
                self.bigramCounts[word+","+tag] = self.bigramCounts[word+","+tag] + 1 # Num times we see word following with the tag ( word/tag)
                if word in self.wordTagCounts:
                    self.wordTagCounts[word].update({tag : self.bigramCounts[word+","+tag]})
                else:
                    self.wordTagCounts[word] = {tag : self.bigramCounts[word+","+tag]}
				
    def score (self, word, tag):
        """ """
        score=0
        score = float(self.bigramCounts[word+","+tag]) / float(self.unigramCounts[tag])
        return score
