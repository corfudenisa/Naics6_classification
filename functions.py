import nltk
import pandas as pd
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
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
    text=str(text)
    # Tokenize the text into words
    tokens = word_tokenize(text)
    
    # Initialize the Lancaster Stemmer
    ls = SnowballStemmer('english')
    
    # Stem each word and create a list of stemmed tokens
    stemmed_tokens = [ls.stem(token) for token in tokens]
    
    # Join the stemmed tokens back into a single string
    preprocessed_text = ' '.join(stemmed_tokens)
    
    return preprocessed_text
def importancecateg(text,input):
    short_description = input["Short_Description"] if pd.notna(input["Short_Description"]) else ""
    long_description = input["Long_Description"] if pd.notna(input["Long_Description"]) else ""

    valuexx = "".join([short_description, long_description])
    information = preprocess_text(valuexx)

    importan = information.count(text)
    if importan == 0 :
        importan = 0.5
    return importan

