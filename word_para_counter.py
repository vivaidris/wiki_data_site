import json
import math

with open('wiki_data.json', 'r') as f:
    wiki_data = json.load(f)

total_para_sum = sum(obj.get('paragraph_count', 0) for obj in wiki_data)
total_word_sum = sum(obj.get('word_count', 0) for obj in wiki_data)

av_para = total_para_sum/50
av_word = total_word_sum/50

print(math.ceil(av_word))
print(math.ceil(av_para))