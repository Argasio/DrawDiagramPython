from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QGraphicsView,
    QGraphicsScene,
    QGraphicsItem,
    QGraphicsRectItem,
    QStyleOptionGraphicsItem,
)
from PySide6.QtCore import QPoint
from PySide6.QtGui import QBrush
from PySide6.QtGui import QColor
from PySide6.QtGui import QPainter
from PySide6.QtCore import QRect
from PySide6.QtCore import QRectF
from PySide6.QtCore import QLineF
class StateGraphicItem(QGraphicsItem):
    '''BoundingRect Required to be implemented from QGraphicsItem'''
    def boundingRect(self):
        return QRectF(self.rect)
    '''construct the stat representation as a rectangle'''
    def __init__(self, start:QPoint, end:QPoint):
        super().__init__()
        #self.setRect(QRect)
        print("item init")
        self.line = QLineF(start,end)
        print(str(anchor.x())+" "+str(anchor.y()))
        self.Brush = QBrush(QColor(125, 125, 128))
    '''paint method Required to be implemented from QGraphicsItem'''
    def paint(self, painter, *widget):
        painter.setBrush(self.Brush)
        painter.drawRect(self.rect)