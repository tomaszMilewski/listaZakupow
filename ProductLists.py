from PyQt5.QtWidgets import QVBoxLayout, QWidget, QTabWidget


class ProductLists(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        super().__init__()
        self.setGeometry(0, 0, 600, 600)
        self.setFixedSize(600, 600)
        self.layout = QVBoxLayout(self)

        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()

        self.tabs.addTab(self.tab1, "Lista 1")
        self.tabs.addTab(self.tab2, "Lista 2")

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)


