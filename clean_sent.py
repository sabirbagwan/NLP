# creating a function to preprocess the text
def clean_sent(sent):
    
    ## splitting the sentence into words 
    words = word_tokenize(sent)
    
    ## removing punctuations from the words list
    re_punc = re.compile('[%s]' % re.escape(string.punctuation))
    words = [re_punc.sub('', word) for word in words]
    
    ## removing un-printable words from the word list
    re_unprintable = re.compile('[^%s]' % re.escape(string.printable))
    words = [re_unprintable.sub('', word) for word in words]
    
    ## removing non-alphabetic 
    words = [word for word in words if word.isalpha()]
    
    ## removing the word with only one character
    words = [word for word in words if len(word) > 1]
    
    ## lowering the case of all the words
    words = [word.lower() for word in words]
    
    ## removing the stopwords from the words
    words = [word for word in words if word not in set(stopwords.words('english'))]
    
    ## stemming the words
    words = [WordNetLemmatizer().lemmatize(word) for word in words]
    
    ## joining the words again to make a sentence
    return words
