import sys
sys.path.append("D:/mypython/input")
sys.path.append("D:/mypython/output")
sys.path.append("D:/mypython/process")
from input import Input
from output import Output
from process import Process


# 최종 함수
def scriptSliderProgram(rawVoice, textFile):
    input = Input()
    output = Output()
    process = Process()
    recognizedVoice = input.voiceRecognizer(rawVoice)
    userVoiceText = output.voiceApiCaller(recognizedVoice)
    scriptText = input.speechScriptInputter(textFile)
    matchRate = output.speechScriptComparer(userVoiceText, scriptText)
    process.scriptSlider(matchRate)

scriptSliderProgram(1,2)
