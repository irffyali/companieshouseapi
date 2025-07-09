##load data py
import pandas as pd

rename_dict ={
    'RegAddress.PostCode':'postcode',
    'CompanyName': 'company_name',
    'CompanyNumber':'company_number',
    'IncorporationDate':'incorporation_date',
    'DissolutionDate':'dissolution_date'
        } 


def truncate_by_length(postcode):
    if len(postcode) == 7:
        return postcode[:4]
    elif len(postcode) == 6:
        return postcode[:3]
    elif len(postcode)==5:
        return postcode[:2]
    return postcode 

def load_data():
    
    df = pd.read_csv("C:/Users/irffy/Documents/Learning/Companies_House_API/companies.csv", engine="pyarrow")
    df.columns = df.columns.str.strip()

    df = df.rename(columns=rename_dict)
    df["postcode_prefix"] = df['postcode'].apply(truncate_by_length).str.strip() 
    df.columns = [
    f"sic_code{col.split('_')[-1]}"
    if col.startswith("SICCode.SicText_") else col
    for col in df.columns
    ]






    return df


