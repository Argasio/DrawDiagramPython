# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'draw_tools.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_FrameDrawButtons(object):
    def setupUi(self, FrameDrawButtons):
        if not FrameDrawButtons.objectName():
            FrameDrawButtons.setObjectName(u"FrameDrawButtons")
        FrameDrawButtons.resize(565, 460)
        self.verticalLayout = QVBoxLayout(FrameDrawButtons)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.BtnDrawRect = QPushButton(FrameDrawButtons)
        self.BtnDrawRect.setObjectName(u"BtnDrawRect")

        self.verticalLayout.addWidget(self.BtnDrawRect)

        self.BtnDrawArrow = QPushButton(FrameDrawButtons)
        self.BtnDrawArrow.setObjectName(u"BtnDrawArrow")

        self.verticalLayout.addWidget(self.BtnDrawArrow)


        self.retranslateUi(FrameDrawButtons)
        self.BtnDrawRect.clicked.connect(FrameDrawButtons.BtnClickedDrawRect)
        self.BtnDrawArrow.clicked.connect(FrameDrawButtons.BtnClickedDrawArrow)

        QMetaObject.connectSlotsByName(FrameDrawButtons)
    # setupUi

    def retranslateUi(self, FrameDrawButtons):
        FrameDrawButtons.setWindowTitle(QCoreApplication.translate("FrameDrawButtons", u"Form", None))
        self.BtnDrawRect.setText(QCoreApplication.translate("FrameDrawButtons", u"DrawRect", None))
        self.BtnDrawArrow.setText(QCoreApplication.translate("FrameDrawButtons", u"Draw Arrow", None))
    # retranslateUi

