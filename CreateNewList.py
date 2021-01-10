from PyQt5.QtGui import QValidator, QDoubleValidator
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QScrollArea, QGridLayout, QLabel, QLineEdit, QPushButton, QCompleter, \
    QMessageBox, QDialog
from PyQt5 import QtCore

from JsonReader import JsonReader


class CreateNewList(QWidget):
    def __init__(self, reloadLists):
        super().__init__()
        self.initUI()
        self.productsToAdd = []
        self.reloadLists = reloadLists

    def initUI(self):
        self.setGeometry(0, 0, 600, 600)
        self.setFixedSize(600, 600)

        self.reader = JsonReader()
        self.products = self.reader.readProducts()
        self.productNames = map(lambda item: item['name'], self.products)

        self.layout = QVBoxLayout(self)
        self.scrollArea = QScrollArea(self)
        self.titleBox = QScrollArea(self)
        #self.titleContainer = QWidget(self.titleBox)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setMaximumHeight(50)
        self.titleBox.setFixedHeight(30)
        self.scrollAreaWidgetContents = QWidget()
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridTitle = QGridLayout(self.titleBox)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.layout.setSpacing(1)
        self.layout.addWidget(self.titleBox)
        self.layout.addWidget(self.scrollArea)






        self.listItems = []

        nameLabel = QLabel('Nazwa', self)
        amountLabel = QLabel('Ilosc', self)
        buttonLabel = QLabel('Akcja', self)

        nameLabel.setFixedWidth(250)
        amountLabel.setFixedWidth(250)
        buttonLabel.setFixedWidth(30)

        self.gridTitle.addWidget(nameLabel, 0, 0, 1, 1)
        nameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.gridTitle.addWidget(amountLabel, 0, 1, 1, 1)
        amountLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.gridTitle.addWidget(buttonLabel, 0, 2, 1, 1)
        buttonLabel.setAlignment(QtCore.Qt.AlignCenter)


        self.addInputFields(1)
        self.addSaveButton()

        self.show()

    def addSaveButton(self):
        self.buttonSave = QPushButton('Create New List', self)
        self.layout.addWidget(self.buttonSave, alignment=QtCore.Qt.AlignTop)
        self.buttonSave.clicked.connect(self.showDialog)
        self.buttonSave.setFixedWidth(100)

    def showDialog(self):
        self.dialog = QDialog()
        self.dialog.setFixedSize(200, 100)
        self.listName = QLineEdit(self.dialog)
        buttonOk = QPushButton('Ok', self.dialog)
        buttonCancel = QPushButton('Anuluj', self.dialog)
        self.listName.move(20,20)
        buttonOk.move(10, 70)
        buttonCancel.move(100,70)
        buttonOk.clicked.connect(self.confirm)
        buttonCancel.clicked.connect(self.cancel)
        self.dialog.setWindowTitle('Wpisz nazwe listy')
        self.dialog.exec_()

    def confirm(self):
        self.dialog.reject()
        listName = self.listName.text()
        self.reader.addSingleList(listName, self.productsToAdd)
        self.reloadLists()

    def cancel(self):
        self.dialog.reject()

    def addInputFields(self, position):
        self.newName = QLineEdit()
        self.newAmount = QLineEdit()
        self.newAmount.setValidator(QDoubleValidator(999999, -999999, 8))
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
        if len(name) != 0 and len(amount) != 0:
            if self.scrollArea.height() < 500:
                self.scrollArea.setFixedHeight(self.scrollArea.height() + 30)
                self.scrollArea.setFixedHeight(self.scrollArea.height() + 30)


        if len(name) == 0 or len(amount) == 0:
            QMessageBox.question(self, 'Błąd', 'Musisz podac nazwę i ilość\n "Ilość" powinna być typu float',
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

        if self.scrollArea.height() >= 100 and self.scrollArea.verticalScrollBar().isVisible() == False:
            self.scrollArea.setFixedHeight(self.scrollArea.height() - 30)
           # self.buttonSave.move(10, self.scrollArea.height() + 10)


