from gensim.summarization import summarize


class Summarizator:

    @staticmethod
    def text_summary(text):
        return summarize(text)
