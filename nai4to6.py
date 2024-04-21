import json
from functions import preprocess_text
with open("naics6.json", "r") as json_file:
        data_dict = json.load(json_file)
with open("naics4.json","r") as json_file_2:
        data_dict_not = json.load(json_file_2)
good_text = preprocess_text("Used used junk recyable")
print(good_text)
def calculate_compatibility_score_tab(data_yes, data_not, input_str):
    compatibility_score = 0
    # Split the input string into a list of items
    input_list = input_str.split(" | ")

    # Remove words from each item in the input list that appear in data_not
    cleaned_input_list = []
    for item in input_list:
        cleaned_item = ' '.join([word for word in item.split() if word.lower() not in data_not.lower()])
        cleaned_input_list.append(cleaned_item)
    for words in cleaned_input_list:
        var=1
        if any(word in good_text for word in words):
            print(words)
            var=15
        if len(words) == 1:
             if words in data_yes["Name"]:
                  compatibility_score+=8*var
             compatibility_score+=(data_yes["Description"].count(words)*4 /len(data_yes["Description"]))*var
        elif len(words) == 2:                 
              word = str(words[0]) + " " + str(words[1])
              if word in data_yes["Name"]:
                  compatibility_score+=12*var
              if word[0] in data_yes["Name"]:
                   compatibility_score+=4*var
              if word[1] in data_yes["Name"]:
                   compatibility_score+=4*var
              compatibility_score+=(data_yes["Description"].count(word)*6 /len(data_yes["Description"]))*var
              compatibility_score+=((data_yes["Description"].count(words[0])*2+data_yes["Description"].count(words[1])*2) /len(data_yes["Description"]))*var
        elif len(words) == 3:
            word = str(words[0]) + " " + str(words[1]) + " " + str(words[2])
            if word in data_yes["Name"]:
                compatibility_score += 16*var
            if str(words[0]) + " " + str(words[1]) in data_yes["Name"]:
                compatibility_score += 6*var
            if str(words[1]) + " " + str(words[2]) in data_yes["Name"]:
                compatibility_score += 6*var
            if str(words[0]) + " " + str(words[2]) in data_yes["Name"]:
                compatibility_score += 6*var
            if words[0] in data_yes["Name"]:
                compatibility_score += 4*var
            if words[1] in data_yes["Name"]:
                compatibility_score += 4*var
            if words[2] in data_yes["Name"]:
                compatibility_score += 4*var
            compatibility_score += (data_yes["Description"].count(word) * 8 / len(data_yes["Description"]))*var
            compatibility_score += ((data_yes["Description"].count(words[0]) * 2 + data_yes["Description"].count(words[1]) * 2 + data_yes["Description"].count(words[2]) * 2) / len(data_yes["Description"]))*var
        else:
            for i in range(len(words)-2):
                word = str(words[i]) + " " + str(words[i+1]) + " " + str(words[i+2])
                if word in data_yes["Name"]:
                    compatibility_score += 10
                if str(words[i]) + " " + str(words[i+1]) in data_yes["Name"]:
                    compatibility_score += 4
                if str(words[i+1]) + " " + str(words[i+2]) in data_yes["Name"]:
                    compatibility_score += 4
                if str(words[i]) + " " + str(words[i+2]) in data_yes["Name"]:
                    compatibility_score += 4
                if words[0] in data_yes["Name"]:
                    compatibility_score += 3
                if words[i+1] in data_yes["Name"]:
                    compatibility_score += 3
                if words[i+2] in data_yes["Name"]:
                    compatibility_score += 3
                compatibility_score += (data_yes["Description"].count(word) * 6 / len(data_yes["Description"]))
                compatibility_score += ((data_yes["Description"].count(words[i]) * 1.5 + data_yes["Description"].count(words[i+1]) * 1.5 + data_yes["Description"].count(words[i+2]) * 1.5) / len(data_yes["Description"]))
    return compatibility_score
             
                  
             

def mainfunction(naic4, input):        
    if naic4 > 999 :
        frecV =[0]*100
        data_not = data_dict_not[str(naic4)]["Name"]
        for i in range(100):
              naic6 = naic4*100+i
              if str(naic6) in data_dict.keys():
                frecV[i]+=calculate_compatibility_score_tab(data_dict[str(naic6)],data_not,preprocess_text(input["Generated_Buisness_tag"]))
        print(frecV)
        print("Maximum value in frecV:", max(frecV))
        print("Index of the maximum value in frecV:", f"{naic4}{frecV.index(max(frecV))}")
    else:
        print("Error")

                    


    