from PySide6 import QtWidgets
from GraphicsScene import GraphicsScene
from PySide6 import QtGui
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QGraphicsView,
    QGraphicsScene,
    QGraphicsRectItem,
)
from PySide6.QtCore import QPoint
from StateGraphicItem import StateGraphicItem
class GraphicsView(QGraphicsView):
    def __init__(self, scene, parent=None):
        print("View Init")
        super().__init__(parent)

        #set width and height of the viewport
        self.setFixedHeight(500)
        self.setFixedWidth(500)
        #assign graphics scene
        self.setScene(scene)
        #constrain scene space to viewport (eliminates offset when drawing!)
        self.setSceneRect(self.rect())
        self.mode = 0


        self.mode = 0
    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        print("press\n")

        if self.mode == 1:
            try:
                newItem = StateGraphicItem(QPoint(event.x(), event.y()))
                self.scene().AddItem(newItem)
                self.update()
            except Exception as ex:
                print(ex)
            print("add item\n")



        super(QGraphicsView, self).mousePressEvent(event)

    def SetMode(self, mode):
        self.mode = mode
        return