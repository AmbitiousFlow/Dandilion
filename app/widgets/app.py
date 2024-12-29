# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AppZbGPLm.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QLabel, QLineEdit, QMainWindow, QPlainTextEdit,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

import app.resources.assets_rc as assets_rc

class Ui_Dandilion(object):
    def setupUi(self, Dandilion):
        if not Dandilion.objectName():
            Dandilion.setObjectName(u"Dandilion")
        Dandilion.setEnabled(True)
        Dandilion.resize(822, 337)
        font = QFont()
        font.setFamilies([u"Leelawadee"])
        font.setBold(False)
        font.setItalic(False)
        Dandilion.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Icons/icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Dandilion.setWindowIcon(icon)
        self.actionAbout = QAction(Dandilion)
        self.actionAbout.setObjectName(u"actionAbout")
        self.MainGrid = QWidget(Dandilion)
        self.MainGrid.setObjectName(u"MainGrid")
        self.MainGrid.setEnabled(True)
        self.gridLayout_2 = QGridLayout(self.MainGrid)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.TitleLabel = QLabel(self.MainGrid)
        self.TitleLabel.setObjectName(u"TitleLabel")

        self.verticalLayout.addWidget(self.TitleLabel)

        self.VerticalSpacerTools = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.VerticalSpacerTools)

        self.GithubButton = QPushButton(self.MainGrid)
        self.GithubButton.setObjectName(u"GithubButton")
        self.GithubButton.setAutoDefault(False)
        self.GithubButton.setFlat(False)

        self.verticalLayout.addWidget(self.GithubButton)

        self.WikiButton = QPushButton(self.MainGrid)
        self.WikiButton.setObjectName(u"WikiButton")

        self.verticalLayout.addWidget(self.WikiButton)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.spacer = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.spacer, 0, 2, 1, 1)

        self.InputGridSection = QGridLayout()
        self.InputGridSection.setSpacing(6)
        self.InputGridSection.setObjectName(u"InputGridSection")
        self.UrlLabel = QLabel(self.MainGrid)
        self.UrlLabel.setObjectName(u"UrlLabel")

        self.InputGridSection.addWidget(self.UrlLabel, 0, 0, 1, 1)

        self.TypeComboBox = QComboBox(self.MainGrid)
        self.TypeComboBox.addItem("")
        self.TypeComboBox.addItem("")
        self.TypeComboBox.addItem("")
        self.TypeComboBox.addItem("")
        self.TypeComboBox.addItem("")
        self.TypeComboBox.setObjectName(u"TypeComboBox")
        self.TypeComboBox.setEditable(False)

        self.InputGridSection.addWidget(self.TypeComboBox, 1, 1, 1, 3)

        self.DownloadButton = QPushButton(self.MainGrid)
        self.DownloadButton.setObjectName(u"DownloadButton")

        self.InputGridSection.addWidget(self.DownloadButton, 5, 3, 1, 1)

        self.TypeLabel = QLabel(self.MainGrid)
        self.TypeLabel.setObjectName(u"TypeLabel")

        self.InputGridSection.addWidget(self.TypeLabel, 1, 0, 1, 1)

        self.UrlEntry = QLineEdit(self.MainGrid)
        self.UrlEntry.setObjectName(u"UrlEntry")

        self.InputGridSection.addWidget(self.UrlEntry, 0, 1, 1, 3)

        self.DownloadProgressBar = QProgressBar(self.MainGrid)
        self.DownloadProgressBar.setObjectName(u"DownloadProgressBar")
        self.DownloadProgressBar.setEnabled(True)
        self.DownloadProgressBar.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.DownloadProgressBar.setValue(0)
        self.DownloadProgressBar.setTextVisible(True)
        self.DownloadProgressBar.setInvertedAppearance(False)

        self.InputGridSection.addWidget(self.DownloadProgressBar, 5, 0, 1, 3)

        self.OutputAreaBox = QPlainTextEdit(self.MainGrid)
        self.OutputAreaBox.setObjectName(u"OutputAreaBox")
        self.OutputAreaBox.setEnabled(True)
        self.OutputAreaBox.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByKeyboard|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.InputGridSection.addWidget(self.OutputAreaBox, 2, 0, 1, 4)

        self.InputGridSection.setColumnStretch(0, 1)
        self.InputGridSection.setColumnStretch(1, 2)
        self.InputGridSection.setColumnStretch(2, 10)

        self.gridLayout_2.addLayout(self.InputGridSection, 0, 4, 1, 1)

        self.seperator = QFrame(self.MainGrid)
        self.seperator.setObjectName(u"seperator")
        self.seperator.setFrameShape(QFrame.Shape.VLine)
        self.seperator.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.seperator, 0, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        Dandilion.setCentralWidget(self.MainGrid)
        self.statusbar = QStatusBar(Dandilion)
        self.statusbar.setObjectName(u"statusbar")
        Dandilion.setStatusBar(self.statusbar)

        self.retranslateUi(Dandilion)

        self.GithubButton.setDefault(False)


        QMetaObject.connectSlotsByName(Dandilion)
    # setupUi

    def retranslateUi(self, Dandilion):
        Dandilion.setWindowTitle(QCoreApplication.translate("Dandilion", u"Dandilion", None))
        self.actionAbout.setText(QCoreApplication.translate("Dandilion", u"About", None))
        self.TitleLabel.setText(QCoreApplication.translate("Dandilion", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:700;\">Dandilion</span></p></body></html>", None))
        self.GithubButton.setText(QCoreApplication.translate("Dandilion", u"Github", None))
        self.WikiButton.setText(QCoreApplication.translate("Dandilion", u"About", None))
        self.UrlLabel.setText(QCoreApplication.translate("Dandilion", u"<html><head/><body><p align=\"center\">URL</p></body></html>", None))
        self.TypeComboBox.setItemText(0, QCoreApplication.translate("Dandilion", u"MP3", None))
        self.TypeComboBox.setItemText(1, QCoreApplication.translate("Dandilion", u"MP4", None))
        self.TypeComboBox.setItemText(2, QCoreApplication.translate("Dandilion", u"WEBM", None))
        self.TypeComboBox.setItemText(3, QCoreApplication.translate("Dandilion", u"OGG", None))
        self.TypeComboBox.setItemText(4, QCoreApplication.translate("Dandilion", u"WAV", None))

        self.DownloadButton.setText(QCoreApplication.translate("Dandilion", u"Download", None))
        self.TypeLabel.setText(QCoreApplication.translate("Dandilion", u"<html><head/><body><p align=\"center\">Type</p></body></html>", None))
        self.OutputAreaBox.setPlainText("")
    # retranslateUi

