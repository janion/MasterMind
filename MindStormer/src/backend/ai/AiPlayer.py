'''
Created on 21 Jul 2016

@author: Janion
'''
from compiler.pycodegen import CodeGenerator

class AiPlayer():

    def __init__(self, codeLength, evaluatorClass):
        self.generator = CodeGenerator()
        self.code = self.generator.generateCode(codeLength)
        self.evaluator = evaluatorClass()
    
################################################################################
    
    def evaluateGuess(self, guess):
        return self.evaluator.evaluateGuess(guess)
    
################################################################################
    
    def generateNewCode(self, codeLength):
        self.code = self.generator.generateCode(codeLength)
        
################################################################################
    
    def setEvaluatorClass(self, evaluatorClass):
        self.evaluator = evaluatorClass()