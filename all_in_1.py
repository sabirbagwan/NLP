#### HTML Tags removal #########
import re
def remove_html_tags(text):
    pattern = re.compile('<.*?>')
    return pattern.sub(r'', text)


def clean_re(text):
    regex = re.compile('[^a-z\s]')
    return regex

#### Remove links ##########
def remove_url(text):
    pattern = re.compile(r'https?://\S+|www\.\S+')
    return pattern.sub(r'', text)


#### Remove Punctuation ########
import string
exclude = string.punctuation
def remove_punc(text):
    return text.translate(str.maketrans('', '', exclude))


from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

def remove_stopwords(text):
    words = text.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return " ".join(filtered_words)


### Remove Emoji
import re
def remove_emoji(text):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)


### Replace Emoji with words
import emoji
def demojize(text):
    return emoji.demojize(text)


### Tokenisation with NLTK
from nltk.tokenize import word_tokenize,sent_tokenize
def word_tokenize_nltk(text):
    return word_tokenize(text)

#### Tokenisation with spacy
import spacy
nlp = spacy.load('en_core_web_sm')
def word_tokenize_spacy(text):
    return nlp(text)

### Stemming 
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
def stem_words(text):
    return " ".join([ps.stem(token.text) for token in nlp(text)])


###### Lemmatization
import spacy
nlp = spacy.load("en_core_web_sm")
def lemmatize_words(text):
    doc = nlp(text)
    return " ".join([token.lemma_ if token.lemma_ != '-PRON-' else token.text for token in doc])
