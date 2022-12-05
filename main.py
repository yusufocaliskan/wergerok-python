from PyQt5.QtWidgets import (
    QPushButton, QApplication,
    QWidget, QLabel,QGridLayout,QPlainTextEdit,QComboBox,QStatusBar,
    QMainWindow, QHBoxLayout,QVBoxLayout)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import *

import sys
import time
import keyboard

from core.Werger import Werger 
class FerhengApp(QMainWindow):

    """Some defines about main windows"""
    windowWidth = 700
    windowHeight = 400
    title = 'Wergerok!'
    
    """Layout settings"""
    mainWidget = ""
    gridLayout = ""
    
    
    #Inputs
    fromInput = ""
    targetInput = ""

    #Selections
    sourceSelect = ""
    targetSelect = ""

    switcherButton = "" 
    
    #Werger class
    #The translator class
    werger = ""
    
    """ some usefull variables """
    loading = False
    statusBarMessage = "Silav û rêz!"
    
    def __init__(self):
        super(FerhengApp,self).__init__()
        self.createWindow()
        self.werger = Werger("ku","en")        

    def createWindow(self):
        """Creates main windows"""

        self.setWindowTitle(self.title)
        self.setFixedSize(self.windowWidth, self.windowHeight)

        #Just to push the gridLayout in it.
        self.createCentralWidget()
        self.statBar = QStatusBar()
        self.statBar.showMessage(self.statusBarMessage)
        self.setStatusBar(self.statBar)

        self.setCentralWidget(self.mainWidget)
        self.show()
    
    
    def createCentralWidget(self):
        """ Main widget """

        #GridLayout
        self.gridLayout = QGridLayout()
        
        #Language selections
        self.sourceSelect = QComboBox()
        self.sourceSelect.addItem('Kurdî',{"abbr":"ku"})
        self.sourceSelect.addItem('Ingilizî',{"abbr":"en"})
        self.sourceSelect.currentIndexChanged.connect(self.setSourceLanguage)
        self.gridLayout.addWidget(self.sourceSelect, 0,0)
        
        self.targetSelect = QComboBox()
        self.targetSelect.addItem('Ingilizî',{"abbr":"en"})
        self.targetSelect.addItem('Kurdî',{"abbr":"ku"})
        self.targetSelect.currentIndexChanged.connect(self.setTargetLanguage)
        self.gridLayout.addWidget(self.targetSelect, 0,2)
        
        #Switcher button
        self.switcherButton = QPushButton('Sw')
        self.gridLayout.addWidget(self.switcherButton,0,1)
        
        #From input
        self.fromInput = QPlainTextEdit('')
        self.fromInput.textChanged.connect(self.eventHandler)
        
        textFont = QFont()
        textFont.setPointSize(20)
        self.fromInput.setFont(textFont)
        self.gridLayout.addWidget(self.fromInput, 1,0)


        #target input
        self.targetInput = QPlainTextEdit('')
        self.targetInput.setFont(textFont)
        self.gridLayout.addWidget(self.targetInput, 1,2)

        #main widget        
        self.mainWidget = QWidget();
        self.mainWidget.setLayout(self.gridLayout)

    def setSourceLanguage(self):
        itemData = self.sourceSelect.itemData(self.sourceSelect.currentIndex())
        self.werger.setSourceLanguage(itemData["abbr"])

    def setTargetLanguage(self):
        itemData = self.targetSelect.itemData(self.targetSelect.currentIndex())
        self.werger.setTargetLanguage(itemData["abbr"])

    def eventHandler(self):
        """ Handling events """
        
        self.statBar.showMessage("Pêl [Enter]'ê bike, gava te qedant.[ "+self.werger.getSourceLanguage()+" ---> "+self.werger.getTargetLanguage()+" ]")

        #Whenever the from text is changed
        # is it pressed enter?
        if keyboard.is_pressed('enter'):
            fromText = self.fromInput.toPlainText()
            if fromText != "":
                result = self.werger.translate(fromText)
                self.targetInput.setPlainText(result)
                self.statBar.showMessage("Baş e, çêbû.")
            else:
                self.targetInput.setPlainText("")
            
    
        
#Start everything.
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ferhengApp = FerhengApp()
    sys.exit(app.exec())