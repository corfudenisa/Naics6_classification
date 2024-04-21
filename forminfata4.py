import nltk
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize
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
import json

try:
    with open("naics6.json", "r") as json_file:
        data_dict = json.load(json_file)
        
    for keys in data_dict:
        data_dict[keys]["Name"] = preprocess_text(data_dict[keys]["Name"])
        listnew =[]
        for text in data_dict[keys]["Description"]:
            listnew.append(preprocess_text(text))
        data_dict[keys]["Description"] = listnew
    print(data_dict["423140"])
    print(preprocess_text("(Used)"))
    with open("naics6.json", "w") as json_file:
        json.dump(data_dict, json_file, indent=4)
        print("Data written successfully.")
        

except Exception as e:
    print("Error occurred:", e)
