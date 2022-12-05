from googletrans import Translator


class Werger:

    #Default selected target language
    selectedLanguage = ""
    
    #Some more info about language
    languages = {
        "kr":{
            "name": "Kurdî",
            "slug": "Kr"
        }
    }

    #Result of the translation
    result = ""

    #the translator.
    translator = Translator()

    def __init__(self, selectedLanguage):
        self.setSelectedLanguage(selectedLanguage)

    def terminal(self):
        """ Getting the text will be translated """

        while True:
            targetLanguage = input("Select the target language: ")
            self.setSelectedLanguage(targetLanguage)
            text = input("Enter the text: ")
            print("Result("+targetLanguage+") : ",self.translate(text))

    def translate(self, text):
        """ Translate the given text """
        
        self.result = self.translator.translate(text, dest=self.selectedLanguage)
        return self.result.text
    
    
    def setSelectedLanguage(self, lang ):
        """sets the selected language
            @lang : the abbrevation of the lang """

        self.selectedLanguage = lang


# if __name__ == "__main__":
#     #Set the language and start the applications
#     werger = Ferheng("en")
#     werger.terminal()
    