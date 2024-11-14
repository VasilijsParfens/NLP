import nltk
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

nltk.download('punkt')

text = "Latvija ir valsts Baltijas reģionā. Tās galvaspilsēta ir Rīga, kas ir slavena ar savu vēsturisko centru un skaistajām ēkām. Latvija robežojas ar Lietuvu, Igauniju un Krieviju, kā arī tai ir piekļuve Baltijas jūrai. Tā ir viena no Eiropas Savienības dalībvalstīm."

# Izmanto angļu valodu vai pārbauda, vai citas ir pieejamas
parser = PlaintextParser.from_string(text, Tokenizer("english"))
summarizer = LsaSummarizer()

for sentence in summarizer(parser.document, 2):
    print(sentence)
