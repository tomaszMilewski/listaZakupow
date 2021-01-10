from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QScrollArea, QGridLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, \
    QMessageBox

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
        self.titleBox = QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.titleBox.setFixedHeight(30)
        self.scrollAreaWidgetContents = QWidget()
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridTitle = QGridLayout(self.titleBox)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.layout.addWidget(self.titleBox)
        self.layout.addWidget(self.scrollArea)

        self.reader = JsonReader()
        print(f'Size test: {self.titleBox.width()}')
        size = (self.titleBox.width()*5 - 20)/4
        idLabel = QLabel('Id', self)
        idLabel.setFixedWidth(size)
        nameLabel = QLabel('Nazwa', self)
        nameLabel.setFixedWidth(size)
        priceLabel = QLabel('Cena', self)
        priceLabel.setFixedWidth(size)
        imageLabel = QLabel('Obrazek', self)
        priceLabel.setFixedWidth(size)
        actionLabel = QLabel('Akcja', self)
        actionLabel.setFixedWidth(40)

        self.gridTitle.addWidget(idLabel, 0, 0, 1 ,1)
        self.gridTitle.addWidget(nameLabel, 0, 1, 1 ,1)
        self.gridTitle.addWidget(priceLabel, 0, 2, 1 ,1)
        self.gridTitle.addWidget(imageLabel, 0, 3, 1 ,1)
        self.gridTitle.addWidget(actionLabel, 0, 4, 1 ,1)

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
        self.gridLayout.addWidget(self.newPrice, len(self.products) + 2, 2)


        self.gridLayout.addWidget(self.newName, len(self.products) + 2, 1)
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
            lambda: self.removeProduct(idValueLabel, position))

        if (position % 2 == 0):
            idValueLabel.setStyleSheet("background: gray")
            nameValueLabel.setStyleSheet("background: gray")
            priceValueLabel.setStyleSheet("background: gray")
            imageValueLabel.setStyleSheet("background: gray")

        pixmap = QPixmap(f'foto/{image}.png')
        imageValueLabel.setFixedSize(50, 50)
        imageValueLabel.setScaledContents(True)
        pixmap.scaled(50, 50)
        imageValueLabel.setPixmap(pixmap)

        self.gridLayout.addWidget(idValueLabel, position, 0)
        self.gridLayout.addWidget(nameValueLabel, position, 1)
        self.gridLayout.addWidget(priceValueLabel, position, 2)
        self.gridLayout.addWidget(imageValueLabel, position, 3)
        self.gridLayout.addWidget(buttonRemove, position, 4)

    def removeProduct(self, buttonRemove, position):
        for i in reversed(range(self.gridLayout.count())):
            if self.gridLayout.itemAt(i).widget() == buttonRemove:
                for x in range(0, 5):
                    self.gridLayout.itemAt(i).widget().setParent(None)
        products = self.reader.readProducts()
        products.pop(position - 1)
        self.reader.saveProducts(products)

    def addProduct(self):
        testVal = self.newID.text()
        control = False
        for x in self.products:
            exVal = x.get('id')
            if int(exVal) == int(testVal):
                control = True
                break
        try:

            if len(self.newName.text()) == 0 or self.newID.text() == 0 or self.newPrice.text() == 0:
                QMessageBox.question(self, 'Puste pola', '"ID", "Nazwa" oraz, "Cena" nie mogą być puste',
                                     QMessageBox.Yes)
            elif control == True:
                QMessageBox.question(self, 'Istniejace "ID"', f'"ID" :{self.newID.text()} juz istnieje',
                                     QMessageBox.Yes)
            else:
                self.reader.addSingleProduct(self.newID.text(), self.newName.text(), self.newPrice.text(),
                                             self.newImage.text())
                self.products = self.reader.readProducts()

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
        except ValueError:
            QMessageBox.question(self, 'Niepoprawny format', '"ID" - format int\n"Cena" - float',
                                 QMessageBox.Yes)