'''
Created on 21 Jul 2016

@author: Janion
'''

import wx
from src.backend.code.CodeItems import CodeItems

class Window(wx.Frame):
    
    bigSize = 30
    smallSize = 15
    bigGapX = 35
    bigGapY = 40
    smallGapX = 20
    smallGapY = bigGapY
    
    # Build window and initialise objects
    def __init__(self, parent, idd, title):
        wx.Frame.__init__(self, parent, idd, title, size=(610, 685))
        self.panel = wx.Panel(self, -1)
        
        self.SetMinSize(self.GetSize())
        self.SetMaxSize(self.GetMinSize())
        
        self.codeLength = 5
        self.maxGuesses = 12
        
        self.makeBitmaps()
        self.placePegHoles()
        self.placeExamplePegs()
        self.placeAnswerHoles()
        
        self.bindPegRow(0)
                
################################################################################
    
    def setPegColour(self, event):
        event.GetEventObject().SetBitmap(self.currentColour.GetBitmap())
                
################################################################################
    
    def setCurrentColour(self, event):
        self.currentColour.SetBitmap(event.GetEventObject().GetBitmap())
                
################################################################################
    
    def bindPegRow(self, index):
        if index > 0:
            for x in xrange(len(self.pegs[index])):
                # Bind row and unbind previous row
                self.pegs[index][x].Bind(wx.EVT_BUTTON, self.setPegColour)
                self.pegs[index-1][x].Unbind(wx.EVT_BUTTON)
        else:
            for x in xrange(len(self.pegs[index])):
                self.pegs[0][x].Bind(wx.EVT_BUTTON, self.setPegColour)
                # Unbind all rows other than the first
                for y in xrange(1, len(self.pegs)):
                    self.pegs[y][x].Unbind(wx.EVT_BUTTON)
                
################################################################################
    
    def placeExamplePegs(self):
        xPos = 300
        for y in xrange(CodeItems.getItemCount()):
            pos = (xPos, 10 + (y * self.bigGapY))
            bmp = wx.BitmapButton(self.panel, -1, self.bitmaps[y], pos=pos, style=wx.NO_BORDER)
            bmp.Bind(wx.EVT_BUTTON, self.setCurrentColour)
        
        self.currentColour = wx.BitmapButton(self.panel, -1, self.grey, pos=(xPos + self.bigGapY, 10), style=wx.NO_BORDER)
                
################################################################################
    
    def placePegHoles(self):
        
        self.pegs = [[None for x in xrange(self.codeLength)] for x in xrange(self.maxGuesses)]
        
        x = 0
        for x in xrange(self.codeLength):
            for y in xrange(self.maxGuesses):
                pos = (10 + (x * self.bigGapX), 10 + (y * self.bigGapY))
                self.pegs[y][x] = wx.BitmapButton(self.panel, -1, self.grey, pos=pos, style=wx.NO_BORDER)
                
################################################################################
    
    def placeAnswerHoles(self):
        
        self.answers = [[None for x in xrange(self.codeLength)] for x in xrange(self.maxGuesses)]
        
        x = 0
        for x in xrange(self.codeLength):
            for y in xrange(self.maxGuesses):
                pos = (190 + (x * self.smallGapX), 17 + (y * self.smallGapY))
                self.answers[y][x] = wx.BitmapButton(self.panel, -1, self.smallGrey, pos=pos, style=wx.NO_BORDER)
    
################################################################################
    
    def makeBitmaps(self):
        self.pink = self.getBitmap(CodeItems.PINK, self.bigSize)
        self.red = self.getBitmap(CodeItems.RED, self.bigSize)
        self.orange = self.getBitmap(CodeItems.ORANGE, self.bigSize)
        self.yellow = self.getBitmap(CodeItems.YELLOW, self.bigSize)
        self.green = self.getBitmap(CodeItems.GREEN, self.bigSize)
        self.blue = self.getBitmap(CodeItems.BLUE, self.bigSize)
        self.white = self.getBitmap(CodeItems.WHITE, self.bigSize)
        self.black = self.getBitmap(CodeItems.BLACK, self.bigSize)
        self.grey = self.getBitmap(CodeItems.GREY, self.bigSize)
        
        self.bitmaps = [self.pink, self.red, self.orange, self.yellow, self.green, self.blue, self.white, self.black]
        
        self.smallGrey = self.getBitmap(CodeItems.GREY, self.smallSize)
        self.smallWhite = self.getBitmap(CodeItems.WHITE, self.smallSize)
        self.smallBlack = self.getBitmap(CodeItems.BLACK, self.smallSize)
    
################################################################################
    
    def getBitmap(self, item, size):
        img = wx.Image(("gui/pegs/(%03d,%03d,%03d).png" %item), wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        
        image = wx.ImageFromBitmap(img)
        image = image.Scale(size, size, wx.IMAGE_QUALITY_HIGH)
        return wx.BitmapFromImage(image)
    