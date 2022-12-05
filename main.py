from PyQt5.QtWidgets import (
    QPushButton, QApplication,
    QWidget, QLabel,QGridLayout,QPlainTextEdit,QComboBox,
    QMainWindow, QHBoxLayout,QVBoxLayout)
import sys
import time

from core.Werger import Werger 
class FerhengApp(QMainWindow):

    """Some defines about main windows"""
    windowWidth = 700
    windowHeight = 400
    title = 'Ferhengok!'
    
    """Layout settings"""
    mainWidget = ""
    gridLayout = ""
    
    
    #Inputs
    fromInput = ""
    targetInput = ""

    #Selections
    fromSelect = ""
    targetSelect = ""

    switcherButton = "" 
    
    #Werger class
    #The translator class
    werger = ""

    def __init__(self):
        super(FerhengApp,self).__init__()
        self.createWindow()
        self.werger = Werger("en")


    def createWindow(self):
        """Creates main windows"""

        self.setWindowTitle(self.title)
        self.setFixedSize(self.windowWidth, self.windowHeight)

        #Just to push the gridLayout in it.
        self.createCentralWidget()
        self.setCentralWidget(self.mainWidget)
        self.show()
    
    
    def createCentralWidget(self):
        """ Main widget """

        #GridLayout
        self.gridLayout = QGridLayout()
        
        #Language selections
        self.fromSelect = QComboBox()
        self.fromSelect.addItem('Kurdî')
        self.fromSelect.addItem('Ingilizî')
        self.gridLayout.addWidget(self.fromSelect, 0,0)
        
        self.targetSelect = QComboBox()
        self.targetSelect.addItem('Kurdî')
        self.targetSelect.addItem('Ingilizî')
        self.gridLayout.addWidget(self.targetSelect, 0,2)
        
        #Switcher button
        self.switcherButton = QPushButton('Sw')
        self.gridLayout.addWidget(self.switcherButton,0,1)
        
        #From input
        self.fromInput = QPlainTextEdit('')
        self.fromInput.textChanged.connect(self.eventHandler)
        self.gridLayout.addWidget(self.fromInput, 1,0)
        
        #From input
        self.empty = QLabel('')
        self.gridLayout.addWidget(self.empty, 1,1)

        #To input
        self.targetInput = QPlainTextEdit('')
        
        self.gridLayout.addWidget(self.targetInput, 1,2)

        #main widget        
        self.mainWidget = QWidget();
        self.mainWidget.setLayout(self.gridLayout)
        

    def eventHandler(self):
        """ Handling events """
        
        #Whenever the from text is changed
        fromText = self.fromInput.toPlainText()
        if fromText != "":
            result = self.werger.translate(fromText)
            self.targetInput.setPlainText(result)
        else:
            self.targetInput.setPlainText("")
        
    
    
    

#Start everything.
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ferhengApp = FerhengApp()
    sys.exit(app.exec())