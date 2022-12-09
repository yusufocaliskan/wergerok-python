from PyPDF2 import PdfReader
import re

class TextExtractor:
    resultFile = "../data/result.txt"
    testFile = "../data/test.txt"
    def __init__(self):
        pass
        
    """ ji dosyê encamê peyvan li ekranê bi nîşan dide. """
    def display(self):
        getTextLines = self.getTextFromFile()
        i = -1 #ji bo risteye evil bê stendin.
        while i <= 100:
            i +=1
            text = getTextLines[i]
            #text = "b,B1 a,Am1 c,C,1. d,D1 a,Am1."
            """ Herfên sereke ên elfêbê bibin """
            search= re.sub(r"([a-z],Am?,?1?.?)",r'\n############################## [ \1 ] #####################\n',text)
                              
            print(i," -> ", search)
        
        #self.save2File(search, self.testFile)
    """ li peyîvan digere """
    def match():
        pass

    """ Ji dosya .pdf ku peyv tê de nivisî  dixwîne. """
    def extractTextFromPdf(self):
        reader = PdfReader("../data/ferheng.pdf")
        number_of_pages = len(reader.pages)
        i = 23
        result = ""
        while i < number_of_pages-2:
            i +=1
            print(i)
            page = reader.pages[i]
            text = page.extract_text()
        result += str(text)
        self.save2File(result, self.resultFile)


    """ encame tomar bike
        :data - daneyên ku dê bên tomarkirin
    """
    def save2File(self, data, file):
        with open(file, "w") as f:
            f.write("\n".join(data))
            f.close()

    
    """ encama ku ji .pdfê vegerîya li dosyayê dinivîse.  """
    def getTextFromFile(self):
        with open(self.resultFile, "r") as file:
            return file.readlines()
            



if __name__ == "__main__":
    TextExtractor().display()


