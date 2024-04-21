import pandas as pd
from functions import list_to_dict as ltd, from_name_to_Naics2 as fnn, RecuresionOfMediumErorr, clear_console
from nai2to4 import mainfunction as naicstr4
from nai4to6 import mainfunction as naicstr6
from tqdm import tqdm
import progressbar
import time

def main():
    df = pd.read_csv("../NAICS6_Classification.csv")

    id_list = ["ID"]
    Naics_list = ["Naics"]
    with tqdm(total=len(df), desc="Processing", position=1, dynamic_ncols=True) as pbar:
        for index, rows in df.iterrows():
            CompanyList = []
            for data in rows:
                CompanyList.append(data)
            CompanyImpData = ltd(CompanyList)
            Id = CompanyImpData["Company_ID"]
            Name = CompanyImpData["Company_Name"]
            valueC2 = fnn(CompanyImpData["Business_Model"])
            id_list.append(Id)
            valueC4 = naicstr4(valueC2, CompanyImpData)
            valueC6 = naicstr6(valueC4, CompanyImpData)
            while valueC6 < 99999:
                valueC6 = RecuresionOfMediumErorr(valueC6)
            Naics_list.append(str(valueC6))
            pbar.update(1)  # Update tqdm progress bar

    output_df = pd.DataFrame({"Id": id_list, "Naics": Naics_list})
    output_df.to_excel("../output.xlsx", index=False)

if __name__ == "__main__":
    main()
