def list_to_dict(list):

    dict={}
    dict['Company_ID'] = list[0]
    dict['Company_Name'] = list[1]
    dict['Domain'] = list[2]
    dict['Category'] = list[8]
    dict['Google_Label'] = list[9]
    dict['Linkedin_Label'] = list[10]
    dict['Facebook_Label']  = list[11]
    dict['Business_Model'] = list[12]
    dict['Genereted_Description'] = list[14]
    dict['Generated_Buisness_tag'] = list[15]
    dict['Short_Description'] = list[16]
    dict['Long_Description'] = list[17]
    dict['Legal_Name'] = list[20]
    dict['Facebook_Link'] = list[24]
    dict['Linkedin_Link'] = list[25]
    return dict

def from_name_to_Naics2(name):
    if(name == "Manufacturing"):
        return 32
    if(name=="Services"):
        return 54
    return 42