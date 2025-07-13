##load data py
import pandas as pd
from cleanco import basename

rename_dict ={
    'RegAddress.PostCode':'postcode',
    'CompanyName': 'company_name',
    'CompanyNumber':'company_number',
    'IncorporationDate':'incorporation_date',
    'DissolutionDate':'dissolution_date'
        } 


def truncate_by_length(postcode):
    if postcode is None:
        return ""
    if len(postcode) == 7:
        return postcode[:4]
    elif len(postcode) == 6:
        return postcode[:3]
    elif len(postcode)==5:
        return postcode[:2]
    return postcode 

def get_data():
    
    df = pd.read_csv("../data/companies.csv", engine="pyarrow")
    df.columns = df.columns.str.strip()

    df = df.rename(columns=rename_dict)
    df["postcode_prefix"] = df["postcode"].apply(truncate_by_length).str.strip() 
    df.columns = [
    f"sic_code{col.split('_')[-1]}"
    if col.startswith("SICCode.SicText_") else col
    for col in df.columns
    ]
    
    df['incorporation_date'] = pd.to_datetime(df['incorporation_date'])
    df['companies_cleaned'] = df['company_name'].apply(basename)




    return df


