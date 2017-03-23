#! /usr/bin/env python
# -*- encoding: utf-8 -*-

class Word (object):
    """ """
    def __init__ (self, form, pos):
        """ """
        self.form = form
        self.pos = pos

    def __str__ (self):
        """ """
        return self.form + "/" + self.pos

    def __repr__ (self):
        """ """
        return self.__str__()
