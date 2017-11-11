def read_script():
    textFile = open("script.txt", "r", encoding="utf8")
    texts = textFile.read()
    textList = texts.split(".")
    return textList