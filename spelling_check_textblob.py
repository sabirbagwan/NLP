from textblob import TextBlob
def spelling_check_textblob(text):
    textBlb = TextBlob(text)
    return textBlb.correct().string
