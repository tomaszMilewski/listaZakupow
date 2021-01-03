from PyQt5.QtWidgets import QVBoxLayout, QWidget, QTabWidget

from CreateNewList import CreateNewList


class ProductLists(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        super().__init__()
        self.tabsList = []
        self.layout = QVBoxLayout(self)

        self.tabs = QTabWidget()

        self.tabsList.append(QWidget())
        self.tabsList.append(QWidget())
        self.tabsList.append(QWidget())
        self.tabsList.append(CreateNewList())

        for index, tab in enumerate(self.tabsList):
            if (index < len(self.tabsList) - 1):
                self.tabs.addTab(tab, f'Lista {index}')
            else:
                self.tabs.addTab(tab, '+')

        self.tabs.currentChanged.connect(self.onChange)

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def onChange(self, i):
        print(i)
