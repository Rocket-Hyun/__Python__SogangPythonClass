import sys
sys.path.append("D:/mypython/input")
sys.path.append("D:/mypython/output")
sys.path.append("D:/mypython/process")
from input import Input
from output import Output
from process import Process


# 최종 메인 함수 입니다.
def scriptSliderProgram():
    input = Input()
    output = Output()
    process = Process()

    scriptText = input.speechScriptInputter()
    for sentence in scriptText:
        while True:
            print(sentence)
            # 음성을 인식해 파일로 변환하는 함수
            input.voiceRecognizer()
            userVoiceText = output.voiceApiCaller()
            print(userVoiceText)
            matchRate = output.speechScriptComparer(userVoiceText, sentence)
            print(matchRate)
            if matchRate > 0.6:
                break

scriptSliderProgram()
