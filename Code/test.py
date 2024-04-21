import pandas as pd
import json
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import LancasterStemmer

# Descarcă resursele NLTK necesare
nltk.download('punkt')

def list_to_dict(lst):
    keys = ["Company_ID", "Company_Name", "Domain", "Category", "Google_Label", 
            "Linkedin_Label", "Facebook_Label", "Business_Model", "Genereted_Description", 
            "Generated_Buisness_tag", "Short_Description", "Long_Description", "Legal_Name", 
            "Facebook_Link", "Linkedin_Link"]
    return dict(zip(keys, lst))

def from_name_to_Naics2(name):
    if name == "Manufacturing":
        return 32
    elif name == "Services":
        return 54
    else:
        return 42

def preprocess_text(text):
    text = str(text)
    # Tokenize the text into words
    tokens = word_tokenize(text)
    
    # Initialize the Lancaster Stemmer
    ls = LancasterStemmer()
    
    # Stem each word and create a list of stemmed tokens
    stemmed_tokens = [ls.stem(token) for token in tokens]
    
    # Join the stemmed tokens back into a single string
    preprocessed_text = ' '.join(stemmed_tokens)
    
    return preprocessed_text

def importancecateg(text, input):
    short_description = str(input["Short_Description"]) if pd.notna(input["Short_Description"]) else ""
    long_description = str(input["Long_Description"]) if pd.notna(input["Long_Description"]) else ""
    
    valuexx = short_description + long_description
    information = preprocess_text(valuexx)

    importance = information.count(text)
    if importance == 0:
        importance = 0.5
    return importance

def calculate_compatibility_score_tab(importance_tuples, data_dict):
    compatibility_score = 0
        
    # Iterate over each key-value pair in the data dictionary
    for value in data_dict.values():
        name = value["Name"]
        description = " _ ".join(value["Description"])
        
        # Preprocess the name and description
        preprocessed_name = preprocess_text(name)
        preprocessed_description = preprocess_text(description)
        
        # Split the preprocessed name and description into words
        name_words = preprocessed_name.split()
        description_words = preprocessed_description.split()
        
        # Calculate compatibility score based on common sequences of words
        for word, importance in importance_tuples:
            # Check if the word is present in the name or description
            if word in name_words :
                compatibility_score += 3 * importance  # Weight for single word match
            elif word in description_words:
                compatibility_score += 1 * importance  # Weight for single word match in description
            # Check for sequences of 2 words
            if len(importance_tuples) > 1:
                for i in range(len(importance_tuples) - 1):
                    sequence = " ".join([importance_tuples[i][0], importance_tuples[i+1][0]])
                    if sequence in name:
                        compatibility_score += 9 * importance  # Weight for two-word sequence match in name
                    elif sequence in description:
                        compatibility_score += 4 * importance  # Weight for two-word sequence match in description
            # Check for sequences of 3 words
            if len(importance_tuples) > 2:
                for i in range(len(importance_tuples) - 2):
                    sequence = " ".join([importance_tuples[i][0], importance_tuples[i+1][0], importance_tuples[i+2][0]])
                    if sequence in name :
                        compatibility_score += 27 * importance  # Weight for three-word sequence match in name
                    elif sequence in description:
                        compatibility_score += 16 * importance  # Weight for three-word sequence match in description

    return compatibility_score

def mainfunction(valueC2, input):
    with open("naics4.json", "r") as json_file:
        data_dict = json.load(json_file)
        
    frecV = [0] * 100
    tag_importance_tuples = preprocess_text(input["Generated_Buisness_tag"]).split(" ")
    categ_importance_tuples = [(word, importancecateg(word, input)) for word in input["Category"].split(" ")]
    
    for key, value in data_dict.items():
        intval = int(key) // 100
        if intval == valueC2:
            frecV[int(key) % 100] += calculate_compatibility_score_tab(categ_importance_tuples, {key: value})
    print(f"{valueC2}{frecV.index(max(frecV))}")
    return f"{valueC2}{frecV.index(max(frecV))}"

if __name__ == "__main__":
    df = pd.read_csv("../NAICS6_Classification.csv")
    id_list = ["ID"]
    name_list = ["Name"]
    Naics_list =["Naics"]

    for index, row in df.iloc[:10000].iterrows(): 
        CompanyList = list(row)
        CompanyImpData = list_to_dict(CompanyList)
        Id = CompanyImpData["Company_ID"]
        Name = CompanyImpData["Company_Name"]
        valueC2 = from_name_to_Naics2(CompanyImpData["Business_Model"])
        id_list.append(Id)
        name_list.append(Name)
        valueC4 = mainfunction(valueC2, CompanyImpData)
        Naics_list.append(valueC4)
        if index % 1000 == 0:
            print(index)
    
    output_df = pd.DataFrame({"Id": id_list, "Name": name_list, "Naics": Naics_list})

    # Write DataFrame to Excel
    output_df.to_excel("../output.xlsx", index=False)
