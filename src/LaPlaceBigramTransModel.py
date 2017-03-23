#! /usr/bin/env python
# -*- encoding: utf-8 -*-

import math , collections

class LaPlaceBigramTransModel (object):
    """ """
    def __init__ (self, delta):
        """ """
        self.delta = delta
        self.unigramCounts = collections.defaultdict(lambda: self.delta)
        self.bigramCounts= collections.defaultdict(lambda: self.delta)

    def train (self, corpus):
        """ """
        for sentence in corpus.sentences:
            datums = sentence.words
            datums_size = len(datums)

            for index in range(datums_size): 
                tag = datums[index].pos
                self.unigramCounts[tag] = self.unigramCounts[tag] + 1
                if index > 0:
                    previous_current = datums[index-1].pos+","+tag
                    self.bigramCounts[previous_current]= self.bigramCounts[previous_current] + 1

    def score (self, previous_tag,current_tag):
        """ """
        score = 0
        score = float(self.bigramCounts[previous_tag+","+current_tag]) / float(self.unigramCounts[current_tag])
        return score
