import pandas as pd
dictData = {}
prefix = [32, 42, 54]
df = pd.read_excel("../2022-NAICS-Keywords.xlsx")

for index, row in df.iterrows():
    values = row.values  # Get the values of the row
    try:
        val = int(values[0])  # Convert values[0] to integer
        if val // 10000 in prefix:
            key = f"{values[0]}"
            if key not in dictData:
                dictData[key] = {"Name":values[1],"Description": []}
                
            dictData[key]["Description"].append(values[2])
    except:
        pass
   


import json




# Define the file path
file_path1 = "naics6.json"

with open(file_path1, "w") as json_file1:
    json.dump(dictData, json_file1, indent=4)
