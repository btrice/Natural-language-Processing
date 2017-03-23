#! /usr/bin/env python
# -*- encoding: utf-8 -*-

from Sentence import *


class Corpus (object):
    """A Corpus of Sentences"""

    def __init__ (self, filename = None):
        """create a corpus, possibly from file"""
        if filename:
            self.read_corpus(filename)
        else:
            self.sentences = []


    def read_corpus (self, filename):
        """ """
        self.sentences = []
        f = open(filename)
        for line in f:
            self.sentences.append(Sentence(line))


    def __str__ (self):
        """ """
        return '\n'.join([s.__str__() for s in self.sentences])
