import googletrans
from googletrans import Translator
#from different languages to English. May need to be changed.
#Using translation with Spanish
def text_changer(text, language="spanish"):
    translator1=Translator();
    translator2=Translator()
    text_spanish= translator1.translate(text, src='en', dest=language)
    result=translator2.translate(text_spanish.text)
    return result.text
text_changed=text_changer("Unless you have been hiding under a rock, you have probably used Google Translate on many occasions in your life. Whenever you try to translate a word or a sentence from a certain language to another, it is the Google Translate API which brings you the desired results in the background.",language="ukrainian")
print(text_changed)