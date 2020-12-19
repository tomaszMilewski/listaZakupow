import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QVBoxLayout, QScrollArea, QLineEdit, \
    QPushButton, QMainWindow, QTabWidget

from JsonReader import JsonReader
from ProductLists import ProductLists
from ProductsEditor import ProductsEditor


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Lista zakupów')
        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)
        self.show()


class MyTableWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        self.tabs = QTabWidget()
        self.tab1 = ProductsEditor()
        self.tab2 = ProductLists()

        self.tabs.addTab(self.tab1, "Baza produktów")
        self.tabs.addTab(self.tab2, "Listy zakupów")

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())