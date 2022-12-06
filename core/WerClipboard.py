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
                return True

    def saveLastCopiedText(self):
        """ Saves the last copied text """
        
        file = os.open("data/clipboard.txt","w")
        file.write(clipboard.paste())
        file.close()

    def getLastCopiedText(self):
        """ Reads the last copy text """
        file = os.popen("data/clipboard.txt","r")
        content = file.read()
        file.close()
        return str(content)
    
    def paste():
        return clipboard.paste()
    
    
    def copy():
        return clipboard.copy()
    