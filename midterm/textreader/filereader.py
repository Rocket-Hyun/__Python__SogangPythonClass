class TextReader:
    def __init__(self, fileName):
        textFile = open(fileName, "r", encoding="utf8")
        self.text = textFile.read()

