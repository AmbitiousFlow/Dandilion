# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainzQxqhb.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys
sys.dont_write_bytecode = True 

import app.resources.assets

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainAvZruz.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QTextEdit, QWidget)


class MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(898, 495)
        icon = QIcon()
        icon.addFile(u":/icons/assets/icons8-dandelion-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QSize(10, 10))
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.HelpFaq))
        self.actionAbout.setIcon(icon1)
        self.MainLayout = QWidget(MainWindow)
        self.MainLayout.setObjectName(u"MainLayout")
        self.gridLayout_2 = QGridLayout(self.MainLayout)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.LogsOutputBox = QGroupBox(self.MainLayout)
        self.LogsOutputBox.setObjectName(u"LogsOutputBox")
        self.gridLayout_3 = QGridLayout(self.LogsOutputBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.LogsTextEdit = QTextEdit(self.LogsOutputBox)
        self.LogsTextEdit.setObjectName(u"LogsTextEdit")
        self.LogsTextEdit.setEnabled(False)

        self.gridLayout_3.addWidget(self.LogsTextEdit, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.LogsOutputBox, 4, 0, 1, 1)

        self.ActionsGroupBox = QGroupBox(self.MainLayout)
        self.ActionsGroupBox.setObjectName(u"ActionsGroupBox")
        self.gridLayout_5 = QGridLayout(self.ActionsGroupBox)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.DownloadProgress = QProgressBar(self.ActionsGroupBox)
        self.DownloadProgress.setObjectName(u"DownloadProgress")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DownloadProgress.sizePolicy().hasHeightForWidth())
        self.DownloadProgress.setSizePolicy(sizePolicy)
        self.DownloadProgress.setValue(0)
        self.DownloadProgress.setTextVisible(False)
        self.DownloadProgress.setOrientation(Qt.Orientation.Horizontal)
        self.DownloadProgress.setTextDirection(QProgressBar.Direction.TopToBottom)

        self.gridLayout_5.addWidget(self.DownloadProgress, 1, 0, 1, 1)

        self.ConvertButton = QPushButton(self.ActionsGroupBox)
        self.ConvertButton.setObjectName(u"ConvertButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ConvertButton.sizePolicy().hasHeightForWidth())
        self.ConvertButton.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.ConvertButton, 1, 1, 1, 1)


        self.gridLayout_2.addWidget(self.ActionsGroupBox, 3, 0, 1, 1)

        self.TopLayout = QGridLayout()
        self.TopLayout.setObjectName(u"TopLayout")
        self.Title = QLabel(self.MainLayout)
        self.Title.setObjectName(u"Title")
        font = QFont()
        font.setFamilies([u"Segoe UI Historic"])
        font.setPointSize(10)
        self.Title.setFont(font)

        self.TopLayout.addWidget(self.Title, 0, 1, 1, 2)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label = QLabel(self.MainLayout)
        self.label.setObjectName(u"label")

        self.gridLayout_7.addWidget(self.label, 0, 0, 1, 1)


        self.TopLayout.addLayout(self.gridLayout_7, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.TopLayout, 0, 0, 1, 1)

        self.FooterLabelWidget = QLabel(self.MainLayout)
        self.FooterLabelWidget.setObjectName(u"FooterLabelWidget")

        self.gridLayout_2.addWidget(self.FooterLabelWidget, 5, 0, 1, 1)

        self.PathOptionGroupBox = QGroupBox(self.MainLayout)
        self.PathOptionGroupBox.setObjectName(u"PathOptionGroupBox")
        self.gridLayout_6 = QGridLayout(self.PathOptionGroupBox)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.PathButton = QPushButton(self.PathOptionGroupBox)
        self.PathButton.setObjectName(u"PathButton")
        sizePolicy1.setHeightForWidth(self.PathButton.sizePolicy().hasHeightForWidth())
        self.PathButton.setSizePolicy(sizePolicy1)

        self.gridLayout_6.addWidget(self.PathButton, 0, 1, 1, 1)

        self.PathLineEdit = QLineEdit(self.PathOptionGroupBox)
        self.PathLineEdit.setObjectName(u"PathLineEdit")
        self.PathLineEdit.setEnabled(False)
        sizePolicy.setHeightForWidth(self.PathLineEdit.sizePolicy().hasHeightForWidth())
        self.PathLineEdit.setSizePolicy(sizePolicy)

        self.gridLayout_6.addWidget(self.PathLineEdit, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.PathOptionGroupBox, 2, 0, 1, 1)

        self.DataGroupBox = QGroupBox(self.MainLayout)
        self.DataGroupBox.setObjectName(u"DataGroupBox")
        self.gridLayout = QGridLayout(self.DataGroupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.UrlTextInput = QLineEdit(self.DataGroupBox)
        self.UrlTextInput.setObjectName(u"UrlTextInput")
        sizePolicy.setHeightForWidth(self.UrlTextInput.sizePolicy().hasHeightForWidth())
        self.UrlTextInput.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.UrlTextInput, 0, 1, 1, 1)

        self.MediaTypeComboBox = QComboBox(self.DataGroupBox)
        self.MediaTypeComboBox.addItem("")
        self.MediaTypeComboBox.addItem("")
        self.MediaTypeComboBox.setObjectName(u"MediaTypeComboBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.MediaTypeComboBox.sizePolicy().hasHeightForWidth())
        self.MediaTypeComboBox.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.MediaTypeComboBox, 0, 2, 1, 1)


        self.gridLayout_2.addWidget(self.DataGroupBox, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.MainLayout)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Dandilion", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.LogsOutputBox.setTitle(QCoreApplication.translate("MainWindow", u"Logs", None))
        self.ActionsGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Actions", None))
        self.ConvertButton.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
        self.Title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt;\">Dandilion</span></p><p>Cross-platform open-source desktop application that converts YouTube links into various media formats, including audio and video. </p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icons/assets/icons8-dandelion-100.png\"/></p></body></html>", None))
        self.FooterLabelWidget.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">\u00a9 2025 Dandilion. All rights reserved. This project is open-source and licensed under the GNU General Public License v3.0. </span></p></body></html>", None))
        self.PathOptionGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Path", None))
        self.PathButton.setText(QCoreApplication.translate("MainWindow", u"Path", None))
        self.DataGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Inputs", None))
        self.MediaTypeComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"MP3", None))
        self.MediaTypeComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"MP4", None))

    # retranslateUi

