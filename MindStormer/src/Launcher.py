'''
Created on 21 Jul 2016

@author: Janion
'''

import wx
from src.gui.GuessFrame import Window

if __name__ == '__main__':
    app = wx.App()
    fr = Window(None, -1, 'Master Mind')
    fr.Show()
    app.MainLoop()