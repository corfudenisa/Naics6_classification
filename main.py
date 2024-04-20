import pandas as pd
import magic
from functions import list_to_dict as ltd
# NumberOfCmp = input("Introduceti cate fisiere firme procesam : ")

df = pd.read_csv("../NAICS6_Classification.csv")
#df.iloc[1:].iterrows()
for index,rows in df.iterrows(): 
    CompanyList = []
    for data in rows:
        CompanyList.append(data)
    print(f"Index ->{index} {CompanyList}")
    CompanyImpData = ltd(CompanyList)
    magic.magic_main(CompanyImpData)


# for i in range(NumberOfCmp):
