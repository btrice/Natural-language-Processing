#! /usr/bin/env python
# -*- encoding: utf-8 -*-

class Evaluator (object):
    """ """
    def __init__ (self):
        """"""
        pass

    def evaluate(self, corpus_train, corpus_predicted):
        """ Evaluate the model : corpus_train and corpus_predicted should have the same word length"""
        total = 0
        correct = 0
        if(len(corpus_train.sentences) == len(corpus_predicted.sentences)): 
            for index in range(len(corpus_train.sentences)):
                sentence_train = (corpus_train.sentences)[index]
                words_train = sentence_train.words[1:-1] # remove START/END
                sentence_predicted = (corpus_predicted.sentences)[index]
                words_predicted = sentence_predicted.words[1:-1] # remove START/END
                #print("train_word : " +str(len(words_train)))
                #print("Predicted : " +str(len(words_predicted)))			
                for idx in range(len(words_train)):
                    total += 1
                    if words_train[idx].pos == words_predicted[idx].pos:
                        correct += 1

        print("total: " +str(total))
        print("correct: "+str(correct))
        print("accuracy: "+str(float(correct)/total))
