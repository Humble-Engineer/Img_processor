# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'demo.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(2, -6, 631, 431))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.title = QLabel(self.layoutWidget)
        self.title.setObjectName(u"title")

        self.horizontalLayout.addWidget(self.title)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.number1 = QDoubleSpinBox(self.layoutWidget)
        self.number1.setObjectName(u"number1")

        self.horizontalLayout_2.addWidget(self.number1)

        self.add = QLabel(self.layoutWidget)
        self.add.setObjectName(u"add")

        self.horizontalLayout_2.addWidget(self.add)

        self.number2 = QDoubleSpinBox(self.layoutWidget)
        self.number2.setObjectName(u"number2")

        self.horizontalLayout_2.addWidget(self.number2)

        self.equal = QLabel(self.layoutWidget)
        self.equal.setObjectName(u"equal")

        self.horizontalLayout_2.addWidget(self.equal)

        self.result = QLabel(self.layoutWidget)
        self.result.setObjectName(u"result")

        self.horizontalLayout_2.addWidget(self.result)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.bar_label = QLabel(self.layoutWidget)
        self.bar_label.setObjectName(u"bar_label")

        self.horizontalLayout_3.addWidget(self.bar_label)

        self.progressBar = QProgressBar(self.layoutWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.horizontalLayout_3.addWidget(self.progressBar)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.delay_lable = QLabel(self.layoutWidget)
        self.delay_lable.setObjectName(u"delay_lable")

        self.horizontalLayout_4.addWidget(self.delay_lable)

        self.delay = QSpinBox(self.layoutWidget)
        self.delay.setObjectName(u"delay")

        self.horizontalLayout_4.addWidget(self.delay)

        self.cal_button = QPushButton(self.layoutWidget)
        self.cal_button.setObjectName(u"cal_button")

        self.horizontalLayout_4.addWidget(self.cal_button)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u6cd5\u5668", None))
        self.add.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.result.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.bar_label.setText(QCoreApplication.translate("MainWindow", u"\u8fdb\u5ea6\uff1a", None))
        self.delay_lable.setText(QCoreApplication.translate("MainWindow", u"\u5ef6\u65f6\uff1a", None))
        self.cal_button.setText(QCoreApplication.translate("MainWindow", u"\u8ba1\u7b97", None))
    # retranslateUi

