import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QVBoxLayout, QScrollArea, QLineEdit, QPushButton

from JsonReader import JsonReader


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 600, 600)
        self.setFixedSize(600, 600)
        self.resize(100, 100)

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

        self.gridLayout.addWidget(idLabel, 0, 0, 1, 1)
        self.gridLayout.addWidget(nameLabel, 0, 1, 1, 1)
        self.gridLayout.addWidget(priceLabel, 0, 2, 1, 1)
        self.gridLayout.addWidget(imageLabel, 0, 3, 1, 1)

        self.products = self.reader.readProducts()
        for item in self.products:
            print(item)
            index = self.products.index(item) + 1
            idValueLabel = QLabel(str(item['id']), self)
            nameValueLabel = QLabel(str(item['name']), self)
            priceValueLabel = QLabel(str(item['price']), self)
            imageValueLabel = QLabel(str(item['image']), self)
            buttonRemove = QPushButton('-', self)

            if (index % 2 == 0):
                idValueLabel.setStyleSheet("background: gray")
                nameValueLabel.setStyleSheet("background: gray")
                priceValueLabel.setStyleSheet("background: gray")
                imageValueLabel.setStyleSheet("background: gray")

            self.gridLayout.addWidget(idValueLabel, index, 0)
            self.gridLayout.addWidget(nameValueLabel, index, 1)
            self.gridLayout.addWidget(priceValueLabel, index, 2)
            self.gridLayout.addWidget(imageValueLabel, index, 3)
            self.gridLayout.addWidget(buttonRemove, index, 4)

        self.newID = QLineEdit()
        self.newName = QLineEdit()
        self.newPrice = QLineEdit()
        self.newImage = QLineEdit()
        self.buttonAdd = QPushButton('+', self)
        self.buttonAdd.clicked.connect(self.addProduct)

        self.gridLayout.addWidget(self.newID, len(self.products) + 2, 0)
        self.gridLayout.addWidget(self.newName, len(self.products) + 2, 1)
        self.gridLayout.addWidget(self.newPrice, len(self.products) + 2, 2)
        self.gridLayout.addWidget(self.newImage, len(self.products) + 2, 3)
        self.gridLayout.addWidget(self.buttonAdd, len(self.products) + 2, 4)
        self.show()

    def addProduct(self):
        self.reader.addSingleProduct(self.newID.text(), self.newName.text(), self.newPrice.text(), self.newImage.text())
        self.initUI()

def main():
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
