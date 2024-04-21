import json
from functions import preprocess_text

with open("naics6.json", "r") as json_file:
    data_dict = json.load(json_file)

with open("naics4.json", "r") as json_file_2:
    data_dict_not = json.load(json_file_2)

keys_starting_with_32 = [key for key in data_dict.keys() if key.startswith("32")]
keys_starting_with_42 = [key for key in data_dict.keys() if key.startswith("42")]
keys_starting_with_54 = [key for key in data_dict.keys() if key.startswith("54")]

good_text = preprocess_text("Used used junk recyable")

def calculate_compatibility_score_tab(data_yes, data_not, input_list):
    compatibility_score = 0
    # Iterate over each item in the input list
    for word in input_list:
        # Iterate over each word in the item
        
        if len(word) == 1:
            if(word[0][0]=='cloth'):
                pass
            if word[0][0] in data_yes["Name"]:
                compatibility_score += 8 * word[0][1]
                compatibility_score += (data_yes["Description"].count(word[0]) * 4 / len(data_yes["Description"])) * word[0][1]
        elif len(word) == 2:
            if word[0][0] in data_yes["Name"] and word[1][0] in data_yes["Name"]:
                compatibility_score += 12 * (word[0][1] + word[1][1]) / 2
            if word[0][0] in data_yes["Name"]:
                compatibility_score += 4 * word[0][1]
            if word[1][0] in data_yes["Name"]:
                compatibility_score += 4 * word[1][1]
            compatibility_score += (data_yes["Description"].count(word) * 6 / len(data_yes["Description"])) * (word[0][1] + word[1][1]) / 2
            compatibility_score += ((data_yes["Description"].count(word[0][0]) * 2 * word[0][1] + data_yes["Description"].count(word[1][0]) * 2) / len(data_yes["Description"])) * word[0][1]
        elif len(word) == 3:
            xxx = [word_tuple[0] for word_tuple in word]
            trigram = " ".join(xxx)
            if trigram in data_yes["Name"]:
                compatibility_score += 16 * (word[0][1]+word[1][1]+word[2][1])/3
            if " ".join(xxx[:2]) in data_yes["Name"]:
                compatibility_score += 6 * word[0][1]*(word[0][1]+word[1][1])/2
            if " ".join(xxx[1:]) in data_yes["Name"]:
                compatibility_score += 6 * word[1][1]*(word[1][1]+word[2][1])/2
            if word[0][0] in data_yes["Name"]:
                compatibility_score += 4 * word[0][1]
            if word[1][0] in data_yes["Name"]:
                compatibility_score += 4 * word[1][1]
            if word[2][0] in data_yes["Name"]:
                compatibility_score += 4 * word[2][1]
            compatibility_score += (data_yes["Description"].count(trigram) * 8 / len(data_yes["Description"])) *(word[0][1]+word[1][1]+word[2][1])/3
            compatibility_score += ((data_yes["Description"].count(word[0][0]) *word[0][1]* 2 + data_yes["Description"].count(word[1][0]) *word[1][1] *2 + data_yes["Description"].count(word[2][0]) *word[2][1]* 2) / len(data_yes["Description"]))
        else:
            for i in range(len(word) - 2):
                 xxx = []
                 for j in range(3):
                     xxx.append( word[i+j][0])
                     if(i==1):
                         pass
                 trigram = " ".join(xxx)
                 if trigram in data_yes["Name"]:
                    compatibility_score += 10 * (word[i][1]+word[i+1][1]+word[i+2][1])/3
                 if " ".join(xxx[:2]) in data_yes["Name"]:
                    compatibility_score += 4 * (word[i][1]+word[i+1][1])/2
                 if " ".join(xxx[1:]) in data_yes["Name"]:
                    compatibility_score += 4 * (word[i+1][1]+word[i+2][1])/2
                 if word[i][0] in data_yes["Name"]:
                    compatibility_score += 3 * word[i][1]
                 if word[i+1][0] in data_yes["Name"]:
                    compatibility_score += 3 * word[i+1][1]
                 if word[i+2][0] in data_yes["Name"]:
                    compatibility_score += 3 * word[i+2][1]
                 compatibility_score += (data_yes["Description"].count(trigram) * 6 / len(data_yes["Description"])) *(word[i][1]+word[i+1][1]+word[i+2][1])/3
                 compatibility_score += ((data_yes["Description"].count(word[i][0]) *word[i][1]* 1.5 + data_yes["Description"].count(word[i+1][0]) *word[i+1][1]* 1.5 + data_yes["Description"].count(word[i+2][0]) *word[i+2][1]* 1.5) / len(data_yes["Description"]))
    
    return compatibility_score

def mainfunction(naic4, input):  
    input_text = preprocess_text(input["Generated_Buisness_tag"])
    input_segments = input_text.split("|")
    input_cat = preprocess_text(input["Category"]).split(" ")
    input_des = preprocess_text(input["Genereted_Description"]).split(" ")
    dobblist = [[] for _ in range(len(input_segments))]  # Initialize as list of lists
    dobblist1 = [[] for _ in range(len(input_cat))]  # Initialize as list of lists
    dobblist2 = [[] for _ in range(len(input_des))]  # Initialize as list of lists

    for i, segment in enumerate(input_segments):
        words = segment.split(" ")
        for word in words:
            if word in good_text and word != '':
                dobblist[i].append((word, 5))
            elif word != '':
                dobblist[i].append((word, 1))
    for i, segment in enumerate(input_cat):
        words = segment.split(" ")
        for word in words:
            if word in good_text and word != '':
                dobblist1[i].append((word, 5))
            elif word != '':
                dobblist1[i].append((word, 1))
    for i, segment in enumerate(input_des):
        words = segment.split(" ")
        for word in words:
            if word in good_text and word != '':
                dobblist2[i].append((word, 5))
            elif word != '':
                dobblist2[i].append((word, 1))

   

    if naic4 > 999:
        frecV = [0] * 100
        data_not = data_dict_not[str(naic4)]["Name"]
        for i in range(100):
            if i == 40:
                pass
            naic6 = naic4 * 100 + i
            if str(naic6) in data_dict.keys():
                frecV[i] += calculate_compatibility_score_tab(data_dict[str(naic6)], data_not, dobblist)
                +calculate_compatibility_score_tab(data_dict[str(naic6)], data_not, dobblist1)*1/100+calculate_compatibility_score_tab(data_dict[str(naic6)], data_not, dobblist2)*1/10000
        return int(f"{naic4}{frecV.index(max(frecV))}")
    else:
        dict345=[]
        if  naic4 //10 == 32:
            dict345 = keys_starting_with_32
        elif naic4 //10 == 42:
            dict345 = keys_starting_with_42
        elif naic4 //10 == 54:
            dict345 = keys_starting_with_54
        frecV = [0] * 10000
        for keys in dict345:
                 frecV[int(keys)%10000]+=calculate_compatibility_score_tab(data_dict[keys],"", dobblist)
        
        return int(f"{naic4//10}{frecV.index(max(frecV))}")
        

