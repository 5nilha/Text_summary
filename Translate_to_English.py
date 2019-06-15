from googletrans import Translator
from enum import Enum

class Languages(Enum):
    Korean = "ko"
    english = 'en'


class Translate_to_English(object):

    @staticmethod
    def translate(from_lang, to_lang, text):
        translator = Translator()

        return translator.translate(text).text