from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QScrollArea, QGridLayout, QLabel, QPushButton, QMessageBox

from JsonReader import JsonReader


class DisplayList(QWidget):
    def __init__(self, list):
        super().__init__()
        self.initUI(list)

    def initUI(self, list):
        self.setGeometry(0, 0, 600, 600)
        self.setFixedSize(600, 600)
        self.reader = JsonReader()
        self.products = self.reader.readProducts()

        self.layout = QVBoxLayout(self)
        self.scrollArea = QScrollArea(self)
        self.titleBox = QScrollArea(self)
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

        for item in list["products"]:
            self.addProduct(item)

        self.show()

    def findProduct(self, name):
        for product in self.products:
            if product["name"] == name:
                return product
        return 0

    def addProduct(self, item):
        counter = 0
        productResult = self.findProduct(item["name"])
        if productResult:
            nameValueLabel = QLabel(productResult["name"], self)
            amountValueLabel = QLabel(item["amount"], self)
            self.gridLayout.addWidget(nameValueLabel, counter + 1, 0)
            self.gridLayout.addWidget(amountValueLabel, counter + 1, 1)
            counter += 1




