'''
Created on 21 Jul 2016

@author: Janion
'''

class Scorer():

    def __init__(self):
        self.scores = [0, 0]
    
################################################################################
    
    def player1Guesses(self, guesses):
        self.scores[0] += guesses
    
################################################################################
    
    def player2Guesses(self, guesses):
        self.scores[1] += guesses
        
################################################################################
    
    def getPlayer1Score(self):
        return self.scores[0]
        
################################################################################
    
    def getPlayer2Score(self):
        return self.scores[2]
        
################################################################################
    
    def getPlayerScores(self):
        return self.scores
    
################################################################################
    
    def resetScores(self):
        self.scores = [0, 0]