class TalkExtractor:
    print("Hi!")
    
    def __init__(self, textFile):
        self.text = textFile.read()
        self.textList = self.text.split("\n")

    def specificUserTalk(self, name):
        self.filteredTalks = []
        for talk in self.textList:
            if name in talk.split("] [")[0]:
                self.filteredTalks.append(talk.split("] ")[2])
                #self.filteredTalks.append(talk)

        return(self.filteredTalks)
