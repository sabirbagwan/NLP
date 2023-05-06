text = ' '.join(w for w in X['Preamble'])

wordcloud = WordCloud(width = 1200, height = 1200, background_color = 'black', min_font_size = 10).generate(text)

# plt.title('Top 10 most used words in all the Preamble', backgroundcolor = 'skyblue')
plt.figure(figsize = (12, 12), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
plt.savefig('wordcloud.png')
plt.show()
