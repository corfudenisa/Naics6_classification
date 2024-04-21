import nltk
nltk.download('stopwords')
import re
import json
from functions import preprocess_text 
# Read the text file and split it into sections based on empty lines
with open("../datanaics4.txt", "r") as file:
    sections = file.read().split("\n\n")

# Define a function to extract data from each section
def extract_data(section):
    lines = section.split("\n")
    code_match = re.search(r"\d{4}", lines[0])
    name_match = re.search(r"(?<=- ).*", lines[0])
    if code_match and name_match:
        code = code_match.group(0)
        name = name_match.group(0).strip()
        description = [line.strip("- ") for line in lines[1:]]
        return code, {"Name": name, "Description": description}
    else:
        return None

# Create a dictionary to store the data
data_dict = {}

# Extract data from each section and add it to the dictionary
for section in sections:
    data = extract_data(section)
    if data:
        code, info = data
        info['Name'] = preprocess_text(info['Name'])
        info['Name'] = (info['Name'].split(":"))[0]
        listXX =[]
        for XX in info['Description']:
            listXX.append(preprocess_text(XX))
        info['Description']=listXX
        #prcdata=preprocess_text(info)
        data_dict[code] = info

# Write the dictionary to a JSON file
with open("naics4.json", "w") as json_file:
    json.dump(data_dict, json_file, indent=4)
