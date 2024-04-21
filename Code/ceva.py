import json
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize

def stem_text(text):
    tokens = word_tokenize(text)
    stemmer = SnowballStemmer('english')
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    return ' '.join(stemmed_tokens)

try:
    with open("naics6.json", "r") as json_file:
        data_dict = json.load(json_file)
        
    for key, value in data_dict.items():
        # Stem the name
        data_dict[key]["Name"] = stem_text(value["Name"])
        
        # Stem each description
        stemmed_descriptions = [stem_text(desc) for desc in value["Description"]]
        data_dict[key]["Description"] = stemmed_descriptions

    with open("naics6.json", "w") as json_file:
        json.dump(data_dict, json_file, indent=4)
        print("Data written successfully.")
        
except Exception as e:
    print("Error occurred:", e)
