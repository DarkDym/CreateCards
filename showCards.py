# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QLabel, QWidget, QFormLayout

from ui_showCards import Ui_centralWidget

# if __name__ == "__main__":
#     pass

class showCards():
    def __init__(self):

        '''
            Preciso contar a quantidade de Blocos que existem.
            Posso obter essa informação via classe Sets(PC de casa).

            Após ter a informação da quantidades de blocos, adicionar
            a quantidade equivalente de labels, com os seus respectivos
            logos.

            Replicar a ideia acima para os sets de cada um do blocos.

            Talvez verificar a possibilidade de adicionar botões ao invés
            de labels. Somente para que seja possível adicionar as funções
            de clique em cada bloco/set.

            Fazer a função que avalia o set que foi clicado, para assim gerar
            os label/botões dos subsets.

            Colocar o QStackedWidget para testar a animação de troca entre os
            widgets associados aos blocos/sets.
        '''

        self.widget = QWidget()
        self.ui_widget = Ui_centralWidget()
        self.ui_widget.setupUi(self.widget)

        self.sets = { 'set' : [
                        {'name' : 't1','subset' : ['st1_1','st1_2','st1_3']},
                        {'name' : 't2','subset' : ['st2_1','st2_2','st2_3']},
                        {'name' : 't3','subset' : ['st3_1','st3_2','st3_3']}
                    ]}

        self.formLayout = self.widget.findChild(QFormLayout, "formLayout")

        for key, value in self.sets['set']:
            label = QLabel(f"{key}: {value}")
            self.formLayout.addWidget(label)


