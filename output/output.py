class Output:

    def voiceApiCaller(self, recognizedVoice):
        print('인식한 음성을 음성인식 API 서버에 보내 텍스트를 반환하는 함수')
        print('출력결과: "사용자가 말한 텍스트입니다."')
        return '사용자가 말한 텍스트'

    def speechScriptComparer(self, userVoiceText, scriptText):
        print('사용자가 말한 것과 사용자의 대본을 비교해 일치율(%)로 반환하는 함수')
        print('출력결과: 0.93')
        return '1보다 작거나 같고 0보다 크거나 같은 실수'
