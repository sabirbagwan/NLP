words = []
for text in X['message']:
    words.extend(text.split())
word_count = collections.Counter(words)
top_words = dict(word_count.most_common(23))
top_words



# Figure Size
plt.figure(figsize = (15, 6))

# Create the Barplot
plt.bar(range(len(top_words)), list(top_words.values()), align = 'center')

# Creating a y axis with words
plt.xticks(range(len(top_words)), list(top_words.keys()))

# Grid Opacity
plt.grid(alpha = 0.5)

# Title
plt.title('Top 10 most used words', fontsize = 8)
plt.xticks(rotation = 45, ha = 'center')
plt.xlabel('Words')
plt.ylabel('Frequency')
