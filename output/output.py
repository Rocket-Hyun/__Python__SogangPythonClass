import google_voice_api as gv
import strings_compare as sc

class Output:

    def voiceApiCaller(self):
        return gv.recognition()

    def speechScriptComparer(self, userVoiceText, scriptText):
        return sc.compare(userVoiceText, scriptText)
        # print('사용자가 말한 것과 사용자의 대본을 비교해 일치율(%)로 반환하는 함수')
        # print('출력결과: 0.93')
        # return '1보다 작거나 같고 0보다 크거나 같은 실수'
