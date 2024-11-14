import sys
import markovify

sys.stdout.reconfigure(encoding='utf-8')

text = """Reiz kādā tālā zemē karalis dzīvoja pilī. Viņš bija labsirdīgs un mīlēja savus pavalstniekus. 
Pils dārzā vienmēr ziedēja skaistas puķes, un putni priecīgi čivināja."""
model = markovify.Text(text)

generated_text = model.make_sentence(tries=100)

print(generated_text if generated_text else "Neizdevās ģenerēt teikumu.")
