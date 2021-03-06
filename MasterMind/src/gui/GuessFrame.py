'''
Created on 21 Jul 2016

@author: Janion
'''

import wx
import  wx.lib.scrolledpanel as scrolled
from src.backend.code.CodeItems import CodeItems
from backend.ai.AiPlayer import AiPlayer

class Window(wx.Frame):
    
    bigSize = 30
    smallSize = 15
    bigGapX = 35
    bigGapY = 40
    smallGapX = 20
    smallGapY = bigGapY
    
    # Build window and initialise objects
    def __init__(self, parent, idd, title):
        wx.Frame.__init__(self, parent, idd, title, size=(610, 785))
        self.setupMenu()
        self.panel = scrolled.ScrolledPanel(self, -1, size=(10, 10))
        self.panel.SetupScrolling()
        
        self.codeLength = 6
        self.maxGuesses = 25
        self.currentGuess = 0
        
        self.makeBitmaps()
        self.placePegHoles()
        self.placeExamplePegs()
        self.placeAnswerHoles()
        self.placeButtons()
        self.bindPegRow(0)
        
        self.compAi = AiPlayer(self.codeLength, AiPlayer.HARD)
#         self.refreshStartSize()
                
################################################################################
    
    def refreshStartSize(self):
        size = self.GetSize()
        panelSize = self.panel.GetSize()
        
        self.SetSize((min(size[0], panelSize[0] + 20), min(size[1], panelSize[1] + 65)))
                
################################################################################
    
    def setPegColour(self, event):
        event.GetEventObject().SetBitmap(self.currentColour.GetBitmap())
                
################################################################################
    
    def setCurrentColour(self, event):
        self.currentColour.SetBitmap(event.GetEventObject().GetBitmap())
                
################################################################################
    
    def restartGame(self, event):
        self.bindPegRow(0)
        self.resetPegs()
        self.resetAnswers()
                
################################################################################
    
    def submitGuess(self, event):
        guess = []
        for btn in self.pegs[self.currentGuess]:
            guess.append(self.getColourFrombitmap(btn.GetBitmap()))
            if guess[-1] == CodeItems.GREY:
                print "No"
                return
        
        self.fillInAnswer(self.compAi.evaluateGuess(guess))
        self.bindPegRow(self.currentGuess + 1)
                
################################################################################
    
    def fillInAnswer(self, answer):
        for x in xrange(len(answer)):
            if answer[x]:
                self.answers[self.currentGuess][x].SetBitmap(self.smallWhite)
            else:
                self.answers[self.currentGuess][x].SetBitmap(self.smallBlack)
                
################################################################################
    
    def getColourFrombitmap(self, bmp):
        for (img, colour) in self.bitmaps:
            if bmp == img:
                return colour
        return CodeItems.GREY
                
################################################################################
    
    def bindPegRow(self, index):
        self.currentGuess = index
        
        if 0 < index:
            if index < self.maxGuesses:
                for x in xrange(len(self.pegs[index])):
                    # Bind row and unbind previous row
                    self.pegs[index][x].Bind(wx.EVT_BUTTON, self.setPegColour)
                    self.pegs[index-1][x].Unbind(wx.EVT_BUTTON)
            else:
                for x in xrange(len(self.pegs[index])):
                    # Unbind previous row
                    self.pegs[index-1][x].Unbind(wx.EVT_BUTTON)
                    # Do something to show end of game
                
        else:
            for x in xrange(len(self.pegs[index])):
                self.pegs[0][x].Bind(wx.EVT_BUTTON, self.setPegColour)
                # Unbind all rows other than the first
                for y in xrange(1, len(self.pegs)):
                    self.pegs[y][x].Unbind(wx.EVT_BUTTON)
                
################################################################################
    
    def placeButtons(self):
        y = 10 + self.maxGuesses * self.bigGapY
        self.submitBtn = wx.Button(self.panel, -1, "Submit guess", pos=(10,y))
        self.restartBtn = wx.Button(self.panel, -1, "Restart game", pos=(10 + self.submitBtn.GetSize()[0],y))
        
        self.submitBtn.Bind(wx.EVT_BUTTON, self.submitGuess)
        self.restartBtn.Bind(wx.EVT_BUTTON, self.restartGame)
        
        self.setScrollPanelSize(y = y + self.submitBtn.GetSize()[1])
                
################################################################################
    
    def placeExamplePegs(self):
        x0 = 20 + (self.codeLength * self.bigGapX) + (self.codeLength * self.smallGapX)
        y = 0
        for item in self.bitmaps:
            self.createExamplePeg(x0, 10 + (y * self.bigGapY), item[0])
            y += 1
        
        self.createExamplePeg(x0, 10 + (y * self.bigGapY), self.grey)
        self.setScrollPanelSize(x = x0 + 2 * self.bigGapY, y = 10 + ((y + 2) * self.bigGapY))
        
        self.currentColour = wx.BitmapButton(self.panel, -1, self.grey, pos=(x0 + self.bigGapY, 10), style=wx.NO_BORDER)
                
################################################################################
    
    def createExamplePeg(self, x, y, colour):
            bmp = wx.BitmapButton(self.panel, -1, colour, pos=(x,y), style=wx.NO_BORDER)
            bmp.Bind(wx.EVT_BUTTON, self.setCurrentColour)
                
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
        
        x0 = 10 + self.codeLength * self.bigGapX
        offset = 10 + (self.bigSize - self.smallSize) / 2
        x = 0
        for x in xrange(self.codeLength):
            for y in xrange(self.maxGuesses):
                pos = (x0 + (x * self.smallGapX), offset + (y * self.smallGapY))
                self.answers[y][x] = wx.BitmapButton(self.panel, -1, self.smallGrey, pos=pos, style=wx.NO_BORDER)
                
################################################################################
    
    def resetPegs(self):
        for x in xrange(self.codeLength):
            for y in xrange(self.maxGuesses):
                self.pegs[y][x].SetBitmap(self.grey)
                
################################################################################
    
    def resetAnswers(self):
        for x in xrange(self.codeLength):
            for y in xrange(self.maxGuesses):
                self.answers[y][x].SetBitmap(self.smallGrey)
    
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
        
        self.bitmaps = [(self.pink, CodeItems.PINK),
                        (self.red, CodeItems.RED),
                        (self.orange, CodeItems.ORANGE),
                        (self.yellow, CodeItems.YELLOW),
                        (self.green, CodeItems.GREEN),
                        (self.blue, CodeItems.BLUE),
                        (self.white, CodeItems.WHITE),
                        (self.black, CodeItems.BLACK)
                        ]
        
        self.smallGrey = self.getBitmap(CodeItems.GREY, self.smallSize)
        self.smallWhite = self.getBitmap(CodeItems.WHITE, self.smallSize)
        self.smallBlack = self.getBitmap(CodeItems.BLACK, self.smallSize)
    
################################################################################
    
    def getBitmap(self, item, size):
        img = wx.Image(("gui/pegs/(%03d,%03d,%03d).png" %item), wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        
        image = wx.ImageFromBitmap(img)
        image = image.Scale(size, size, wx.IMAGE_QUALITY_HIGH)
        return wx.BitmapFromImage(image)

################################################################################
            
    def setupMenu(self):
        self.menuBar = wx.MenuBar()
        
        menu1 = wx.Menu()
        menu1.Append(101, "New game")
        menu1.AppendSeparator()
        menu1.Append(103, "Quit")
        self.menuBar.Append(menu1, "File")
        
        menu2 = wx.Menu()
        menu2.Append(201, "Configure game")
        self.menuBar.Append(menu2, "Config")
        
        self.SetMenuBar(self.menuBar)
        
        self.Bind(wx.EVT_MENU, self.restartGame, id=101)
        self.Bind(wx.EVT_MENU, self.close, id=103)
        
################################################################################
        
    def setScrollPanelSize(self, x=0, y=0):
        size = self.panel.GetSize()
         
        if x > size[0]:
            size[0] = x
            print "x = ", x
        if y > size[1]:
            size[1] = y
            print "y = ", y
         
        self.panel.SetSize(size)
        self.panel.SetupScrolling()
        
################################################################################
        
    def close(self, event):
        self.Destroy()
        
################################################################################
        
    def Show(self):
        size = self.panel.GetSize()
        super(Window, self).Show()
        self.panel.SetSize(size)
        self.panel.Refresh()
    