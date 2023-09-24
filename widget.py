# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(565, 460)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.FrameLeftToolbar = QFrame(Form)
        self.FrameLeftToolbar.setObjectName(u"FrameLeftToolbar")
        self.FrameLeftToolbar.setFrameShape(QFrame.StyledPanel)
        self.FrameLeftToolbar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.FrameLeftToolbar)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.horizontalLayout.addWidget(self.FrameLeftToolbar)

        self.FrameView = QFrame(Form)
        self.FrameView.setObjectName(u"FrameView")
        self.FrameView.setFrameShape(QFrame.StyledPanel)
        self.FrameView.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.FrameView)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.horizontalLayout.addWidget(self.FrameView)

        self.FrameRightToolbar = QFrame(Form)
        self.FrameRightToolbar.setObjectName(u"FrameRightToolbar")
        self.FrameRightToolbar.setFrameShape(QFrame.StyledPanel)
        self.FrameRightToolbar.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.FrameRightToolbar)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.horizontalLayout.addWidget(self.FrameRightToolbar)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
    # retranslateUi

