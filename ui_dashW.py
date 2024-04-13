# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashW.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QLabel, QPushButton,
    QSizePolicy, QTabWidget, QWidget)

class Ui_centralWidget(object):
    def setupUi(self, centralWidget):
        if not centralWidget.objectName():
            centralWidget.setObjectName(u"centralWidget")
        centralWidget.resize(1105, 726)
        self.tabWidget = QTabWidget(centralWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(110, 100, 411, 271))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.totalValue = QLabel(self.tab)
        self.totalValue.setObjectName(u"totalValue")
        self.totalValue.setGeometry(QRect(10, 50, 291, 101))
        font = QFont()
        font.setPointSize(28)
        self.totalValue.setFont(font)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.cardValue = QLabel(self.tab_2)
        self.cardValue.setObjectName(u"cardValue")
        self.cardValue.setGeometry(QRect(10, 60, 291, 101))
        self.cardValue.setFont(font)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.calendarWidget = QCalendarWidget(self.tab_3)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(5, -1, 392, 236))
        self.tabWidget.addTab(self.tab_3, "")
        self.pushButton = QPushButton(centralWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(500, 580, 93, 29))

        self.retranslateUi(centralWidget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(centralWidget)
    # setupUi

    def retranslateUi(self, centralWidget):
        centralWidget.setWindowTitle(QCoreApplication.translate("centralWidget", u"Form", None))
        self.totalValue.setText(QCoreApplication.translate("centralWidget", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("centralWidget", u"Tab 1", None))
        self.cardValue.setText(QCoreApplication.translate("centralWidget", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("centralWidget", u"Tab 2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("centralWidget", u"Page", None))
        self.pushButton.setText(QCoreApplication.translate("centralWidget", u"TESTE", None))
    # retranslateUi

