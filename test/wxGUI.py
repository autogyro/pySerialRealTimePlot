import wx
import os
from data_plot import PlotFigure
from usual_figure import PlotUsualFigure

global pitch
global roll
global yaw
pitch = [0]
roll = [0]
yaw = [0]


class MyFrame(wx.Frame):
    """docstring for MyFrame"""

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200, 100))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.Show(True)


class MainWindow(wx.Frame):
    """docstring for MainWindow"""

    def __init__(self, parent, title):
        self.dirname = ''

        wx.Frame.__init__(self, parent, title=title, size=(200, -1))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar()
        ########### frames ###########
        framePitch = PlotFigure(None, 'pitch', pitch)
        framePitch.start()
        frameRoll = PlotFigure(None, 'roll', roll)
        frameRoll.start()

        ########### Menu ###########
        fileMenu = wx.Menu()
        menuAbout = fileMenu.Append(
            wx.ID_ABOUT, 'About', 'info about programe')
        fileMenu.AppendSeparator()
        menuExit = fileMenu.Append(wx.ID_EXIT, 'Exit', 'exit programe')
        fileMenu.AppendSeparator()
        menuOpen = fileMenu.Append(wx.ID_OPEN, 'Open', 'open file')

        ########### MenuBar ###########
        menubar = wx.MenuBar()
        menubar.Append(fileMenu, 'File')
        self.SetMenuBar(menubar)

        ###########Button Sizers ###########
        self.ButtonSizer = wx.BoxSizer(wx.HORIZONTAL)
        buttonOpen = wx.Button(self, -1, "Open")
        self.ButtonSizer.Add(buttonOpen, 1, wx.SHAPED |
                             wx.ALIGN_LEFT | wx.ALIGN_TOP)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.ButtonSizer, 0, wx.GROW)
        self.sizer.Add(self.control, 1, wx.EXPAND)

        # set sizer
        self.SetSizer(self.sizer)
        self.SetAutoLayout(True)
        self.sizer.Fit(self)

        ########### Event ###########
        # Menu
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        # Button
        self.Bind(wx.EVT_BUTTON, self.OnOpenSerial, buttonOpen)

        ########### show frame ###########
        self.Show()

    def OnAbout(self, event):
        dlg = wx.MessageDialog(self, 'A Serial Real Time Plot Debug Application Programmed by Python',
                               'About pySerial RT Plot', wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def OnExit(self, event):
        self.Close()

    def OnOpen(self, event):
        dlg = wx.FileDialog(self, 'Choose a file',
                            self.dirname, '', '*.*', wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close
        dlg.Destroy()

    def OnOpenSerial(self, event):
        print 'open serial'


if __name__ == "__main__":
    global pitch
    global roll
    global yaw
    app = wx.App(False)

    frame = MainWindow(None, 'pySerial RT Plot')

    app.MainLoop()
