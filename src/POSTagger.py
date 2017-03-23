#! /usr/bin/env python
# -*- encoding: utf-8 -*-

from Corpus import *
from LaPlaceBigramTransModel import *
from LaPlaceEmissionModel import *
from Evaluator import *

class POSTagger(object) :
    """ The Pos Tagger class
    """

    def __init__(self, transmodel, emmodel) :
        self.transmodel = transmodel
        self.emmodel = emmodel
        self.resultWithLogProbabily = Sentence()

    def train (self, corpus):
        """Train the POStagger"""
        self.transmodel.train(corpus)
        self.emmodel.train(corpus)
        

    def tag (self, corpus):
        """scoring of each sentence of the corpus"""

        res = Corpus()
        res.sentences = [self.viterbi(s) for s in corpus.sentences]
        return res

    def viterbi(self, sentence):
        #Viterbi scoring	
        result = Sentence()
        log_probability = 0
        first_round = True
        not_found = False
        max_probability = 0
        probability = 0.0000000001
        datums = sentence.words
        datums_size = len(datums)
        y_1 = '*'
        for index in range(datums_size): 	
            # Check for end of sentence
            word = datums[index].form
            # Check if there is an existing label associated to the word	   
            if word in self.emmodel.wordTagCounts:
                not_found = False
                max_probability = 0
                for label in list(self.emmodel.wordTagCounts[word]):
                    # Calculate e(x|y)
                    emission = self.emmodel.score(word,label)
                    # Calculate q(y| y_i-1)
                    unigram = y_1
                    bigram = y_1 + ","+ label
                    parameter = 0.0000000001
                    if bigram in self.transmodel.bigramCounts:
                        parameter = self.transmodel.score(y_1,label)
                        probability = parameter*emission
                    if probability > max_probability:
                        max_probability = probability
                        arg_max = label	
            else:
                self.resultWithLogProbabily.words.append(Word(word,"UNKWON\n"))
                result.words.append(Word(word,"UNKWON\n"))					
                not_found = True
                    
            if not_found == False:					
                log_probability = log_probability + math.log(max_probability)
                self.resultWithLogProbabily.words.append(Word(word,arg_max+"_"+str(log_probability)+'\n'))
                result.words.append(Word(word,arg_max))			
                y_1 = arg_max	
        return result

def main ():
    """Main function"""


    p = POSTagger(LaPlaceBigramTransModel(0.0), LaPlaceEmissionModel(0.0))
    train_corpus = Corpus("../data/ftb_2.tagged")
    dev_corpus = Corpus("../data/test.tagged")
    print("CORPUS_ORIGINAL")	
    print(dev_corpus)
    p.train(train_corpus)
    dev_tagged = p.tag(dev_corpus)
    print("PREDICTED_CORPUS")
    print(dev_tagged)
    e = Evaluator()
    e.evaluate(dev_corpus, dev_tagged)
    #print(p.resultWithLogProbabily)

if __name__ == "__main__":
    main()
