# -*- coding: utf-8 -*-

import wx
from matplotlib.figure import Figure
import matplotlib.font_manager as font_manager
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
# wxWidgets object ID for the timer


# number of data points
POINTS = 300
y_lim = 1000
y_tick = 100


class PlotUsualFigure(wx.Frame):
    """Matplotlib wxFrame with animation effect"""

    def __init__(self, parent, plot_title, data_list, label_list, window_size=(600, 400)):
        wx.Frame.__init__(self, parent, wx.ID_ANY,
                          title=plot_title, size=window_size)
        # input figure settings
        self.data = data_list
        self.label = label_list
        self.winsize = window_size

        # Matplotlib Figure
        self.fig = Figure((6, 4), 100)
        # bind the Figure to the backend specific canvas
        self.canvas = FigureCanvas(self, wx.ID_ANY, self.fig)
        # add a subplot
        self.ax = self.fig.add_subplot(211)
        # limit the X and Y axes dimensions
        # self.ax.set_ylim([-y_lim, y_lim])
        self.ax.set_xlim([0, POINTS])

        self.ax.set_autoscale_on(False)
        self.ax.set_xticks([])
        # we want a tick every 10 point on Y (101 is to have 10
        # self.ax.set_yticks(range(-y_lim, y_lim + 1, y_tick))
        # disable autoscale, since we don't want the Axes to ad
        # draw a grid (it will be only for Y)
        self.ax.grid(True)
        # generates first "empty" plots
        self.user = [None] * POINTS
        # self.l_user, = self.ax.plot(range(POINTS), self.user, label='Acc_X')
        self.l_user, = self.ax.plot(
            range(POINTS), self.user, label=self.label[0])

        # add the legend
        self.ax.legend(loc='upper center',
                           ncol=4,
                           prop=font_manager.FontProperties(size=10))
        # force a draw on the canvas()
        # trick to show the grid and the legend
        self.canvas.draw()
        # save the clean background - everything but the line
        # is drawn and saved in the pixel buffer background
        self.bg = self.canvas.copy_from_bbox(self.ax.bbox)
        # bind events coming from timer with id = TIMER_ID
        # to the onTimer callback function
        self.TIMER_ID = wx.NewId()
        wx.EVT_TIMER(self, self.TIMER_ID, self.onTimer)
        self.timer = wx.Timer(self, self.TIMER_ID)

    def onTimer(self, evt):
        """callback function for timer events"""
        # restore the clean background, saved at the beginning
        self.canvas.restore_region(self.bg)
        # update the data
        # temp = np.random.randint(10, 80)
        temp = self.data[0]
        self.user = self.user[1:] + [temp]
        # update the plot
        self.l_user.set_ydata(self.user)
        # just draw the "animated" objects
        # It is used to efficiently update Axes data (axis ticks, labels, etc
        # are not updated)
        self.ax.draw_artist(self.l_user)
        self.canvas.blit(self.ax.bbox)

        ymin, ymax = self.ax.get_ylim()  # update xlim and ylim
        # if (temp >= ymax):
        #     self.ax.set_ylim(ymin + temp - ymax + 200,
        #                      temp + 200)

        #     # ymin, ymax = self.ax.get_ylim()
        #     self.canvas.draw()
        #     # self.ax.set_yticks(range(ymin, ymax+1, y_tick))
        # elif (temp <= ymin):
        #     self.ax.set_ylim(temp - 200,
        #                      ymax + temp - ymin - 200)
        #     self.canvas.draw()

    def __del__(self):
        self.timer.Stop()

    def start(self):
        self.timer.Start(50)
        self.Show()
