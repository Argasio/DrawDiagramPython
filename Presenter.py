from GraphicsView import GraphicsView
from GraphicsScene import GraphicsScene
import sys
from widget import Ui_Form as ui_main_widget
from main_window import Ui_MainWindow as ui_main_window
from draw_tools import Ui_FrameDrawButtons as ui_draw
from PySide6 import QtWidgets
from PySide6 import QtGui
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QGraphicsView,
    QGraphicsScene,
    QGraphicsRectItem, QHBoxLayout,
)
'''Presenter for the draw tool widget'''
class DrawToolWidget(QWidget):
    def __init__(self, view:GraphicsView):
        '''Initiate the QGraphicsView'''
        super().__init__()
        '''Assign the view so we can use it within the presenter functions'''
        self.view = view
    '''Draws a State'''
    def BtnClickedDrawRect(self):
        self.view.SetMode(1)
    '''Draws a Transition'''
    def BtnClickedDrawArrow(self):
        return

'''Presenter for the main window'''
class ApplicationWindow(QMainWindow):
    def __init__(self, ):
        print("widget init")
        super().__init__()
        '''Create the scene'''
        self.scene = GraphicsScene(0, 0, 400, 400)
        '''Create the application custom view implementation'''
        self.view = GraphicsView(self.scene)
        '''Create the main window widget from the model'''
        self.main_window_form = ui_main_window()
        '''Setup the Ui elements injecting the QMainWindow'''
        self.main_window_form.setupUi(self)
        '''Declare the widget to apply as central element'''
        self.main_widget = QWidget()
        '''Declare the central widget template'''
        self.main_widget_form = ui_main_widget()
        '''setup the widget with the model template'''
        self.main_widget_form.setupUi(self.main_widget)
        '''Declare the draw tool widget template'''
        self.draw_tool_widget_form = ui_draw()
        '''Create the Draw tool widget (use the custom presenter since it has callbacks)'''
        self.draw_tool_widget = DrawToolWidget(self.view)
        '''Setup the draw Widget with the model template'''
        self.draw_tool_widget_form.setupUi(self.draw_tool_widget)
        '''Attach the central widget to the main window central frame'''
        self.main_window_form.FrameMiddle.layout().addWidget(self.main_widget)
        '''Attach the draw widget to the right frame of the central widget'''
        self.main_widget_form.FrameRightToolbar.layout().addWidget(self.draw_tool_widget)
        '''Attach the Custom GraphicView Presenter to the central part of the central widget'''
        self.main_widget_form.FrameView.layout().addWidget(self.view)
        '''Init mode variable'''
        self.mode = 0


        return