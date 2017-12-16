import voice_input as vi
import script_parser as sp

class Input:

    def voiceRecognizer(self):
        # print('사용자의 음성을 인식하는 함수')
        vi.record_to_file('voice.wav')

    def speechScriptInputter(self):
        # print('사용자의 대본 파일을 받아들이는 함수')
        # return '정돈된 문자열'
        return sp.read_script()
