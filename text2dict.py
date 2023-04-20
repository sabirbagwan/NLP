chat_words = {}
for line in text.split('\n'):
    abbr, full_form = line.split('=')
    chat_words[abbr] = full_form
    
# print(chat_words)
chat_words
