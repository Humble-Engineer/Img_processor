# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1230, 766)
        MainWindow.setMinimumSize(QSize(1230, 766))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.label)

        self.origin_img = QLabel(self.centralwidget)
        self.origin_img.setObjectName(u"origin_img")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.origin_img.sizePolicy().hasHeightForWidth())
        self.origin_img.setSizePolicy(sizePolicy1)
        self.origin_img.setFrameShape(QFrame.Shape.Panel)

        self.verticalLayout_8.addWidget(self.origin_img)


        self.horizontalLayout.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_2)

        self.result_img = QLabel(self.centralwidget)
        self.result_img.setObjectName(u"result_img")
        sizePolicy1.setHeightForWidth(self.result_img.sizePolicy().hasHeightForWidth())
        self.result_img.setSizePolicy(sizePolicy1)
        self.result_img.setFrameShape(QFrame.Shape.Panel)

        self.verticalLayout_9.addWidget(self.result_img)


        self.horizontalLayout.addLayout(self.verticalLayout_9)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.color_space_Box = QComboBox(self.centralwidget)
        self.color_space_Box.addItem("")
        self.color_space_Box.addItem("")
        self.color_space_Box.addItem("")
        self.color_space_Box.setObjectName(u"color_space_Box")
        self.color_space_Box.setMinimumSize(QSize(0, 50))

        self.verticalLayout_2.addWidget(self.color_space_Box)

        self.color_space_button = QPushButton(self.centralwidget)
        self.color_space_button.setObjectName(u"color_space_button")
        self.color_space_button.setMinimumSize(QSize(0, 50))

        self.verticalLayout_2.addWidget(self.color_space_button)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_4)

        self.geometric_Box = QComboBox(self.centralwidget)
        self.geometric_Box.addItem("")
        self.geometric_Box.addItem("")
        self.geometric_Box.addItem("")
        self.geometric_Box.addItem("")
        self.geometric_Box.setObjectName(u"geometric_Box")
        self.geometric_Box.setMinimumSize(QSize(0, 50))

        self.verticalLayout_3.addWidget(self.geometric_Box)

        self.geometric_button = QPushButton(self.centralwidget)
        self.geometric_button.setObjectName(u"geometric_button")
        self.geometric_button.setMinimumSize(QSize(0, 50))

        self.verticalLayout_3.addWidget(self.geometric_button)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_6)

        self.noise_Box = QComboBox(self.centralwidget)
        self.noise_Box.addItem("")
        self.noise_Box.addItem("")
        self.noise_Box.setObjectName(u"noise_Box")
        self.noise_Box.setMinimumSize(QSize(0, 50))

        self.verticalLayout_4.addWidget(self.noise_Box)

        self.noise_button = QPushButton(self.centralwidget)
        self.noise_button.setObjectName(u"noise_button")
        self.noise_button.setMinimumSize(QSize(0, 50))

        self.verticalLayout_4.addWidget(self.noise_button)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setItalic(False)
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_5)

        self.blur_Box = QComboBox(self.centralwidget)
        self.blur_Box.addItem("")
        self.blur_Box.addItem("")
        self.blur_Box.addItem("")
        self.blur_Box.addItem("")
        self.blur_Box.setObjectName(u"blur_Box")
        self.blur_Box.setMinimumSize(QSize(0, 50))
        self.blur_Box.setDuplicatesEnabled(False)

        self.verticalLayout_5.addWidget(self.blur_Box)

        self.blur_button = QPushButton(self.centralwidget)
        self.blur_button.setObjectName(u"blur_button")
        self.blur_button.setMinimumSize(QSize(0, 50))

        self.verticalLayout_5.addWidget(self.blur_button)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_7)

        self.edge_Box = QComboBox(self.centralwidget)
        self.edge_Box.addItem("")
        self.edge_Box.addItem("")
        self.edge_Box.addItem("")
        self.edge_Box.setObjectName(u"edge_Box")
        self.edge_Box.setMinimumSize(QSize(0, 50))
        self.edge_Box.setMaxVisibleItems(10)

        self.verticalLayout_6.addWidget(self.edge_Box)

        self.edge_button = QPushButton(self.centralwidget)
        self.edge_button.setObjectName(u"edge_button")
        self.edge_button.setMinimumSize(QSize(0, 50))
        self.edge_button.setAutoRepeat(False)

        self.verticalLayout_6.addWidget(self.edge_button)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_8)

        self.draw_button = QPushButton(self.centralwidget)
        self.draw_button.setObjectName(u"draw_button")
        self.draw_button.setMinimumSize(QSize(0, 50))

        self.verticalLayout_7.addWidget(self.draw_button)

        self.fft_button = QPushButton(self.centralwidget)
        self.fft_button.setObjectName(u"fft_button")
        self.fft_button.setMinimumSize(QSize(0, 50))

        self.verticalLayout_7.addWidget(self.fft_button)


        self.horizontalLayout_2.addLayout(self.verticalLayout_7)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.load_button = QPushButton(self.centralwidget)
        self.load_button.setObjectName(u"load_button")
        self.load_button.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.load_button.sizePolicy().hasHeightForWidth())
        self.load_button.setSizePolicy(sizePolicy2)
        self.load_button.setMinimumSize(QSize(0, 40))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setUnderline(False)
        self.load_button.setFont(font3)

        self.verticalLayout.addWidget(self.load_button)

        self.reset_button = QPushButton(self.centralwidget)
        self.reset_button.setObjectName(u"reset_button")
        sizePolicy2.setHeightForWidth(self.reset_button.sizePolicy().hasHeightForWidth())
        self.reset_button.setSizePolicy(sizePolicy2)
        self.reset_button.setMinimumSize(QSize(0, 40))
        self.reset_button.setFont(font3)

        self.verticalLayout.addWidget(self.reset_button)

        self.save_button = QPushButton(self.centralwidget)
        self.save_button.setObjectName(u"save_button")
        sizePolicy2.setHeightForWidth(self.save_button.sizePolicy().hasHeightForWidth())
        self.save_button.setSizePolicy(sizePolicy2)
        self.save_button.setMinimumSize(QSize(0, 40))
        self.save_button.setFont(font3)

        self.verticalLayout.addWidget(self.save_button)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ImageToolkit", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5904\u7406\u524d\u56fe\u50cf", None))
        self.origin_img.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5904\u7406\u540e\u56fe\u50cf", None))
        self.result_img.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u7a7a\u95f4\u7c7b\u578b", None))
        self.color_space_Box.setItemText(0, QCoreApplication.translate("MainWindow", u"GRAY", None))
        self.color_space_Box.setItemText(1, QCoreApplication.translate("MainWindow", u"HSV", None))
        self.color_space_Box.setItemText(2, QCoreApplication.translate("MainWindow", u"YCrCb", None))

        self.color_space_button.setText(QCoreApplication.translate("MainWindow", u"\u8f6c\u6362\u8272\u5f69\u7a7a\u95f4", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u53d8\u6362\u65b9\u5f0f", None))
        self.geometric_Box.setItemText(0, QCoreApplication.translate("MainWindow", u"\u6c34\u5e73\u7ffb\u8f6c", None))
        self.geometric_Box.setItemText(1, QCoreApplication.translate("MainWindow", u"\u7ad6\u76f4\u7ffb\u8f6c", None))
        self.geometric_Box.setItemText(2, QCoreApplication.translate("MainWindow", u"\u987a\u65f6\u9488\u65cb\u8f6c", None))
        self.geometric_Box.setItemText(3, QCoreApplication.translate("MainWindow", u"\u9006\u65f6\u9488\u65cb\u8f6c", None))

        self.geometric_button.setText(QCoreApplication.translate("MainWindow", u"\u51e0\u4f55\u53d8\u6362", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u566a\u58f0\u6837\u5f0f", None))
        self.noise_Box.setItemText(0, QCoreApplication.translate("MainWindow", u"\u9ad8\u65af\u566a\u58f0", None))
        self.noise_Box.setItemText(1, QCoreApplication.translate("MainWindow", u"\u6912\u76d0\u566a\u58f0", None))

        self.noise_button.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u566a\u58f0", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u6ee4\u6ce2\u65b9\u6cd5", None))
        self.blur_Box.setItemText(0, QCoreApplication.translate("MainWindow", u"\u5747\u503c\u6ee4\u6ce2", None))
        self.blur_Box.setItemText(1, QCoreApplication.translate("MainWindow", u"\u4e2d\u503c\u6ee4\u6ce2", None))
        self.blur_Box.setItemText(2, QCoreApplication.translate("MainWindow", u"\u9ad8\u65af\u6ee4\u6ce2", None))
        self.blur_Box.setItemText(3, QCoreApplication.translate("MainWindow", u"\u4e8c\u7ef4\u5377\u79ef", None))

        self.blur_button.setText(QCoreApplication.translate("MainWindow", u"\u6ee4\u6ce2\u5904\u7406", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u8fb9\u7f18\u7b97\u5b50", None))
        self.edge_Box.setItemText(0, QCoreApplication.translate("MainWindow", u"Canny", None))
        self.edge_Box.setItemText(1, QCoreApplication.translate("MainWindow", u"Laplacian", None))
        self.edge_Box.setItemText(2, QCoreApplication.translate("MainWindow", u"Sobel", None))

        self.edge_button.setText(QCoreApplication.translate("MainWindow", u"\u8fb9\u7f18\u68c0\u6d4b", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u5c5e\u6027", None))
        self.draw_button.setText(QCoreApplication.translate("MainWindow", u"\u7070\u5ea6\u76f4\u65b9\u56fe", None))
        self.fft_button.setText(QCoreApplication.translate("MainWindow", u"\u7070\u5ea6fft\u9891\u8c31", None))
        self.load_button.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u8f7d\u56fe\u50cf", None))
        self.reset_button.setText(QCoreApplication.translate("MainWindow", u"\u6062\u590d\u539f\u56fe", None))
        self.save_button.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u56fe\u50cf", None))
    # retranslateUi

