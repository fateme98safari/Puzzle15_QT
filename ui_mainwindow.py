# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(342, 356)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btm1 = QPushButton(self.centralwidget)
        self.btm1.setObjectName(u"btm1")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btm1.sizePolicy().hasHeightForWidth())
        self.btm1.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(16)
        self.btm1.setFont(font)
        self.btm1.setStyleSheet(u"border-radius:29px;\n"
"background-color: rgb(170, 85, 255);")

        self.gridLayout.addWidget(self.btm1, 0, 0, 1, 1)

        self.btm2 = QPushButton(self.centralwidget)
        self.btm2.setObjectName(u"btm2")
        sizePolicy.setHeightForWidth(self.btm2.sizePolicy().hasHeightForWidth())
        self.btm2.setSizePolicy(sizePolicy)
        self.btm2.setFont(font)
        self.btm2.setStyleSheet(u"border-radius:29px;\n"
"background-color: rgb(170, 85, 255);")

        self.gridLayout.addWidget(self.btm2, 0, 1, 1, 1)

        self.btm5 = QPushButton(self.centralwidget)
        self.btm5.setObjectName(u"btm5")
        sizePolicy.setHeightForWidth(self.btm5.sizePolicy().hasHeightForWidth())
        self.btm5.setSizePolicy(sizePolicy)
        self.btm5.setFont(font)
        self.btm5.setStyleSheet(u"border-radius:29px;\n"
"background-color: rgb(170, 85, 255);")

        self.gridLayout.addWidget(self.btm5, 1, 0, 1, 1)

        self.btm6 = QPushButton(self.centralwidget)
        self.btm6.setObjectName(u"btm6")
        sizePolicy.setHeightForWidth(self.btm6.sizePolicy().hasHeightForWidth())
        self.btm6.setSizePolicy(sizePolicy)
        self.btm6.setFont(font)
        self.btm6.setStyleSheet(u"border-radius:29px;\n"
"background-color: rgb(170, 85, 255);")

        self.gridLayout.addWidget(self.btm6, 1, 1, 1, 1)

        self.btm9 = QPushButton(self.centralwidget)
        self.btm9.setObjectName(u"btm9")
        sizePolicy.setHeightForWidth(self.btm9.sizePolicy().hasHeightForWidth())
        self.btm9.setSizePolicy(sizePolicy)
        self.btm9.setFont(font)
        self.btm9.setStyleSheet(u"border-radius:29px;\n"
"background-color: rgb(170, 85, 255);")

        self.gridLayout.addWidget(self.btm9, 2, 0, 1, 1)

        self.btm13 = QPushButton(self.centralwidget)
        self.btm13.setObjectName(u"btm13")
        sizePolicy.setHeightForWidth(self.btm13.sizePolicy().hasHeightForWidth())
        self.btm13.setSizePolicy(sizePolicy)
        self.btm13.setFont(font)
        self.btm13.setStyleSheet(u"border-radius:29px;\n"
"background-color: rgb(170, 85, 255);")

        self.gridLayout.addWidget(self.btm13, 3, 0, 1, 1)

        self.btm7 = QPushButton(self.centralwidget)
        self.btm7.setObjectName(u"btm7")
        sizePolicy.setHeightForWidth(self.btm7.sizePolicy().hasHeightForWidth())
        self.btm7.setSizePolicy(sizePolicy)
        self.btm7.setFont(font)
        self.btm7.setStyleSheet(u"border-radius:29px;\n"
"background-color: rgb(170, 85, 255);")

        self.gridLayout.addWidget(self.btm7, 1, 2, 1, 1)

        self.btm3 = QPushButton(self.centralwidget)
        self.btm3.setObjectName(u"btm3")
        sizePolicy.setHeightForWidth(self.btm3.sizePolicy().hasHeightForWidth())
        self.btm3.setSizePolicy(sizePolicy)
        self.btm3.setFont(font)
        self.btm3.setStyleSheet(u"border-radius:29px;\n"
"background-color: rgb(170, 85, 255);")

        self.gridLayout.addWidget(self.btm3, 0, 2, 1, 1)

        self.btm4 = QPushButton(self.centralwidget)
        self.btm4.setObjectName(u"btm4")
        sizePolicy.setHeightForWidth(self.btm4.sizePolicy().hasHeightForWidth())
        self.btm4.setSizePolicy(sizePolicy)
        self.btm4.setFont(font)
        self.btm4.setStyleSheet(u"border-radius:29px;\n"
"background-color: rgb(170, 85, 255);")

        self.gridLayout.addWidget(self.btm4, 0, 3, 1, 1)

        self.btm8 = QPushButton(self.centralwidget)
        self.btm8.setObjectName(u"btm8")
        sizePolicy.setHeightForWidth(self.btm8.sizePolicy().hasHeightForWidth())
        self.btm8.setSizePolicy(sizePolicy)
        self.btm8.setFont(font)
        self.btm8.setStyleSheet(u"border-radius:29px;\n"
"background-color: rgb(170, 85, 255);")

        self.gridLayout.addWidget(self.btm8, 1, 3, 1, 1)

        self.btm10 = QPushButton(self.centralwidget)
        self.btm10.setObjectName(u"btm10")
        sizePolicy.setHeightForWidth(self.btm10.sizePolicy().hasHeightForWidth())
        self.btm10.setSizePolicy(sizePolicy)
        self.btm10.setFont(font)
        self.btm10.setStyleSheet(u"border-radius:29px;\n"
"background-color: rgb(170, 85, 255);")

        self.gridLayout.addWidget(self.btm10, 2, 1, 1, 1)

        self.btm11 = QPushButton(self.centralwidget)
        self.btm11.setObjectName(u"btm11")
        sizePolicy.setHeightForWidth(self.btm11.sizePolicy().hasHeightForWidth())
        self.btm11.setSizePolicy(sizePolicy)
        self.btm11.setFont(font)
        self.btm11.setStyleSheet(u"border-radius:29px;\n"
"background-color: rgb(170, 85, 255);")

        self.gridLayout.addWidget(self.btm11, 2, 2, 1, 1)

        self.btm12 = QPushButton(self.centralwidget)
        self.btm12.setObjectName(u"btm12")
        sizePolicy.setHeightForWidth(self.btm12.sizePolicy().hasHeightForWidth())
        self.btm12.setSizePolicy(sizePolicy)
        self.btm12.setFont(font)
        self.btm12.setStyleSheet(u"border-radius:29px;\n"
"background-color: rgb(170, 85, 255);")

        self.gridLayout.addWidget(self.btm12, 2, 3, 1, 1)

        self.btm14 = QPushButton(self.centralwidget)
        self.btm14.setObjectName(u"btm14")
        sizePolicy.setHeightForWidth(self.btm14.sizePolicy().hasHeightForWidth())
        self.btm14.setSizePolicy(sizePolicy)
        self.btm14.setFont(font)
        self.btm14.setStyleSheet(u"border-radius:29px;\n"
"background-color: rgb(170, 85, 255);")

        self.gridLayout.addWidget(self.btm14, 3, 1, 1, 1)

        self.btm15 = QPushButton(self.centralwidget)
        self.btm15.setObjectName(u"btm15")
        sizePolicy.setHeightForWidth(self.btm15.sizePolicy().hasHeightForWidth())
        self.btm15.setSizePolicy(sizePolicy)
        self.btm15.setFont(font)
        self.btm15.setStyleSheet(u"border-radius:29px;\n"
"background-color: rgb(170, 85, 255);")

        self.gridLayout.addWidget(self.btm15, 3, 2, 1, 1)

        self.btm16 = QPushButton(self.centralwidget)
        self.btm16.setObjectName(u"btm16")
        sizePolicy.setHeightForWidth(self.btm16.sizePolicy().hasHeightForWidth())
        self.btm16.setSizePolicy(sizePolicy)
        self.btm16.setFont(font)
        self.btm16.setStyleSheet(u"border-radius:29px;\n"
"background-color: rgb(170, 85, 255);")

        self.gridLayout.addWidget(self.btm16, 3, 3, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 342, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"puzzle15", None))
        self.btm1.setText("")
        self.btm2.setText("")
        self.btm5.setText("")
        self.btm6.setText("")
        self.btm9.setText("")
        self.btm13.setText("")
        self.btm7.setText("")
        self.btm3.setText("")
        self.btm4.setText("")
        self.btm8.setText("")
        self.btm10.setText("")
        self.btm11.setText("")
        self.btm12.setText("")
        self.btm14.setText("")
        self.btm15.setText("")
        self.btm16.setText("")
    # retranslateUi

