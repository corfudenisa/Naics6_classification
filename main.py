import pandas as pd
from functions import list_to_dict as ltd
# NumberOfCmp = input("Introduceti cate fisiere firme procesam : ")

df = pd.read_csv("../NAICS6_Classification.csv")
#df.iloc[1:].iterrows()
for index,rows in df.iloc[1:6].iterrows(): 
    CompanyList = []
    for data in rows:
        CompanyList.append(data)
    print(f"Index ->{index} {CompanyList}")
    CompanyImpData = ltd(CompanyList)
    print(CompanyImpData)


# for i in range(NumberOfCmp):
