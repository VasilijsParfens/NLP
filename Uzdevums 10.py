from deep_translator import GoogleTranslator

texts = ['Labdien! Kā jums klājas?', 'Es šodien lasīju interesantu grāmatu.']
translations = []

for text in texts:
    translation = GoogleTranslator(source='lv', target='en').translate(text)
    translations.append(translation)

for translated_text in translations:
    print(translated_text)
