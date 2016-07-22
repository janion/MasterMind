'''
Created on 21 Jul 2016

@author: Janion
'''

from random import randint
from src.backend.code.CodeItems import CodeItems

class CodeGenerator():

    def generateCode(self, length):
        code = [None for x in xrange(length)]
        for x in xrange(len(code)):
            code[x] = CodeItems.getItem(randint(0, CodeItems.getItemCount() - 1))
        
        return code