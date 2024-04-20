import json
# Open the JSON file and load its contents into a dictionary
with open("naics4.json", "r") as json_file:
    data_dict = json.load(json_file)

# Now you can access the data in the dictionary as needed
def mainfunction(valueC2):
    with open("naics4.json", "r") as json_file:
        data_dict = json.load(json_file)
    for keys in data_dict:
        key_int=int(keys)
        frecV = [0] * 100


