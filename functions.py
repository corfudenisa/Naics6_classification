def list_to_dict(list):

    dict={}
    dict['Company_ID'] = list[1]
    dict['Company_Name'] = list[2]
    dict['Domain'] = list[3]
    dict['Category'] = list[9]
    dict['Google_Label'] = list[10]
    dict['Linkedin_Label'] = list[11]
    dict['Facebook_Label']  = list[12]
    dict['Buisness_Model'] = list[13]
    dict['Genereted_Description'] = list[15]
    dict['Generated_Buisness_tag'] = list[16]
    dict['Short_Description'] = list[17]
    dict['Long_Description'] = list[18]
    dict['Legal_Name'] = list[21]
    dict['Facebook_Link'] = list[25]
    dict['Linkedin_Link'] = list[26]
    return dict
