# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QMainWindow

from ui_mainwindow import Ui_MainWindow

class dashWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

# if __name__ == "__main__":
#     pass
