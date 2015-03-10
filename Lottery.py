#Boa:Dialog:Lottery

import wx

def create(parent):
    return Lottery(parent)

[wxID_LOTTERY, wxID_LOTTERYSTART, wxID_LOTTERYSTATICTEXT1, 
] = [wx.NewId() for _init_ctrls in range(3)]

class Lottery(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_LOTTERY, name='Lottery', parent=prnt,
              pos=wx.Point(596, 401), size=wx.Size(400, 250),
              style=wx.DEFAULT_DIALOG_STYLE, title='Dialog1')
        self.SetClientSize(wx.Size(384, 211))

        self.Start = wx.Button(id=wxID_LOTTERYSTART, label='button1',
              name='Start', parent=self, pos=wx.Point(128, 104),
              size=wx.Size(75, 24), style=0)
        self.Start.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_LOTTERYSTART)

        self.staticText1 = wx.StaticText(id=wxID_LOTTERYSTATICTEXT1,
              label='staticText1', name='staticText1', parent=self,
              pos=wx.Point(120, 24), size=wx.Size(88, 24), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton1Button(self, event):
        event.Skip()
