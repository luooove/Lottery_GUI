#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import Lottery2

modules ={u'Lottery2': [1, 'Main frame of Application', u'Lottery2.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = Lottery2.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
