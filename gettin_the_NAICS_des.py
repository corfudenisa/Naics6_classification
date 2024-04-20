import pandas as pd
dictData={}
prefix = [32 ,42, 54]
df = pd.read_excel("../2022-NAICS-Keywords.xlsx")
for index, row in df.iloc[:6].iterrows():
    print(f"({index}, {row})")
