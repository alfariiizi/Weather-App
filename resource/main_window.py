# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import icon.icon_rc as icon_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1092, 785)
        MainWindow.setStyleSheet(u"background-color: #A0E4CB;\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frameHeader = QFrame(self.centralwidget)
        self.frameHeader.setObjectName(u"frameHeader")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameHeader.sizePolicy().hasHeightForWidth())
        self.frameHeader.setSizePolicy(sizePolicy)
        self.frameHeader.setMinimumSize(QSize(1080, 137))
        self.frameHeader.setStyleSheet(u"background-color: #0D4C92;\n"
"border-radius: 5px;\n"
"border-style: solid;\n"
"border-width: 0px 0px 3px 0px;")
        self.frameHeader.setFrameShape(QFrame.StyledPanel)
        self.frameHeader.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frameHeader)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(120, -1, 120, -1)
        self.titleApp = QPushButton(self.frameHeader)
        self.titleApp.setObjectName(u"titleApp")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.titleApp.sizePolicy().hasHeightForWidth())
        self.titleApp.setSizePolicy(sizePolicy1)
        self.titleApp.setMinimumSize(QSize(351, 81))
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.titleApp.setFont(font)
        self.titleApp.setStyleSheet(u"border: none;\n"
"color: #white;")
        icon = QIcon()
        icon.addFile(u":/icon/weather-44.png", QSize(), QIcon.Normal, QIcon.Off)
        self.titleApp.setIcon(icon)
        self.titleApp.setIconSize(QSize(80, 80))

        self.horizontalLayout_2.addWidget(self.titleApp)

        self.horizontalSpacer = QSpacerItem(313, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.aboutBtn = QPushButton(self.frameHeader)
        self.aboutBtn.setObjectName(u"aboutBtn")
        sizePolicy1.setHeightForWidth(self.aboutBtn.sizePolicy().hasHeightForWidth())
        self.aboutBtn.setSizePolicy(sizePolicy1)
        self.aboutBtn.setMinimumSize(QSize(161, 41))
        font1 = QFont()
        font1.setBold(True)
        self.aboutBtn.setFont(font1)
        self.aboutBtn.setStyleSheet(u"background-color: white;\n"
"color: #0D4C92;\n"
"border: 3px solid;\n"
"border-radius: 10px;")

        self.horizontalLayout_2.addWidget(self.aboutBtn)


        self.verticalLayout_3.addWidget(self.frameHeader)

        self.frameContent = QFrame(self.centralwidget)
        self.frameContent.setObjectName(u"frameContent")
        self.frameContent.setStyleSheet(u"border: none;")
        self.frameContent.setFrameShape(QFrame.StyledPanel)
        self.frameContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frameContent)
        self.verticalLayout_2.setSpacing(30)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(120, 80, 120, 100)
        self.frameSearch = QFrame(self.frameContent)
        self.frameSearch.setObjectName(u"frameSearch")
        sizePolicy.setHeightForWidth(self.frameSearch.sizePolicy().hasHeightForWidth())
        self.frameSearch.setSizePolicy(sizePolicy)
        self.frameSearch.setStyleSheet(u"background-color: #0D4C92;\n"
"border: 3px solid;\n"
"border-radius: 10px;")
        self.frameSearch.setFrameShape(QFrame.StyledPanel)
        self.frameSearch.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frameSearch)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, -1, 20, -1)
        self.searchBar = QLineEdit(self.frameSearch)
        self.searchBar.setObjectName(u"searchBar")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.searchBar.sizePolicy().hasHeightForWidth())
        self.searchBar.setSizePolicy(sizePolicy2)
        self.searchBar.setMinimumSize(QSize(600, 41))
        self.searchBar.setStyleSheet(u"background-color: white;\n"
"color: black;\n"
"border-radius: 8px;")

        self.horizontalLayout.addWidget(self.searchBar)

        self.searchBtn = QPushButton(self.frameSearch)
        self.searchBtn.setObjectName(u"searchBtn")
        sizePolicy1.setHeightForWidth(self.searchBtn.sizePolicy().hasHeightForWidth())
        self.searchBtn.setSizePolicy(sizePolicy1)
        self.searchBtn.setMinimumSize(QSize(118, 41))
        self.searchBtn.setStyleSheet(u"background-color: white;\n"
"color: black;\n"
"border-radius: 8px;")

        self.horizontalLayout.addWidget(self.searchBtn)


        self.verticalLayout_2.addWidget(self.frameSearch)

        self.frameInformation = QFrame(self.frameContent)
        self.frameInformation.setObjectName(u"frameInformation")
        self.frameInformation.setMinimumSize(QSize(821, 361))
        self.frameInformation.setStyleSheet(u"background-color: #0D4C92;\n"
"border: 3px solid;\n"
"border-radius: 10px;\n"
"box-shadow: rgba(0, 0, 0, 0.8) 0px 5px 15px;")
        self.frameInformation.setFrameShape(QFrame.StyledPanel)
        self.frameInformation.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frameInformation)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.cityLbl = QLabel(self.frameInformation)
        self.cityLbl.setObjectName(u"cityLbl")
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        self.cityLbl.setFont(font2)
        self.cityLbl.setLayoutDirection(Qt.LeftToRight)
        self.cityLbl.setStyleSheet(u"color: white;\n"
"border: none;")
        self.cityLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.cityLbl)

        self.temperatureLbl = QLabel(self.frameInformation)
        self.temperatureLbl.setObjectName(u"temperatureLbl")
        self.temperatureLbl.setFont(font2)
        self.temperatureLbl.setStyleSheet(u"color: white;\n"
"border: none;")
        self.temperatureLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.temperatureLbl)

        self.descLbl = QLabel(self.frameInformation)
        self.descLbl.setObjectName(u"descLbl")
        self.descLbl.setFont(font2)
        self.descLbl.setStyleSheet(u"color: white;\n"
"border: none;")
        self.descLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.descLbl)


        self.verticalLayout_2.addWidget(self.frameInformation)


        self.verticalLayout_3.addWidget(self.frameContent)

        MainWindow.setCentralWidget(self.centralwidget)
        self.frameContent.raise_()
        self.frameHeader.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleApp.setText(QCoreApplication.translate("MainWindow", u"Weather App", None))
        self.aboutBtn.setText(QCoreApplication.translate("MainWindow", u"About Version", None))
        self.searchBar.setText("")
        self.searchBar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search . . .", None))
        self.searchBtn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.cityLbl.setText(QCoreApplication.translate("MainWindow", u"Yogyakarta", None))
        self.temperatureLbl.setText(QCoreApplication.translate("MainWindow", u"30\u00b0 Celcius", None))
        self.descLbl.setText(QCoreApplication.translate("MainWindow", u"Overcast Clouds", None))
    # retranslateUi

