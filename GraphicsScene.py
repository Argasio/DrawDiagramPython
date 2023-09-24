from PySide6 import QtWidgets
from PySide6 import QtGui
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QGraphicsView,
    QGraphicsScene,
    QGraphicsRectItem,
    QGraphicsItem
)

class GraphicsScene(QGraphicsScene):
    def __init__(self, x ,y, w, h):
        print("Scene Init")
        super().__init__(x, y, w, h)

        self.itemList = None
    def AddItem(self, item:QGraphicsItem):
        super(GraphicsScene, self).addItem(item)