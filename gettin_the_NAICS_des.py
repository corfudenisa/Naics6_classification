import pandas as pd

dictData = {}
dictData24 ={}
prefix = [32, 42, 54]
df = pd.read_excel("../2022-NAICS-Keywords.xlsx")

for index, row in df.iloc[:10000].iterrows():
    values = row.values  # Get the values of the row
    val = int(values[0])  # Convert values[0] to integer
    if val // 10000 in prefix:
        key = f"{values[0]}"
        key2 = f"{values[0]/10000}"
        if key not in dictData24: 
            description = {}
            subcategories = {}
            dictData[key] = {}
        dictData24[]
        if key not in dictData:
            dictData[key] = []
        dictData[key].append(values[2])
   


import json




# Define the file path
file_path = "naics6.json"

# Write dictionary to JSON file
with open(file_path, "w") as json_file:
    json.dump(dictData, json_file, indent=4)