from usual_figure import PlotUsualFigure
import wx

pitch = [1, 2, 5]
label = ['first', 'second', 'third']

if __name__ == '__main__':
    ############# gui loop set #############
    app = wx.PySimpleApp()

    parent = PlotUsualFigure(parent=None, plot_title='parent',
                             data_list=pitch, label_list=label)
    parent.start()
    # PlotUsualFigure('acc y', roll).start()

    PlotUsualFigure(parent=parent, plot_title='child',
                    data_list=pitch, label_list=label).start()

    app.MainLoop()
