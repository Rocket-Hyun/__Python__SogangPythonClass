import sys
sys.path.append("D:/mypython/input")
sys.path.append("D:/mypython/output")
sys.path.append("D:/mypython/process")
import input
import output
from process import scriptSlider


# 최종 함수
def scriptSliderProgram(rawVoice, textFile):
    recognizedVoice = input.voiceRecognizer(rawVoice)
    userVoiceText = output.voiceApiCaller(recognizedVoice)
    scriptText = input.speechScriptInputter(textFile)
    matchRate = output.speechScriptComparer(userVoiceText, scriptText)
    scriptSlider(matchRate)

scriptSliderProgram(1,2)
