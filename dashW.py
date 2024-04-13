# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QWidget, QTabWidget, QLabel, QStackedWidget, QPushButton
from PySide6.QtCore import QPropertyAnimation, QEasingCurve

from ui_dashW import Ui_centralWidget
from showCards import showCards

# if __name__ == "__main__":
#     pass

class dashW():
    def __init__(self):
        self.widget2 = QWidget()
        self.ui_widget2 = Ui_centralWidget()
        self.ui_widget2.setupUi(self.widget2)

        self.tabWidget = self.widget2.findChild(QTabWidget, "tabWidget")
        self.tabWidget.setTabText(0, "Valor Acumulado")
        self.tabWidget.setTabText(1, "Carta Maior Valor")

        '''
            -Verificar como pode ser feita a adição de eventos no QCalendarWidget.
            -Verificar como obter o dia selecionado no QCalendarWidget.
            -Verificar como mostrar os eventos que foram adicionados quando clicar na data.
        '''
        self.tabWidget.setTabText(2, "Eventos")

        self.total_value = self.widget2.findChild(QLabel, "totalValue")
        self.total_value.setText("R$0,00")

        self.total_value = self.widget2.findChild(QLabel, "cardValue")
        self.total_value.setText("R$0,00")

        self.button = self.widget2.findChild(QPushButton, "pushButton")
        self.button.clicked.connect(self.troca_widget)

    def troca_widget(self):
        self.widget3 = showCards()
        self.widget2.setCentralWidget(self.widget3)

