# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AboutlSUTBE.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QSizePolicy, QWidget)

import app.resources.assets_rc as assets_rc

class Ui_About(object):
    def setupUi(self, About):
        if not About.objectName():
            About.setObjectName(u"About")
        About.resize(378, 120)
        font = QFont()
        font.setFamilies([u"Leelawadee"])
        About.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Icons/icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        About.setWindowIcon(icon)
        self.gridLayout = QGridLayout(About)
        self.gridLayout.setObjectName(u"gridLayout")
        self.AboutGrid = QGridLayout()
        self.AboutGrid.setObjectName(u"AboutGrid")
        self.InfoGrid = QGridLayout()
        self.InfoGrid.setObjectName(u"InfoGrid")
        self.TitleLabel = QLabel(About)
        self.TitleLabel.setObjectName(u"TitleLabel")

        self.InfoGrid.addWidget(self.TitleLabel, 0, 0, 1, 1)

        self.DescriptionLabel = QLabel(About)
        self.DescriptionLabel.setObjectName(u"DescriptionLabel")

        self.InfoGrid.addWidget(self.DescriptionLabel, 1, 0, 1, 1)


        self.AboutGrid.addLayout(self.InfoGrid, 0, 2, 1, 1)

        self.AboutIcon = QLabel(About)
        self.AboutIcon.setObjectName(u"AboutIcon")

        self.AboutGrid.addWidget(self.AboutIcon, 0, 0, 1, 1)

        self.line = QFrame(About)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.AboutGrid.addWidget(self.line, 0, 1, 1, 1)

        self.AboutGrid.setColumnStretch(0, 1)
        self.AboutGrid.setColumnStretch(1, 4)
        self.AboutGrid.setColumnStretch(2, 3)

        self.gridLayout.addLayout(self.AboutGrid, 0, 0, 1, 1)


        self.retranslateUi(About)

        QMetaObject.connectSlotsByName(About)
    # setupUi

    def retranslateUi(self, About):
        About.setWindowTitle(QCoreApplication.translate("About", u"About", None))
        self.TitleLabel.setText(QCoreApplication.translate("About", u"<html><head/><body><p><span style=\" font-size:14pt;\">Dandilion</span></p></body></html>", None))
        self.DescriptionLabel.setText(QCoreApplication.translate("About", u"<html><head/><body><p><span style=\" font-size:10pt;\">Open Source Youtube Media Downloader<br/>Kyle Myre \u00a9 2024 GNU PUBLIC LICENSE</span></p></body></html>", None))
        self.AboutIcon.setText(QCoreApplication.translate("About", u"<html><head/><body><p align=\"center\"><img src=\":/Icons/icon.ico\"/></p></body></html>", None))
    # retranslateUi

