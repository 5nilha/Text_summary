from translate import Translator

class Translator_from_English(object):

    @staticmethod
    def translate(text):
        translator = Translator(to_lang="Korean")
        original_text = text.split(" ")
        sentences = []
        translated_text = ""
        sentence = ""
        char_count = 0
        count_words = 0
        total_words = len(original_text)
        for word in original_text:
            count_words += 1
            if char_count < 300:
                sentence += " " + word
                if char_count < 300 and count_words == total_words:
                    sentences.append(sentence)
            else:
                sentences.append(sentence)
                sentence = ""
                sentence += word

                char_count = 0
            char_count += len(word)



        for sentence in sentences:
            translation = translator.translate(sentence)
            translated_text += " " + translation

        return translated_text + "."

