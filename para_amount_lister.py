import math
import json
import os

os makedirs("json_files", exist_ok=True)

with open('json_files/wiki_data.json', 'r') as f:
    wiki_data = json.load(f)

count_a = sum(1 for item in wiki_data if item.get('paragraph_count', 0) <= 50)
count_b = sum(1 for item in wiki_data if 50 <= item.get('paragraph_count', 0) < 100)
count_c = sum(1 for item in wiki_data if 100 <= item.get('paragraph_count', 0) < 150)
count_d = sum(1 for item in wiki_data if 150 <= item.get('paragraph_count', 0))

print(count_a)
print(count_b)
print(count_c)
print(count_d)