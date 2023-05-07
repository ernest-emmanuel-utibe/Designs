import googletrans
from googletrans import Translator
print(googletrans.LANGUAGES)

translator = Translator()
result = translator.translate('salut programatori ')
print(result)
# by default the translate() method returns the english translation of the text passed to it.

result = translator.translate('salut programatori', src='ro', dest='en')
print(result)
