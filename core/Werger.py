from googletrans import Translator


class Werger:

    #Default selected target language
    targetLanguage = 'en'
    sourceLanguage = 'ku' #Kurdish
    
    #Some more info about language
    languages = {
        "kr":{
            "name": "Kurdî",
            "slug": "Ku"
        }
    }

    #Result of the translation
    result = ""

    #the translator.
    translator = Translator()

    def __init__(self, sourceLang, targetLang):
        self.setTargetLanguage(targetLang)
        self.setSourceLanguage(sourceLang)

    def terminal(self):
        """ Getting the text will be translated """

        while True:
            targetLanguage = input("Select the target language: ")
            sourceLanguage = input("Select the target language: ")
            self.setTargetLanguage(targetLanguage)
            self.setTargetLanguage(sourceLanguage)
            text = input("Enter the text: ")
            print("Result("+sourceLanguage+"->"+targetLanguage+") : ",self.translate(text))

    def translate(self, text):
        """ Translate the given text """
        
        self.result = self.translator.translate(text, dest=self.targetLanguage, src=self.sourceLanguage)
        return self.result.text
    
    
    def setTargetLanguage(self, lang ):
        """sets the selected language
            @lang : the abbrevation of the lang """
        self.targetLanguage = lang

    def setSourceLanguage(self, lang ):
        """sets the selected language
            @lang : the abbrevation of the lang """
        self.sourceLanguage = lang


# if __name__ == "__main__":
#     #Set the language and start the applications
#     werger = Ferheng("en")
#     werger.terminal()
    