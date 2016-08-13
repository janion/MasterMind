'''
Created on 21 Jul 2016

@author: Janion
'''

class CodeItems(object):
    
    PINK = (255, 0, 255)
    RED = (255, 0, 0)
    ORANGE = (255, 127, 0)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREY = (127, 127, 127)
    
    _items = [PINK, RED, ORANGE, YELLOW, GREEN, BLUE, WHITE, BLACK]

################################################################################
    
    @staticmethod
    def getItemCount():
        return len(CodeItems._items)
    
################################################################################
    
    @staticmethod
    def getItems():
        return [CodeItems._items[x] for x in xrange(len(CodeItems._items))]
    
################################################################################
    
    @staticmethod
    def getItem(index):
        return CodeItems._items[index]