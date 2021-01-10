from PyQt5.QtWidgets import QVBoxLayout, QWidget, QTabWidget

from CreateNewList import CreateNewList
from DisplayList import DisplayList
from JsonReader import JsonReader


class ProductLists(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        super().__init__()
        self.tabsList = []
        self.layout = QVBoxLayout(self)
        self.reader = JsonReader()
        self.tabs = QTabWidget()
        self.addTabs()
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def addTabs(self):
        self.lists = self.reader.readLists()

        for list in self.lists:
            self.tabsList.append(DisplayList(list))

        self.tabsList.append(CreateNewList(self.reloadList))

        for index, tab in enumerate(self.tabsList):
            if (index < len(self.tabsList) - 1):
                self.tabs.addTab(tab, f'{self.lists[index]["list_name"]}')
            else:
                self.tabs.addTab(tab, '+')

    def reloadList(self):
        self.lists = self.reader.readLists()
        list = self.lists[self.tabs.count() - 1]
        self.tabs.addTab(DisplayList(list), f'{list["list_name"]}')