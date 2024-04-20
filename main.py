import pandas as pd
from functions import list_to_dict as ltd ,from_name_to_Naics2 as fnn

df = pd.read_csv("../NAICS6_Classification.csv")
#df.iloc[1:].iterrows()
id_list = ["ID"]
name_list = ["Name"]
Naics_list =["Naics"]

for index,rows in df.iterrows(): 
    CompanyList = []
    for data in rows:
        CompanyList.append(data)
    CompanyImpData = ltd(CompanyList)
    Id=CompanyImpData["Company_ID"]
    Name=CompanyImpData["Company_Name"]
    valueC2 = fnn(CompanyImpData["Business_Model"])
    id_list.append(Id)
    name_list.append(Name)
    Naics_list.append(valueC2)
    
output_df = pd.DataFrame({"Id": id_list, "Name": name_list,"Naics": Naics_list})

# Write DataFrame to Excel
output_df.to_excel("../output.xlsx", index=False)

