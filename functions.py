import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.corpus import wordnet as wn
from nltk.metrics import jaccard_distance


def list_to_dict(list):
    dict={}
    dict['Company_ID'] = list[0]
    dict['Company_Name'] = list[1]
    dict['Domain'] = list[2]
    dict['Category'] = list[8]
    dict['Google_Label'] = list[9]
    dict['Linkedin_Label'] = list[10]
    dict['Facebook_Label']  = list[11]
    dict['Business_Model'] = list[12]
    dict['Genereted_Description'] = list[14]
    dict['Generated_Buisness_tag'] = list[15]
    dict['Short_Description'] = list[16]
    dict['Long_Description'] = list[17]
    dict['Legal_Name'] = list[20]
    dict['Facebook_Link'] = list[24]
    dict['Linkedin_Link'] = list[25]
    return dict

def from_name_to_Naics2(name):
    if(name == "Manufacturing"):
        return 32
    if(name=="Services"):
        return 54
    return 42

from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

def preprocess_text(text):
    # Tokenize the text into words
    tokens = word_tokenize(text)
    
    # Initialize the Porter Stemmer
    ps = PorterStemmer()
    
    # Stem each word and create a list of stemmed tokens
    stemmed_tokens = [ps.stem(token) for token in tokens]
    
    # Join the stemmed tokens back into a single string
    preprocessed_text = ' '.join(stemmed_tokens)
    
    return preprocessed_text
