#### Remove Punctuation ########
import string
exclude = string.punctuation
def remove_punc(text):
    return text.translate(str.maketrans('', '', exclude))


############### 2nd 
import string

exclude = string.punctuation

def remove_punc(text):
    if not isinstance(text, str):
        text = str(text)
    return text.translate(str.maketrans('', '', exclude))
