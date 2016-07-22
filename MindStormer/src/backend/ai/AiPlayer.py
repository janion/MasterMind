'''
Created on 21 Jul 2016

@author: Janion
'''

from src.backend.ai.setter.validate.HardEvaluator import HardEvaluator
from src.backend.ai.setter.validate.EasyEvaluator import EasyEvaluator
from src.backend.ai.setter.CodeGenerator import CodeGenerator

class AiPlayer():
    
    EASY = 0
    HARD = 1

    def __init__(self, codeLength, difficulty):
        self.generator = CodeGenerator()
        self.generateNewCode(codeLength)
        self.setEvaluator(difficulty)
    
################################################################################
    
    def evaluateGuess(self, guess):
        return self.evaluator.evaluateGuess(self.code, guess)
    
################################################################################
    
    def generateNewCode(self, codeLength):
        self.code = self.generator.generateCode(codeLength)
        
################################################################################
    
    def setEvaluator(self, difficulty):
        if difficulty == 0:
            self.evaluator = EasyEvaluator()
        else:
            self.evaluator = HardEvaluator()