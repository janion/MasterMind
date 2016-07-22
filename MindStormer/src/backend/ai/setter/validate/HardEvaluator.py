'''
Created on 21 Jul 2016

@author: Janion
'''

from src.backend.ai.setter.validate.CodeEvaluator import CodeEvaluator


class HardEvaluator(CodeEvaluator):
    
    def evaluateGuess(self, code, guess):
        result = []

        for x in xrange(len(code) - 1, -1, -1):
            if guess[x] == code[x]:
                result.append(True)

        for x in xrange(len(code) - len(result)):
            result.append(False)
        
        return result