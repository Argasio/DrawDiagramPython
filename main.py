# This is a sample Python script.
from widget import *
from console import*
from GraphicsView import GraphicsView
from GraphicsScene import GraphicsScene
import sys
from PySide6 import QtWidgets
from PySide6 import QtGui
from PySide6.QtCore import QThread
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QGraphicsView,
    QGraphicsScene,
    QGraphicsRectItem,
)
from Presenter import ApplicationWindow
from PySide6.QtUiTools import QUiLoader

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
'''Main implementation for the graphic implementation inheriting QApplication'''
class MainApp(QApplication):
    def __init__(self):
        super().__init__()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    '''Create a QApplication Object'''
    app = MainApp()
    '''Create the Graphic Interface'''
    widget = ApplicationWindow()
    ''' Display it'''
    widget.show()
    '''The QApplication will bind the execution of the graphic application'''
    sys.exit(app.exec())


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
