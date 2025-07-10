import json
import matplotlib.pyplot as plt

# Load JSON data
with open('wiki_data.json', 'r') as f:
    data = json.load(f)

paragraph_counts = []
word_counts = []

for article in data:
    p = article.get('paragraph_count')
    w = article.get('word_count')
    if p is not None and w is not None:
        paragraph_counts.append(p)
        word_counts.append(w)

plt.figure(figsize=(8,6))

# Scatter plot with color mapped to word counts
scatter = plt.scatter(
    paragraph_counts,
    word_counts,
    c=word_counts,            # color values based on word counts
    cmap='inferno',           # colormap from dark purples to bright yellow
    alpha=0.8,
    edgecolor='k',
    s=50                      # size of dots
)

plt.colorbar(scatter, label='Word Count')  # add a color bar legend

plt.xlabel('Paragraph Count')
plt.ylabel('Word Count')
plt.title('Paragraph Count vs Word Count Colored by Word Count')

plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
