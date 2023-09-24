from PySide6.QtCore import QThread
from PySide6.QtCore import QObject
from PySide6.QtCore import QPointF
from PySide6.QtCore import QEvent
from GraphicsView import *
from GraphicsView import *
import sys
class Console(QObject):
    def __init__(self):
        super().__init__()


    def Hello(self):
        print("Hello World")
    def run(self):
        """Long-running task."""
        while 1:
            QThread.sleep(1)
