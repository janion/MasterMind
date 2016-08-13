'''
Created on 21 Jul 2016

@author: Janion
'''

from src.backend.ai.setter.validate.CodeEvaluator import CodeEvaluator

class EasyEvaluator(CodeEvaluator):

    def evaluateGuess(self, code, guess):
        result = [None for x in xrange(len(code))]
        for x in xrange(len(code)):
            if code[x] == guess[x]:
                result[x] = True
            else:
                result[x] = False
        
        return result