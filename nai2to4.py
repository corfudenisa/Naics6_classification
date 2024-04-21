import json
from functions import  preprocess_text ,importancecateg

with open("naics4.json", "r") as json_file:
        data_dict = json.load(json_file)

data_dict_32 = {}
data_dict_42 = {}
data_dict_54 = {}
for key,value in data_dict.items():
    intval = int(key) // 100
    if(intval == 32):
        data_dict_32[key]=data_dict[key]
    elif(intval ==42):
        data_dict_42[key]=data_dict[key]
    elif(intval ==54):
        data_dict_54[key]=data_dict[key]


# Now you can access the data in the dictionary as needed
def calculate_compatibility_score_tab(importance_tuples, data_dict):
    compatibility_score = 0
        
    # Iterate over each key-value pair in the data dictionary
    value = data_dict
    
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
        
    frecV = [0] * 100
    tag_importance_tuples = preprocess_text(input["Generated_Buisness_tag"])
    categ=preprocess_text(input["Category"])
    listcateg = categ.split(" ")
    listcateg_score =[]
    for word in listcateg:
        categ_importance_tuples =(word , importancecateg(word,input))
        listcateg_score.append(categ_importance_tuples)
    
    if(valueC2==32):
        data_dict1 = data_dict_32
    elif(valueC2==42):
        data_dict1 = data_dict_42
    elif(valueC2==54):
        data_dict1 = data_dict_54
    else:
        print(valueC2 // 100)
    for keys in data_dict1:
        intval = int(keys) // 100
        if intval == valueC2:
            frecV[int(keys) % 100] += calculate_compatibility_score_tab(listcateg_score, data_dict1[keys])
    
    # print("Maximum value in frecV:", max(frecV))
    # print("Index of the maximum value in frecV:", f"{valueC2}{frecV.index(max(frecV))}")
    return int(f"{valueC2}{frecV.index(max(frecV))}")
