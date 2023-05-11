import googletrans
from googletrans import Translator


def quote_translate(quote, to_language="French"):
     translator = Translator()
     language = list(googletrans.LANGUAGES.keys())[list(googletrans.LANGUAGES.values()).index(to_language.lower())]
     print(language)
     result = translator.translate(quote, dest=language)
     return result.text