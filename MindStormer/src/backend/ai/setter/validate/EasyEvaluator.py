'''
Created on 21 Jul 2016

@author: Janion
'''

from src.ai.validate.CodeEvaluator import CodeEvaluator

class EasyEvaluator(CodeEvaluator):

    def __init__(self, code):
        self.code = code
    
################################################################################
    
    def evaluateGuess(self, guess):
        result = [None for x in xrange(len(self.code))]
        for x in xrange(len(self.code)):
            if self.code[x] == guess[x]:
                result[x] = True
            else:
                result[x] = False
    
################################################################################
    
    def setCode(self, code):
        self.code = code