import sys
sys.stdout.reconfigure(encoding='utf-8')

import re

text = "Šis ir lielisks produkts!!! Vai ne? 👏👏👏 http://example.com"
cleaned_text = re.sub(r'http\S+|@\w+|[^a-zA-Zā-žĀ-Ž\s]', '', text).lower().strip()

print(cleaned_text)
