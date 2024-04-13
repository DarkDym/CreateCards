# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget, QMainWindow, QComboBox, QListWidget, QCheckBox, QListWidgetItem, QPushButton, QSpinBox, QTableView, QHeaderView
from PySide6.QtCore import Qt, QAbstractTableModel
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QStackedWidget, QLabel

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_createCards import Ui_MainWindow

from dashW import dashW
from AllSets import Sets

#class Sets():
#    def __init__(self):
#        print("Sets Initialized!")

#        '''
#            Esta classe tem que ser retirada deste arquivo, somente
#            ficará no outro arquivo.
#            Nesta parte, trocar todas os dicionários constantes, pelos
#            valores que vão ser carregados direto do outro arquivo
#            python (PC de Casa).
#        '''

#        self.list_props = {'props' : ['Foil','Promo','Pre Release','Reverse Foil','Staff']}
#        self.list_qlty = {'qlty' : ['NM','SP','MP','HP','D']}
#        self.list_lang = {'lang' : ['ENG','PTBR']}

#    def load_sets(self):
#        '''
#            Esta função vai ficar na inicialização da classe Sets do PC de Casa.
#            Tenho que construir um JSON com os blocos e os sets, para ser utilizado
#            nos ComboBox.
#        '''
#        self.sets = { 'set' : [
#                        {'name' : 't1','subset' : ['st1_1','st1_2','st1_3']},
#                        {'name' : 't2','subset' : ['st2_1','st2_2','st2_3']},
#                        {'name' : 't3','subset' : ['st3_1','st3_2','st3_3']}
#                    ]}
#        return self.sets

class ModeloTabela(QAbstractTableModel):
    def __init__(self, cabecalho,dados=None, parent=None):
        super().__init__(parent)
        self.dados = dados or []
        self.cabecalho = cabecalho

    def rowCount(self, parent):
        return len(self.dados)

    def columnCount(self, parent):
        return len(self.cabecalho)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # Verificar se o índice é válido
            if index.isValid() and 0 <= index.row() < len(self.dados):
                # Obter o dado correspondente ao índice
                dado = self.dados[index.row()]
                # Verificar se a coluna está dentro do intervalo
                if 0 <= index.column() < len(self.cabecalho):
                    # Obter o valor do dado para a coluna específica
                    valor = dado[self.cabecalho[index.column()]]
                    return str(valor)
        return None

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self.cabecalho[section])
            elif orientation == Qt.Vertical:  # Para mostrar os índices das linhas
                return str(section + 1)

'''
    Verificar como abrir a webcam e adicionar em algum widget (o melhor que tiver).
    Após ter a webcam aberta, desenvolver o código que pega a imagem, dentro de uma
    região pré-determinada.
    A região pré-determinada pode ser colocada no frame, possível utilizar o OpenCV
    para realizar essa modificação.
    Verificar técnicas de comparação de imagens, para comparar o logo da coleção com
    com o logo da carta.
    Fazer uma função númerica de comparação entre todos os possíveis logos de todas as
    coleções.
    Pesquisar a possíbilidade de extração de números da carta, para poder descobrir qual
    a carta que deve ser adicionada.
'''


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.cabecalhos = ["subset", "card", "props", "qnt", "qlty", "lang"]
        self.modelo_tabela = ModeloTabela(self.cabecalhos)

        self.s = Sets()
        self.list_sets = self.s.get_all_sets()
        self.t = self.s.adjust_sets_to_qt()

        self.lp = self.findChild(QListWidget, "listProps")

        for e in self.s.list_props['props']:
            novo_item = QListWidgetItem()
            self.checkbox = QCheckBox()
            self.checkbox.setText(e)
            self.checkbox.setStyleSheet("QCheckBox { margin-left: 5px; }")
            self.lp.addItem(novo_item)
            self.lp.setItemWidget(novo_item, self.checkbox)

        self.cqlty = self.findChild(QComboBox,"comboQlty")
        self.cqlty.addItem("Selecione uma opção")
        for e in self.s.list_qlty['qlty']:
            self.cqlty.addItem(e)

        self.clang = self.findChild(QComboBox,"comboLang")
        self.clang.addItem("Selecione uma opção")
        for e in self.s.list_lang['lang']:
            self.clang.addItem(e)


        self.ccard = self.findChild(QComboBox,"comboCards")
        self.ccard.setEnabled(False)

        self.cbloco = self.findChild(QComboBox, "comboBloco")
        self.cbloco.addItem("Selecione uma opção")
        print(self.t['set'])
        for e in self.t['set']:
            self.cbloco.addItem(e['name'])


        self.cc = self.findChild(QComboBox,"comboCollection")
        self.cc.setEnabled(False)


        self.ta = self.findChild(QTableView, "tableAdd")
        for coluna, chave in enumerate(self.cabecalhos):
            self.modelo_tabela.setHeaderData(coluna, Qt.Horizontal, chave)
        self.ta.setModel(self.modelo_tabela)
        self.ta.resizeColumnsToContents()
        self.ta.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.sqnt = self.findChild(QSpinBox, "spinQnt")

        self.cbloco.model().item(0).setEnabled(False)
        self.cbloco.model().item(0).setFlags(self.cbloco.model().item(0).flags() & ~Qt.ItemIsSelectable)


        self.cbloco.currentIndexChanged.connect(self.selecionou_bloco)
        self.cc.currentIndexChanged.connect(self.selecionou_item)
        self.ccard.currentIndexChanged.connect(self.find_image_from_selected_card)

        self.button_send = self.findChild(QPushButton,"buttonSend")
        self.button_send.clicked.connect(self.send_data)

        self.button_save = self.findChild(QPushButton, "buttonSave")
        self.button_save.clicked.connect(self.get_data_table)

    def change_to_widget2(self):

        #self.widget2 = QWidget()
        #self.ui_widget2 = Ui_centralWidget()
        #self.ui_widget2.setupUi(self.widget2)
        self.widget2 = dashW()
        self.setCentralWidget(self.widget2.widget2)

    def get_data_screen(self):

        itens_selecionados = []

        for i in range(self.lp.count()):
            item = self.lp.item(i)
            if item is not None:
                widget = self.lp.itemWidget(item)
                if isinstance(widget, QCheckBox) and widget.isChecked():
                    itens_selecionados.append(widget.text())
        if self.ccard.currentText() == None or self.ccard.currentText() == "":
            '''
                Ajustar para que se a carta não foi selecionada, irá aparecer
                uma janela dizendo que não foi possível fazer a adição na
                lista.
            '''
            print("Não foi selecionada uma carta para ser adicionada.")
        test = {'subset' : self.cc.currentText(),
                'card' : self.ccard.currentText(),
                'props' : itens_selecionados,
                'qnt' : self.sqnt.value(),
                'qlty' : self.cqlty.currentText(),
                'lang' : self.clang.currentText()}
        return test

    def get_data_table(self):
        '''
            Fazer a verificação se existe algum dado na tabela.
            Se não tiver nenhum dado, não abrir a segunda janela.
            Somente irá 'Salvar' as cartas, se alguma carta foi
            devidamente adicionada.
        '''
        table_data = self.modelo_tabela.dados
        self.change_to_widget2()
        return table_data

    def send_data(self):
        test = self.get_data_screen()

        self.modelo_tabela.beginInsertRows(self.ta.rootIndex(), len(self.modelo_tabela.dados), len(self.modelo_tabela.dados))
        self.modelo_tabela.dados.append(test)
        self.modelo_tabela.endInsertRows()
        self.ta.resizeColumnsToContents()
        self.ta.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        #self.cc.setCurrentIndex(0)
        self.cbloco.setCurrentIndex(0)
        self.cc.clear()
        self.cc.setEnabled(False)
        self.ccard.clear()
        self.ccard.setEnabled(False)
        self.clang.setCurrentIndex(0)
        self.cqlty.setCurrentIndex(0)
        self.cardP.clear()

        for row in range(self.lp.count()):
            item = self.lp.item(row)
            widget = self.lp.itemWidget(item)
            if widget.isChecked():
                widget.setChecked(False)

        self.sqnt.setValue(0)

    def find_image_from_selected_card(self):
        '''
            Nesta função, preciso ajustar para que após seja selecionado a carta
            no comboBox, seja buscado na pasta correta a imagem da carta e dispo-
            nibilizado no label.
        '''

        if self.ccard.currentText() != "Selecione uma opção":
            for e in self.allCards:
                [nome,num] = self.ccard.currentText().split("#")
                if (nome == e['name']) and (num == e['number']):
                    self.set_path = "C:/Users/Dymytry/Desktop/PCCA/" + str(self.adjust_name_special_char(e['set_series'])) + "/" + str(e['set_id']) + "/" + str(e['number']) + ".png"
            self.cardP = self.findChild(QLabel, "cardPreview")
            pixmap = QPixmap(self.set_path)
            #pixmap_scaled = pixmap.scaled(self.cardP.size(), aspectRatioMode=Qt.KeepAspectRatio)
            #pixmap_scaled = pixmap.scaledToWidth(self.cardP.width())
            #self.cardP.setText(self.ccard.currentText())
            self.cardP.setPixmap(pixmap)
            self.cardP.setScaledContents(True)

    def selecionou_bloco(self):
        if self.cbloco.currentText() != "Selecione uma opção":
            self.clear_combos()
            self.cc.setEnabled(True)

            self.cc.addItem("Selecione uma opção")
            print("##############################")
            print("##############################")
            print("##############################")
            for e in self.t['set']:
                print(e)
                if e['name'] == self.cbloco.currentText():
                    for f in e['subset']:
                        self.cc.addItem(f)

            self.cc.model().item(0).setEnabled(False)
            self.cc.model().item(0).setFlags(self.cc.model().item(0).flags() & ~Qt.ItemIsSelectable)

    def clear_combos(self):
        self.cc.clear()
        self.cc.setEnabled(False)
        self.ccard.clear()
        self.ccard.setEnabled(False)

    def adjust_name_special_char(self,text):
        return text.replace(' & ' , '_')

    def selecionou_item(self):
        item_selecionado = self.cc.currentText()
        print("!!!!!!!!!!!!!!!!!!!!")
        print(item_selecionado)
        print("!!!!!!!!!!!!!!!!!!!!")
        if item_selecionado != "Selecione uma opção":
            self.ccard.setEnabled(True)

            self.ccard.addItem("Selecione uma opção")

            self.allCards = self.s.return_cards_to_qt(item_selecionado)
            for c in self.allCards:
                if item_selecionado == c['set_id']:
                    self.ccard.addItem(c['name'] + "#" + c['number'])
            #for e in self.list_sets['set']:
            #    if item_selecionado == e['name']:
            #        for elem in e['subset']:
            #            self.ccard.addItem(elem)

            self.ccard.model().item(0).setEnabled(False)
            self.ccard.model().item(0).setFlags(self.ccard.model().item(0).flags() & ~Qt.ItemIsSelectable)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    main = MainWindow()
    main.show()
    sys.exit(app.exec())
