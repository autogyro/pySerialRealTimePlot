# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainWindow
###########################################################################

class MainWindow ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"串口操作", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer11.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"打开", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_button4, 0, wx.ALL, 5 )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"关闭", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_button5, 0, wx.ALL, 5 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"串口显示", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		bSizer11.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.SerialPort = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.SerialPort, 0, wx.ALL, 5 )


		bSizer10.Add( bSizer11, 1, wx.EXPAND, 5 )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"数据显示", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer13.Add( self.m_staticText3, 0, wx.ALL, 5 )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer18 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Pitch", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		bSizer18.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.Pitch = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.Pitch, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer15.Add( bSizer18, 1, wx.EXPAND, 5 )

		bSizer19 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Roll", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		bSizer19.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.Roll = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer19.Add( self.Roll, 0, wx.ALL, 5 )


		bSizer15.Add( bSizer19, 1, wx.EXPAND, 5 )

		bSizer20 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Yaw", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		bSizer20.Add( self.m_staticText10, 0, wx.ALL, 5 )

		self.Yaw = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20.Add( self.Yaw, 0, wx.ALL, 5 )


		bSizer15.Add( bSizer20, 1, wx.EXPAND, 5 )


		bSizer14.Add( bSizer15, 1, wx.EXPAND, 5 )


		bSizer13.Add( bSizer14, 1, wx.EXPAND, 5 )


		bSizer10.Add( bSizer13, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer10 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.Help = wx.Menu()
		self.About = wx.MenuItem( self.Help, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.Help.AppendItem( self.About )

		self.m_menubar1.Append( self.Help, u"Help" )

		self.SetMenuBar( self.m_menubar1 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button4.Bind( wx.EVT_BUTTON, self.OnOpenSerial )
		self.m_button5.Bind( wx.EVT_BUTTON, self.OnCloseSerial )
		self.Bind( wx.EVT_MENU, self.OnAboutSoftware, id = self.About.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnOpenSerial( self, event ):
		event.Skip()

	def OnCloseSerial( self, event ):
		event.Skip()

	def OnAboutSoftware( self, event ):
		event.Skip()


###########################################################################
## Class MenuAbout
###########################################################################

class MenuAbout ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

		bSizer23 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Python Serial Real Time Plot", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		bSizer23.Add( self.m_staticText12, 0, wx.ALL, 5 )

		self.OK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.OK, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer23 )
		self.Layout()
		bSizer23.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.OK.Bind( wx.EVT_BUTTON, self.OK )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OK( self, event ):
		event.Skip()


