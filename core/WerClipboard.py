import clipboard
import os
import keyboard
from pynput.keyboard import GlobalHotKeys
import platform
import asyncio

class WerClipboard:
    
    def listenEvent(self):
        lastCopiedText = self.getLastCopiedText()
        while True:
            if lastCopiedText != clipboard.paste():
                self.saveLastCopiedText()        
                return

    def saveLastCopiedText(self):
        """ Saves the last copied text """
        
        with open("data/clipboard.txt","w") as file:
            file.write(clipboard.paste())
            file.close()

    def getLastCopiedText(self):
        """ Reads the last copy text """
        with open("data/clipboard.txt","r") as file:
            content = file.read()
            file.close()
            return str(content)
    
    def paste():
        return clipboard.paste()
    
    
    def copy():
        return clipboard.copy()
    