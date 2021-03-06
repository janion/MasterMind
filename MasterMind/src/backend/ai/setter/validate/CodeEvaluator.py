'''
Created on 21 Jul 2016

@author: Janion
'''

from abc import ABCMeta, abstractmethod

class CodeEvaluator():
    __metaclass__ = ABCMeta

    @abstractmethod
    def evaluateGuess(self, code, guess):
        raise NotImplementedError()