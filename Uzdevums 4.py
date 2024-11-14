import sys
sys.stdout.reconfigure(encoding='utf-8')

from textblob import TextBlob

sentences = [
    "Šis produkts ir lielisks, esmu ļoti apmierināts!",
    "Esmu vīlies, produkts neatbilst aprakstam.",
    "Neitrāls produkts, nekas īpašs."
]

for sentence in sentences:
    analysis = TextBlob(sentence)
    sentiment = "pozitīvs" if analysis.polarity > 0 else "negatīvs" if analysis.polarity < 0 else "neitrāls"
    print(f"Teikums: \"{sentence}\" - Noskaņojums: {sentiment}")
