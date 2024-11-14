import spacy

nlp = spacy.load("lv_core_news_sm")
text = "Valsts prezidents Egils Levits piedalījās pasākumā, ko organizēja Latvijas Universitāte."

doc = nlp(text)
for ent in doc.ents:
    print(f"Entitāte: {ent.text}, tips: {ent.label_}")
