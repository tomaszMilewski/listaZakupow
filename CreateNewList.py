from PyQt5.QtWidgets import QWidget, QVBoxLayout, QScrollArea, QGridLayout, QLabel, QLineEdit, QPushButton, QCompleter, \
    QMessageBox
from PyQt5 import QtCore

from JsonReader import JsonReader


class CreateNewList(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.productsToAdd = []

    def initUI(self):
        self.setGeometry(0, 0, 600, 600)
        self.setFixedSize(600, 600)

        self.reader = JsonReader()
        self.products = self.reader.readProducts()
        self.productNames = map(lambda item: item['name'], self.products)

        self.layout = QVBoxLayout(self)
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.layout.addWidget(self.scrollArea)
        self.listItems = []

        nameLabel = QLabel('Nazwa', self)
        amountLabel = QLabel('Ilosc', self)
        buttonLabel = QLabel('Akcja', self)

        self.gridLayout.addWidget(nameLabel, 0, 0, alignment=QtCore.Qt.AlignTop)
        self.gridLayout.addWidget(amountLabel, 0, 1, alignment=QtCore.Qt.AlignTop)
        self.gridLayout.addWidget(buttonLabel, 0, 2, alignment=QtCore.Qt.AlignTop)

        self.addInputFields(1)
        self.addSaveButton()

        self.show()
    def addSaveButton(self):
        self.buttonSave = QPushButton('Create New List', self)
        self.buttonSave.clicked.connect(self.saveList)
        self.buttonSave.move(20, 520)

    def saveList(self):
        print(self.productsToAdd)

    def addInputFields(self, position):
        self.newName = QLineEdit()
        self.newAmount = QLineEdit()
        self.buttonAdd = QPushButton('+', self)
        self.buttonAdd.clicked.connect(
            lambda: self.addNewProduct(self.newName.text(), self.newAmount.text(), self.newName))
        self.buttonAdd.setMaximumWidth(25)
        self.buttonAdd.setMaximumHeight(25)

        autoComplete = QCompleter(self.productNames)
        print(self.productNames)
        self.newName.setCompleter(autoComplete)

        self.gridLayout.addWidget(self.newName, position, 0)
        self.gridLayout.addWidget(self.newAmount, position, 1)
        self.gridLayout.addWidget(self.buttonAdd, position, 2)

    def addNewProduct(self, name, amount, buttonAdd):
        if len(name) == 0 or len(amount) == 0:
            QMessageBox.question(self, 'Błąd', 'Musisz podac nazwę i ilość',
                                          QMessageBox.Yes)
            return


        self.productsToAdd.append({'name': name, 'amount': amount})
        print(len(self.productsToAdd))
        nameValueLabel = QLabel(name, self)
        amountValueLabel = QLabel(amount, self)
        buttonRemove = QPushButton('-', self)
        buttonRemove.setMaximumWidth(25)
        buttonRemove.setMaximumHeight(25)
        self.removeProduct(buttonAdd)
        buttonRemove.clicked.connect(
           lambda: self.removeProduct(nameValueLabel, len(self.productsToAdd)))

        self.gridLayout.addWidget(nameValueLabel, len(self.productsToAdd) + 1, 0)
        self.gridLayout.addWidget(amountValueLabel, len(self.productsToAdd) + 1, 1)
        self.gridLayout.addWidget(buttonRemove, len(self.productsToAdd) + 1, 2)
        self.addInputFields(len(self.productsToAdd) + 2)


    def removeProduct(self, buttonRemove, position = 0):
        for i in reversed(range(self.gridLayout.count())):
            if self.gridLayout.itemAt(i).widget() == buttonRemove:
                for x in range(0, 3):
                    self.gridLayout.itemAt(i).widget().setParent(None)
        if position != 0:
            self.productsToAdd.pop(position - 1)

