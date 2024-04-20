from functions import preprocess_text as pt
import json

with open("naics6.json", "r") as json_file:
    data_dict = json.load(json_file)
for keys in data_dict:
    print(data_dict[keys]["Name"])

    data_dict[keys]["Name"] = pt(data_dict[keys]["Name"])
    listnew =[]
    for text in data_dict[keys]["Description"]:
        listnew.append(pt(text))
    data_dict[keys]["Description"] = listnew

with open("naics6.json", "w") as json_file:
    # Write the modified data_dict to the file
    json.dump(data_dict, json_file, indent=4)
