import sys
from PyQt5.uic import loadUi
from PyQt5 import QtGui
from PyQt5.QtWidgets import *

class QCustomQWidget(QWidget):
    def __init__ (self, parent = None):
        super(QCustomQWidget, self).__init__(parent)
        self.textQVBoxLayout =  QVBoxLayout()
        self.textUpQLabel    =  QLabel()
        self.textDownQLabel  =  QLabel()
        self.textQVBoxLayout.addWidget(self.textUpQLabel)
        self.textQVBoxLayout.addWidget(self.textDownQLabel)
        self.allQHBoxLayout  =  QHBoxLayout()
        self.iconQLabel      =  QLabel()
        self.allQHBoxLayout.addWidget(self.iconQLabel, 0)
        self.allQHBoxLayout.addLayout(self.textQVBoxLayout, 1)
        self.setLayout(self.allQHBoxLayout)
        # setStyleSheet
        self.textUpQLabel.setStyleSheet('''
            color: rgb(0, 0, 255);
        ''')
        self.textDownQLabel.setStyleSheet('''
            color: rgb(255, 0, 0);
        ''')

    def setTextUp (self, text):
        self.textUpQLabel.setText(text)

    def setTextDown (self, text):
        self.textDownQLabel.setText(text)

    def setIcon (self, imagePath):
        self.iconQLabel.setPixmap(QtGui.QPixmap(imagePath))

class exampleQMainWindow ( QMainWindow):
    def __init__ (self):
        super(exampleQMainWindow, self).__init__()
        # Create QListWidget
        self.myQListWidget =  QListWidget(self)
        for index, name, icon in [
            ('No.1', 'Meyoko',  'icon.png'),
            ('No.2', 'Nyaruko', 'icon.png'),
            ('No.3', 'Louise',  'icon.png')]:
            # Create QCustomQWidget
            itm = loadUi("CustomeItem.ui")
            itm.developer.setText(name)
            # itm.setTextUp(index)
            # itm.setTextDown(name)
            # itm.setIcon(icon)
            # Create QListWidgetteIm
            myQListWidgetItem =  QListWidgetItem(self.myQListWidget)
            # Set size hint
            myQListWidgetItem.setSizeHint( itm.sizeHint())
            # Add QListWidgetItem into QListWidget
            self.myQListWidget.addItem(myQListWidgetItem)
            self.myQListWidget.setItemWidget(myQListWidgetItem,  itm)
        self.setCentralWidget(self.myQListWidget)