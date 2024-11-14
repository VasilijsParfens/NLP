import sys
sys.stdout.reconfigure(encoding='utf-8')

text1 = "Rudens lapas ir dzeltenas un oranžas. Lapas klāj zemi un padara to krāsainu."
text2 = "Krāsainas rudens lapas krīt zemē. Lapas ir oranžas un dzeltenas."

words1 = set(text1.lower().replace('.', '').split())
words2 = set(text2.lower().replace('.', '').split())

common_words = words1.intersection(words2)
similarity_percentage = len(common_words) / len(words1.union(words2)) * 100

print(f"Sakritību vārdi: {common_words}")
print(f"Sakritības līmenis: {similarity_percentage:.2f}%")