# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'createCards.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHeaderView, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpinBox, QStatusBar,
    QTableView, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1282, 742)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.buttonSend = QPushButton(self.centralwidget)
        self.buttonSend.setObjectName(u"buttonSend")
        self.buttonSend.setGeometry(QRect(280, 650, 93, 29))
        self.comboCollection = QComboBox(self.centralwidget)
        self.comboCollection.setObjectName(u"comboCollection")
        self.comboCollection.setGeometry(QRect(330, 90, 271, 26))
        self.comboCards = QComboBox(self.centralwidget)
        self.comboCards.setObjectName(u"comboCards")
        self.comboCards.setGeometry(QRect(640, 90, 271, 26))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(330, 60, 81, 20))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(640, 60, 63, 20))
        self.listProps = QListWidget(self.centralwidget)
        self.listProps.setObjectName(u"listProps")
        self.listProps.setGeometry(QRect(100, 160, 201, 111))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(460, 160, 81, 20))
        self.comboQlty = QComboBox(self.centralwidget)
        self.comboQlty.setObjectName(u"comboQlty")
        self.comboQlty.setGeometry(QRect(460, 200, 151, 26))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(650, 160, 63, 20))
        self.comboLang = QComboBox(self.centralwidget)
        self.comboLang.setObjectName(u"comboLang")
        self.comboLang.setGeometry(QRect(640, 200, 161, 26))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(340, 160, 91, 20))
        self.spinQnt = QSpinBox(self.centralwidget)
        self.spinQnt.setObjectName(u"spinQnt")
        self.spinQnt.setGeometry(QRect(340, 190, 51, 26))
        self.tableAdd = QTableView(self.centralwidget)
        self.tableAdd.setObjectName(u"tableAdd")
        self.tableAdd.setGeometry(QRect(60, 330, 1191, 301))
        self.cardPreview = QLabel(self.centralwidget)
        self.cardPreview.setObjectName(u"cardPreview")
        self.cardPreview.setGeometry(QRect(1000, 20, 241, 261))
        self.buttonSave = QPushButton(self.centralwidget)
        self.buttonSave.setObjectName(u"buttonSave")
        self.buttonSave.setGeometry(QRect(730, 650, 93, 29))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(100, 60, 63, 20))
        self.comboBloco = QComboBox(self.centralwidget)
        self.comboBloco.setObjectName(u"comboBloco")
        self.comboBloco.setGeometry(QRect(100, 90, 201, 26))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1282, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.buttonSend.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Cole\u00e7\u00f5es", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Carta", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Qualidade", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Idioma", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None))
        self.cardPreview.setText("")
        self.buttonSave.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Bloco", None))
    # retranslateUi

