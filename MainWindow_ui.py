# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 570)
        MainWindow.setMinimumSize(QSize(80, 80))
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.origin_img = QLabel(self.centralwidget)
        self.origin_img.setObjectName(u"origin_img")
        self.origin_img.setGeometry(QRect(10, 30, 330, 330))
        self.origin_img.setFrameShape(QFrame.Shape.Panel)
        self.processed_img = QLabel(self.centralwidget)
        self.processed_img.setObjectName(u"processed_img")
        self.processed_img.setGeometry(QRect(360, 30, 330, 330))
        self.processed_img.setFrameShape(QFrame.Shape.Panel)
        self.save_button = QPushButton(self.centralwidget)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(10, 440, 100, 80))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        self.save_button.setFont(font1)
        self.load_button = QPushButton(self.centralwidget)
        self.load_button.setObjectName(u"load_button")
        self.load_button.setEnabled(True)
        self.load_button.setGeometry(QRect(10, 360, 100, 80))
        self.load_button.setFont(font1)
        self.rgb2gray_button = QPushButton(self.centralwidget)
        self.rgb2gray_button.setObjectName(u"rgb2gray_button")
        self.rgb2gray_button.setGeometry(QRect(110, 360, 100, 80))
        self.rgb2hsv_button = QPushButton(self.centralwidget)
        self.rgb2hsv_button.setObjectName(u"rgb2hsv_button")
        self.rgb2hsv_button.setGeometry(QRect(110, 440, 100, 80))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 0, 71, 31))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.label.setFont(font2)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(500, 0, 81, 31))
        self.label_2.setFont(font2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 700, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.origin_img.setText("")
        self.processed_img.setText("")
        self.save_button.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u56fe\u7247", None))
        self.load_button.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u8f7d\u56fe\u7247", None))
        self.rgb2gray_button.setText(QCoreApplication.translate("MainWindow", u"\u8f6c\u4e3a\u7070\u5ea6\u56fe\u50cf", None))
        self.rgb2hsv_button.setText(QCoreApplication.translate("MainWindow", u"\u8f6c\u5230HSV\u7a7a\u95f4", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5904\u7406\u524d\u56fe\u50cf", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5904\u7406\u540e\u56fe\u50cf", None))
    # retranslateUi

