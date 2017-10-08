def voiceRecognizer(rawVoice):
    print('사용자의 음성을 인식하는 함수')
    return '음성데이터'

def voiceApiCaller(recognizedVoice):
    print('인식한 음성을 음성인식 API 서버에 보내 텍스트를 반환하는 함수')
    print('출력결과: "사용자가 말한 텍스트입니다."')
    return '사용자가 말한 텍스트'

def speechScriptInputter(textFile):
    print('사용자의 대본 파일을 받아들이는 함수')
    return '정돈된 문자열'

def speechScriptComparer(userVoiceText, scriptText):
    print('사용자가 말한 것과 사용자의 대본을 비교해 일치율(%)로 반환하는 함수')
    print('출력결과: 0.93')
    return '1보다 작거나 같고 0보다 크거나 같은 실수'

def scriptSlider(matchRate):
    print('대본 일치율이 70% 이상이면 다음 대본으로 넘기고 그렇지 않으면 대본을 넘기지 않는 함수')

# 최종 함수
def scriptSliderProgram(rawVoice, textFile):
    recognizedVoice = voiceRecognizer(rawVoice)
    userVoiceText = voiceApiCaller(recognizedVoice)
    scriptText = speechScriptInputter(textFile)
    matchRate = speechScriptComparer(userVoiceText, scriptText)
    scriptSlider(matchRate)

scriptSliderProgram(1,2)
