'''
Created on 21 Jul 2016

@author: Janion
'''

from src.ai.validate.CodeEvaluator import CodeEvaluator

class HardEvaluator(CodeEvaluator):

    def __init__(self, code):
        self.code = code
    
################################################################################
    
    def evaluateGuess(self, guess):
        correct = 0
        tmpCode = [self.code[x] for x in xrange(len(self.code))]

        for x in xrange(len(self.code) - 1, -1, -1):
            if guess[x] in tmpCode:
                correct += 1
                tmpCode.remove(guess[x])

        result = [True for x in xrange(correct)]
        for x in xrange(len(self.code) - correct):
            result.append(False)
    
################################################################################
    
    def setCode(self, code):
        self.code = code