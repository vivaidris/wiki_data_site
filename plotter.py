import matplotlib.pyplot as plt

fig, ax = plt.subplots()

bins = [0, 50, 100, 150, 200]
counts = [31, 10, 7, 1]
bar_labels = ['0-50', '51-99', '100-149', '150-200']
bar_colors = [
    (235/255, 255/255, 53/255, 1.0),
    (182/255, 235/255, 50/255, 1.0),
    (67/255, 194/255, 130/255, 1.0),
    (59/255, 209/255, 214/255, 1.0)
]

bin_centers = [(bins[i] + bins[i+1]) / 2 for i in range(len(bins) - 1)]

bars = ax.bar(bin_centers, counts, width=40, color=bar_colors, edgecolor='black')

ax.set_xticks(bin_centers)
ax.set_xticklabels(bar_labels)

ax.set_ylabel('Paragraph amount per article')
ax.set_xlabel('Range of paragraphs')
ax.set_title('Chart of Paragraphs per Article')

ax.set_ylim(0, max(counts) + 5)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Add data labels on top of bars
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # offset label slightly above bar
                textcoords='offset points',
                ha='center', va='bottom')

plt.show()

