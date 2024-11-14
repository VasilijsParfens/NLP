from gensim.models import Word2Vec

sentences = [["māja", "ir", "balta"], ["dzīvoklis", "ir", "liels"], ["jūra", "ir", "zila"]]
model = Word2Vec(sentences, vector_size=50, min_count=1, window=3)

for word in ["māja", "dzīvoklis", "jūra"]:
    print(f"{word} vektors: {model.wv[word]}")
