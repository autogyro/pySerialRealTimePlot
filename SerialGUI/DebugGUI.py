# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version Jun 17 2015)
# http://www.wxformbuilder.org/
##
# PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
# Class MainWindow
###########################################################################


class MainWindow (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.Size(
            1705, 620), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        self.m_menubar1 = wx.MenuBar(0)
        self.Help = wx.Menu()
        self.About = wx.MenuItem(self.Help, wx.ID_ANY,
                                 u"关于软件", wx.EmptyString, wx.ITEM_NORMAL)
        self.Help.AppendItem(self.About)

        self.Protocol = wx.MenuItem(
            self.Help, wx.ID_ANY, u"调试协议", wx.EmptyString, wx.ITEM_NORMAL)
        self.Help.AppendItem(self.Protocol)

        self.m_menubar1.Append(self.Help, u"帮助")

        self.SetMenuBar(self.m_menubar1)

        fgSizer1 = wx.FlexGridSizer(3, 0, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer133 = wx.FlexGridSizer(0, 3, 0, 0)
        fgSizer133.SetFlexibleDirection(wx.BOTH)
        fgSizer133.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer14 = wx.FlexGridSizer(5, 1, 0, 0)
        fgSizer14.SetFlexibleDirection(wx.BOTH)
        fgSizer14.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer14.SetMinSize(wx.Size(200, 250))
        self.m_staticText2 = wx.StaticText(
            self, wx.ID_ANY, u"串口操作", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        self.m_staticText2.SetFont(
            wx.Font(20, 70, 90, 92, False, wx.EmptyString))

        fgSizer14.Add(self.m_staticText2, 0, wx.ALL, 5)

        self.m_button4 = wx.Button(
            self, wx.ID_ANY, u"打开", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer14.Add(self.m_button4, 0, wx.ALL, 5)

        self.m_button5 = wx.Button(
            self, wx.ID_ANY, u"关闭", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer14.Add(self.m_button5, 0, wx.ALL, 5)

        self.m_staticText11 = wx.StaticText(
            self, wx.ID_ANY, u"串口显示", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11.Wrap(-1)
        fgSizer14.Add(self.m_staticText11, 0, wx.ALL, 5)

        self.SerialPort = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer14.Add(self.SerialPort, 0, wx.ALL, 5)

        fgSizer133.Add(fgSizer14, 1, wx.EXPAND, 5)

        self.m_staticline6 = wx.StaticLine(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL)
        fgSizer133.Add(self.m_staticline6, 0, wx.EXPAND | wx.ALL, 5)

        ControlArea = wx.FlexGridSizer(0, 2, 0, 0)
        ControlArea.SetFlexibleDirection(wx.BOTH)
        ControlArea.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText8 = wx.StaticText(
            self, wx.ID_ANY, u"飞行控制", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)
        self.m_staticText8.SetFont(
            wx.Font(20, 70, 90, 92, False, wx.EmptyString))

        ControlArea.Add(self.m_staticText8, 0, wx.ALL, 5)

        fgSizer133.Add(ControlArea, 1, wx.EXPAND, 5)

        fgSizer1.Add(fgSizer133, 1, wx.EXPAND, 5)

        self.m_staticline1 = wx.StaticLine(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        fgSizer1.Add(self.m_staticline1, 0, wx.EXPAND | wx.ALL, 5)

        ParaArea = wx.FlexGridSizer(0, 1, 0, 0)
        ParaArea.SetFlexibleDirection(wx.BOTH)
        ParaArea.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText3 = wx.StaticText(
            self, wx.ID_ANY, u"数据显示", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        self.m_staticText3.SetFont(
            wx.Font(20, 70, 90, 92, False, wx.EmptyString))

        ParaArea.Add(self.m_staticText3, 0, wx.ALL, 5)

        fgSizer5 = wx.FlexGridSizer(0, 3, 0, 0)
        fgSizer5.SetFlexibleDirection(wx.BOTH)
        fgSizer5.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText91 = wx.StaticText(
            self, wx.ID_ANY, u"姿态", wx.DefaultPosition, wx.Size(350, -1), 0)
        self.m_staticText91.Wrap(-1)
        self.m_staticText91.SetForegroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.m_staticText91.SetBackgroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        fgSizer5.Add(self.m_staticText91, 0, wx.ALL, 5)

        self.m_staticText101 = wx.StaticText(
            self, wx.ID_ANY, u"位置", wx.DefaultPosition, wx.Size(350, -1), 0)
        self.m_staticText101.Wrap(-1)
        self.m_staticText101.SetBackgroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_INFOBK))

        fgSizer5.Add(self.m_staticText101, 0, wx.ALL, 5)

        ParaArea.Add(fgSizer5, 1, wx.EXPAND, 5)

        fgSizer25 = wx.FlexGridSizer(0, 6, 0, 0)
        fgSizer25.SetFlexibleDirection(wx.BOTH)
        fgSizer25.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText7 = wx.StaticText(
            self, wx.ID_ANY, u"Pitch", wx.DefaultPosition, wx.Size(110, -1), wx.ALIGN_CENTRE)
        self.m_staticText7.Wrap(-1)
        fgSizer25.Add(self.m_staticText7, 0, wx.ALL, 5)

        self.m_staticText9 = wx.StaticText(
            self, wx.ID_ANY, u"Roll", wx.DefaultPosition, wx.Size(110, -1), wx.ALIGN_CENTRE)
        self.m_staticText9.Wrap(-1)
        fgSizer25.Add(self.m_staticText9, 0, wx.ALL, 5)

        self.m_staticText10 = wx.StaticText(
            self, wx.ID_ANY, u"Yaw", wx.DefaultPosition, wx.Size(110, -1), wx.ALIGN_CENTRE)
        self.m_staticText10.Wrap(-1)
        fgSizer25.Add(self.m_staticText10, 0, wx.ALL, 5)

        self.m_staticText44 = wx.StaticText(
            self, wx.ID_ANY, u"PosX", wx.DefaultPosition, wx.Size(110, -1), wx.ALIGN_CENTRE)
        self.m_staticText44.Wrap(-1)
        fgSizer25.Add(self.m_staticText44, 0, wx.ALL, 5)

        self.m_staticText45 = wx.StaticText(
            self, wx.ID_ANY, u"PosY", wx.DefaultPosition, wx.Size(110, -1), wx.ALIGN_CENTRE)
        self.m_staticText45.Wrap(-1)
        fgSizer25.Add(self.m_staticText45, 0, wx.ALL, 5)

        self.m_staticText46 = wx.StaticText(self, wx.ID_ANY, u"PosZ", wx.DefaultPosition, wx.Size(
            110, -1), wx.ALIGN_CENTRE | wx.ALIGN_LEFT)
        self.m_staticText46.Wrap(-1)
        fgSizer25.Add(self.m_staticText46, 0, wx.ALL, 5)

        ParaArea.Add(fgSizer25, 1, wx.EXPAND, 5)

        fgSizer15 = wx.FlexGridSizer(0, 8, 0, 0)
        fgSizer15.SetFlexibleDirection(wx.BOTH)
        fgSizer15.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Pitch = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer15.Add(self.Pitch, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.Roll = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer15.Add(self.Roll, 0, wx.ALL, 5)

        self.Yaw = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer15.Add(self.Yaw, 0, wx.ALL, 5)

        self.PosX = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer15.Add(self.PosX, 0, wx.ALL, 5)

        self.PosY = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer15.Add(self.PosY, 0, wx.ALL, 5)

        self.PosZ = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer15.Add(self.PosZ, 0, wx.ALL, 5)

        self.m_button13 = wx.Button(
            self, wx.ID_ANY, u"发送", wx.DefaultPosition, wx.Size(-1, 28), 0)
        fgSizer15.Add(self.m_button13, 0, wx.ALL, 5)

        self.m_button14 = wx.Button(
            self, wx.ID_ANY, u"查询", wx.DefaultPosition, wx.Size(-1, 28), 0)
        fgSizer15.Add(self.m_button14, 0, wx.ALL, 5)

        ParaArea.Add(fgSizer15, 1, wx.EXPAND, 5)

        bSizer14 = wx.BoxSizer(wx.HORIZONTAL)

        ParaArea.Add(bSizer14, 1, wx.EXPAND, 5)

        self.m_staticline11 = wx.StaticLine(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        ParaArea.Add(self.m_staticline11, 0, wx.EXPAND | wx.ALL, 5)

        fgSizer51 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer51.SetFlexibleDirection(wx.BOTH)
        fgSizer51.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText911 = wx.StaticText(
            self, wx.ID_ANY, u"AnglePID", wx.DefaultPosition, wx.Size(450, -1), wx.ALIGN_CENTRE)
        self.m_staticText911.Wrap(-1)
        fgSizer51.Add(self.m_staticText911, 0, wx.ALL, 5)

        self.m_staticText1011 = wx.StaticText(
            self, wx.ID_ANY, u"RatePID", wx.DefaultPosition, wx.Size(750, -1), wx.ALIGN_CENTRE)
        self.m_staticText1011.Wrap(-1)
        fgSizer51.Add(self.m_staticText1011, 0, wx.ALL, 5)

        ParaArea.Add(fgSizer51, 1, wx.EXPAND, 5)

        fgSizer511 = wx.FlexGridSizer(0, 6, 0, 0)
        fgSizer511.SetFlexibleDirection(wx.BOTH)
        fgSizer511.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText9111 = wx.StaticText(
            self, wx.ID_ANY, u"Kp", wx.DefaultPosition, wx.Size(200, -1), wx.ALIGN_CENTRE)
        self.m_staticText9111.Wrap(-1)
        fgSizer511.Add(self.m_staticText9111, 0, wx.ALL, 5)

        self.m_staticText10111 = wx.StaticText(
            self, wx.ID_ANY, u"Ki", wx.DefaultPosition, wx.Size(40, -1), wx.ALIGN_CENTRE)
        self.m_staticText10111.Wrap(-1)
        fgSizer511.Add(self.m_staticText10111, 0, wx.ALL, 5)

        self.m_staticText35 = wx.StaticText(
            self, wx.ID_ANY, u"Kd", wx.DefaultPosition, wx.Size(200, -1), wx.ALIGN_CENTRE)
        self.m_staticText35.Wrap(-1)
        fgSizer511.Add(self.m_staticText35, 0, wx.ALL, 5)

        self.m_staticText36 = wx.StaticText(
            self, wx.ID_ANY, u"Kp", wx.DefaultPosition, wx.Size(250, -1), wx.ALIGN_RIGHT)
        self.m_staticText36.Wrap(-1)
        fgSizer511.Add(self.m_staticText36, 0, wx.ALL, 5)

        self.m_staticText37 = wx.StaticText(
            self, wx.ID_ANY, u"Ki", wx.DefaultPosition, wx.Size(220, -1), wx.ALIGN_CENTRE)
        self.m_staticText37.Wrap(-1)
        fgSizer511.Add(self.m_staticText37, 0, wx.ALL, 5)

        self.m_staticText38 = wx.StaticText(
            self, wx.ID_ANY, u"Kd", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText38.Wrap(-1)
        fgSizer511.Add(self.m_staticText38, 0, wx.ALL, 5)

        ParaArea.Add(fgSizer511, 1, wx.EXPAND, 5)

        fgSizer13 = wx.FlexGridSizer(0, 11, 0, 0)
        fgSizer13.SetFlexibleDirection(wx.BOTH)
        fgSizer13.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText39 = wx.StaticText(
            self, wx.ID_ANY, u"Pitch", wx.DefaultPosition, wx.Size(50, -1), 0)
        self.m_staticText39.Wrap(-1)
        fgSizer13.Add(self.m_staticText39, 0, wx.ALL, 5)

        self.m_textCtrl15 = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer13.Add(self.m_textCtrl15, 0, wx.ALL, 5)

        self.m_textCtrl16 = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer13.Add(self.m_textCtrl16, 0, wx.ALL, 5)

        self.m_textCtrl17 = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer13.Add(self.m_textCtrl17, 0, wx.ALL, 5)

        self.m_button9 = wx.Button(
            self, wx.ID_ANY, u"发送", wx.DefaultPosition, wx.Size(-1, 28), 0)
        fgSizer13.Add(self.m_button9, 0, wx.ALL, 5)

        self.m_button10 = wx.Button(
            self, wx.ID_ANY, u"查询", wx.DefaultPosition, wx.Size(-1, 28), 0)
        fgSizer13.Add(self.m_button10, 0, wx.ALL, 5)

        self.m_textCtrl18 = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer13.Add(self.m_textCtrl18, 0, wx.ALL, 5)

        self.m_textCtrl19 = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer13.Add(self.m_textCtrl19, 0, wx.ALL, 5)

        self.m_textCtrl20 = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer13.Add(self.m_textCtrl20, 0, wx.ALL, 5)

        self.m_button11 = wx.Button(
            self, wx.ID_ANY, u"发送", wx.DefaultPosition, wx.Size(-1, 28), 0)
        fgSizer13.Add(self.m_button11, 0, wx.ALL, 5)

        self.m_button12 = wx.Button(
            self, wx.ID_ANY, u"查询", wx.DefaultPosition, wx.Size(-1, 28), 0)
        fgSizer13.Add(self.m_button12, 0, wx.ALL, 5)

        ParaArea.Add(fgSizer13, 1, wx.EXPAND, 5)

        fgSizer131 = wx.FlexGridSizer(0, 360, 0, 0)
        fgSizer131.SetFlexibleDirection(wx.BOTH)
        fgSizer131.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText391 = wx.StaticText(
            self, wx.ID_ANY, u"Roll", wx.DefaultPosition, wx.Size(50, -1), 0)
        self.m_staticText391.Wrap(-1)
        fgSizer131.Add(self.m_staticText391, 0, wx.ALL, 5)

        self.m_textCtrl151 = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer131.Add(self.m_textCtrl151, 0, wx.ALL, 5)

        self.m_textCtrl161 = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer131.Add(self.m_textCtrl161, 0, wx.ALL, 5)

        self.m_textCtrl171 = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer131.Add(self.m_textCtrl171, 0, wx.ALL, 5)

        self.m_button91 = wx.Button(
            self, wx.ID_ANY, u"发送", wx.DefaultPosition, wx.Size(-1, 28), 0)
        fgSizer131.Add(self.m_button91, 0, wx.ALL, 5)

        self.m_button101 = wx.Button(
            self, wx.ID_ANY, u"查询", wx.DefaultPosition, wx.Size(-1, 28), 0)
        fgSizer131.Add(self.m_button101, 0, wx.ALL, 5)

        self.m_textCtrl181 = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer131.Add(self.m_textCtrl181, 0, wx.ALL, 5)

        self.m_textCtrl191 = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer131.Add(self.m_textCtrl191, 0, wx.ALL, 5)

        self.m_textCtrl201 = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer131.Add(self.m_textCtrl201, 0, wx.ALL, 5)

        self.m_button111 = wx.Button(
            self, wx.ID_ANY, u"发送", wx.DefaultPosition, wx.Size(-1, 28), 0)
        fgSizer131.Add(self.m_button111, 0, wx.ALL, 5)

        self.m_button121 = wx.Button(
            self, wx.ID_ANY, u"查询", wx.DefaultPosition, wx.Size(-1, 28), 0)
        fgSizer131.Add(self.m_button121, 0, wx.ALL, 5)

        ParaArea.Add(fgSizer131, 1, wx.EXPAND, 5)

        fgSizer132 = wx.FlexGridSizer(0, 11, 0, 0)
        fgSizer132.SetFlexibleDirection(wx.BOTH)
        fgSizer132.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText392 = wx.StaticText(
            self, wx.ID_ANY, u"Yaw", wx.DefaultPosition, wx.Size(50, -1), 0)
        self.m_staticText392.Wrap(-1)
        fgSizer132.Add(self.m_staticText392, 0, wx.ALL, 5)

        self.m_textCtrl152 = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer132.Add(self.m_textCtrl152, 0, wx.ALL, 5)

        self.m_textCtrl162 = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer132.Add(self.m_textCtrl162, 0, wx.ALL, 5)

        self.m_textCtrl172 = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer132.Add(self.m_textCtrl172, 0, wx.ALL, 5)

        self.m_button92 = wx.Button(
            self, wx.ID_ANY, u"发送", wx.DefaultPosition, wx.Size(-1, 28), 0)
        fgSizer132.Add(self.m_button92, 0, wx.ALL, 5)

        self.m_button102 = wx.Button(
            self, wx.ID_ANY, u"查询", wx.DefaultPosition, wx.Size(-1, 28), 0)
        fgSizer132.Add(self.m_button102, 0, wx.ALL, 5)

        self.m_textCtrl182 = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer132.Add(self.m_textCtrl182, 0, wx.ALL, 5)

        self.m_textCtrl192 = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer132.Add(self.m_textCtrl192, 0, wx.ALL, 5)

        self.m_textCtrl202 = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer132.Add(self.m_textCtrl202, 0, wx.ALL, 5)

        self.m_button112 = wx.Button(
            self, wx.ID_ANY, u"发送", wx.DefaultPosition, wx.Size(-1, 28), 0)
        fgSizer132.Add(self.m_button112, 0, wx.ALL, 5)

        self.m_button122 = wx.Button(
            self, wx.ID_ANY, u"查询", wx.DefaultPosition, wx.Size(-1, 28), 0)
        fgSizer132.Add(self.m_button122, 0, wx.ALL, 5)

        ParaArea.Add(fgSizer132, 1, wx.EXPAND, 5)

        fgSizer1.Add(ParaArea, 8, wx.EXPAND, 5)

        self.SetSizer(fgSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_MENU, self.OnAboutSoftware, id=self.About.GetId())
        self.Bind(wx.EVT_MENU, self.OnDebugProtocol, id=self.Protocol.GetId())
        self.m_button4.Bind(wx.EVT_BUTTON, self.OnOpenSerial)
        self.m_button5.Bind(wx.EVT_BUTTON, self.OnCloseSerial)
        self.m_button13.Bind(wx.EVT_BUTTON, self.OnPosSend)
        self.m_button14.Bind(wx.EVT_BUTTON, self.OnPosReceive)
        self.m_button9.Bind(wx.EVT_BUTTON, self.OnPitchAngleSend)
        self.m_button10.Bind(wx.EVT_BUTTON, self.OnPitchAngleReceive)
        self.m_button11.Bind(wx.EVT_BUTTON, self.OnPitchRateSend)
        self.m_button12.Bind(wx.EVT_BUTTON, self.OnPitchRateReceive)
        self.m_button91.Bind(wx.EVT_BUTTON, self.OnRollAngleSend)
        self.m_button101.Bind(wx.EVT_BUTTON, self.OnRollAngleReceive)
        self.m_button111.Bind(wx.EVT_BUTTON, self.OnRollRateSend)
        self.m_button121.Bind(wx.EVT_BUTTON, self.OnRollRateReceive)
        self.m_button92.Bind(wx.EVT_BUTTON, self.OnYawAngleSend)
        self.m_button102.Bind(wx.EVT_BUTTON, self.OnYawAngleReceive)
        self.m_button112.Bind(wx.EVT_BUTTON, self.OnYawRateSend)
        self.m_button122.Bind(wx.EVT_BUTTON, self.OnYawRateReceive)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def OnAboutSoftware(self, event):
        event.Skip()

    def OnDebugProtocol(self, event):
        event.Skip()

    def OnOpenSerial(self, event):
        event.Skip()

    def OnCloseSerial(self, event):
        event.Skip()

    def OnPosSend(self, event):
        event.Skip()

    def OnPosReceive(self, event):
        event.Skip()

    def OnPitchAngleSend(self, event):
        event.Skip()

    def OnPitchAngleReceive(self, event):
        event.Skip()

    def OnPitchRateSend(self, event):
        event.Skip()

    def OnPitchRateReceive(self, event):
        event.Skip()

    def OnRollAngleSend(self, event):
        event.Skip()

    def OnRollAngleReceive(self, event):
        event.Skip()

    def OnRollRateSend(self, event):
        event.Skip()

    def OnRollRateReceive(self, event):
        event.Skip()

    def OnYawAngleSend(self, event):
        event.Skip()

    def OnYawAngleReceive(self, event):
        event.Skip()

    def OnYawRateSend(self, event):
        event.Skip()

    def OnYawRateReceive(self, event):
        event.Skip()


###########################################################################
# Class MenuAbout
###########################################################################

class MenuAbout (wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString,
                           pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer23 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText12 = wx.StaticText(
            self, wx.ID_ANY, u"Python Serial Real Time Plot", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText12.Wrap(-1)
        bSizer23.Add(self.m_staticText12, 0, wx.ALL, 5)

        self.OK = wx.Button(self, wx.ID_ANY, u"OK",
                            wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer23.Add(self.OK, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(bSizer23)
        self.Layout()
        bSizer23.Fit(self)

        self.Centre(wx.BOTH)

        # Connect Events
        self.OK.Bind(wx.EVT_BUTTON, self.OK)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def OK(self, event):
        event.Skip()


###########################################################################
# Class MyFrame2
###########################################################################

class MyFrame2 (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.Size(
            500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        self.Centre(wx.BOTH)

    def __del__(self):
        pass
