
from Summarizator import Summarizator
from Translator_from_English import Translator_from_English
from Translate_to_English import Translate_to_English, Languages




text = "I눈을 뜬다 어둠 속 나 " + \
       "daughter Connie (Talia Shire) and Carlo Rizzi (Gianni Russo). Vito (Marlon Brando),"  + \
       "the head of the Corleone Mafia family, is known to friends and associates as Godfather. "  + \
       "He and Tom Hagen (Robert Duvall), the Corleone family lawyer, are hearing requests for favors "  + \
       "because, according to Italian tradition, no Sicilian can refuse a request on his daughter's wedding " + \
       " day. One of the men who asks the Don for a favor is Amerigo Bonasera, a successful mortician "  + \
       "and acquaintance of the Don, whose daughter was brutally beaten by two young men because she"  + \
       "refused their advances; the men received minimal punishment from the presiding judge. " + \
       "The Don is disappointed in Bonasera, who'd avoided most contact with the Don due to Corleone's" + \
       "nefarious business dealings. The Don's wife is godmother to Bonasera's shamed daughter, " + \
       "a relationship the Don uses to extract new loyalty from the undertaker. The Don agrees " + \
       "to have his men punish the young men responsible (in a non-lethal manner) in return for " + \
        "future service if necessary."



print(Summarizator.text_summary(text))



# print(Translator_from_English.translate("Hi, I'm Jimy! How are you?"))
# print(Translate_to_English.translate(Languages.Korean.value, Languages.english.value, "저도 요! ㅋㅋㅋ"))