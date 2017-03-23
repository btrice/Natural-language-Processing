#! /usr/bin/env python
# -*- encoding: utf-8 -*-

from Word import *
import re


class Sentence (object):
    """A sequence of Tokens"""

    def __init__ (self, line = None):
        """creates a sentence from a string"""
        self.words =[]
        if line:
            line.strip()
            self.words.append(Word('<S>', 'START'))
            # YOUR CODE HERE
            mots = line.split()
            for i in range(len(mots)):
                match = re.search(r'(.+)/([^/]+)',mots[i]) # n'importe quelle caractère suivie d'un mot qui contient pas /
                if match:
                    self.words.append(Word(match.group(1),match.group(2)))
            self.words.append(Word('<*EOS*>', 'END'))

    def __str__ (self):
        """ """
        return ' '.join([w.__str__() for w in self.words[1:-1]])
#def main ():
#    """Main function"""
#    p=Sentence("Et/CC pourtant/ADV ,/PONCT à/P y/CLO")
#    print p
#if __name__ == "__main__":
#    main()
