from PyQt5.QtWidgets import QWidget, QVBoxLayout, QScrollArea, QGridLayout, QLabel, QLineEdit, QPushButton

from JsonReader import JsonReader


class ProductsEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 600, 600)
        self.setFixedSize(600, 600)

        self.layout = QVBoxLayout(self)
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.layout.addWidget(self.scrollArea)

        self.reader = JsonReader()

        idLabel = QLabel('Id', self)
        nameLabel = QLabel('Nazwa', self)
        priceLabel = QLabel('Cena', self)
        imageLabel = QLabel('Obrazek', self)
        actionLabel = QLabel('Akcja', self)

        self.gridLayout.addWidget(idLabel, 0, 0, 1, 1)
        self.gridLayout.addWidget(nameLabel, 0, 1, 1, 1)
        self.gridLayout.addWidget(priceLabel, 0, 2, 1, 1)
        self.gridLayout.addWidget(imageLabel, 0, 3, 1, 1)
        self.gridLayout.addWidget(actionLabel, 0, 4, 1, 1)

        self.products = self.reader.readProducts()
        for item in self.products:
            print(item)
            position = self.products.index(item) + 1
            self.addNewProduct(str(item['id']), str(item['name']), str(item['price']), str(item['image']), position)

        self.newID = QLineEdit()
        self.newName = QLineEdit()
        self.newPrice = QLineEdit()
        self.newImage = QLineEdit()
        self.buttonAdd = QPushButton('+', self)
        self.buttonAdd.setMaximumWidth(25)
        self.buttonAdd.setMaximumHeight(25)
        self.buttonAdd.clicked.connect(self.addProduct)

        self.gridLayout.addWidget(self.newID, len(self.products) + 2, 0)
        self.gridLayout.addWidget(self.newName, len(self.products) + 2, 1)
        self.gridLayout.addWidget(self.newPrice, len(self.products) + 2, 2)
        self.gridLayout.addWidget(self.newImage, len(self.products) + 2, 3)
        self.gridLayout.addWidget(self.buttonAdd, len(self.products) + 2, 4)
        self.show()

    def addNewProduct(self, id, name, price, image, position):
        idValueLabel = QLabel(id, self)
        nameValueLabel = QLabel(name, self)
        priceValueLabel = QLabel(price, self)
        imageValueLabel = QLabel(image, self)
        buttonRemove = QPushButton('-', self)
        buttonRemove.setMaximumWidth(25)
        buttonRemove.setMaximumHeight(25)
        buttonRemove.clicked.connect(
            lambda: self.removeProduct(idValueLabel))

        if (position % 2 == 0):
            idValueLabel.setStyleSheet("background: gray")
            nameValueLabel.setStyleSheet("background: gray")
            priceValueLabel.setStyleSheet("background: gray")
            imageValueLabel.setStyleSheet("background: gray")

        self.gridLayout.addWidget(idValueLabel, position, 0)
        self.gridLayout.addWidget(nameValueLabel, position, 1)
        self.gridLayout.addWidget(priceValueLabel, position, 2)
        self.gridLayout.addWidget(imageValueLabel, position, 3)
        self.gridLayout.addWidget(buttonRemove, position, 4)

    def removeProduct(self, buttonRemove):
        for i in reversed(range(self.gridLayout.count())):
            if self.gridLayout.itemAt(i).widget() == buttonRemove:
                for x in range(0, 5):
                    self.gridLayout.itemAt(i).widget().setParent(None)

    def addProduct(self):
        self.reader.addSingleProduct(self.newID.text(), self.newName.text(), self.newPrice.text(), self.newImage.text())
        self.products = self.reader.readProducts()
        self.addNewProduct(self.newID.text(), self.newName.text(), self.newPrice.text(), self.newImage.text(),
                           len(self.products))
        self.gridLayout.removeWidget(self.newID)
        self.gridLayout.removeWidget(self.newName)
        self.gridLayout.removeWidget(self.newPrice)
        self.gridLayout.removeWidget(self.newImage)
        self.gridLayout.removeWidget(self.buttonAdd)

        self.gridLayout.addWidget(self.newID, len(self.products) + 2, 0)
        self.gridLayout.addWidget(self.newName, len(self.products) + 2, 1)
        self.gridLayout.addWidget(self.newPrice, len(self.products) + 2, 2)
        self.gridLayout.addWidget(self.newImage, len(self.products) + 2, 3)
        self.gridLayout.addWidget(self.buttonAdd, len(self.products) + 2, 4)
