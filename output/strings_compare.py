import difflib
# 특수문제 제거용 패키지
import re

def compare(userVoiceText, scriptText):
    cleanedScript = re.sub('[-=.#/?:$}]', '',scriptText)
    smilarity = difflib.SequenceMatcher(None, userVoiceText, cleanedScript).ratio()
    return smilarity