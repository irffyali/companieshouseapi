# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import date
from load_data import load_data
from typing import Optional

app = FastAPI(title="The Companies House API", version="0.1")
df = load_data()
# Data model for incoming POST requests
class Model(BaseModel):
    company_name: str
    postcode_prefix: str 
    postcode: str 
    company_number: str
    sic_code1: str
    sic_code2: str
    sic_code3: str
    sic_code4: str
    incorporation_date:str
    dissolution_date :Optional[str] = None

    
   

# Health check endpoint
@app.get("/company/{company_number}",response_model=Model)
async def get_company_data(company_number: str):
    result = df[df["company_number"] == company_number]
   
    if len(result)>1000: #will implement proper pagination at some point for now juat limit 1k
        result = result.head(1000)

    if result.empty:
        raise HTTPException(status_code=404, detail="Company not found")
    return Model(**result.iloc[0].to_dict())


@app.get("/postcode/{postcode}",
summary="Retrieves companies incorporated at a postcode",
 response_model=list[Model])
async def get_postcode_data(postcode: str):
    result = df[df["postcode"] == postcode]
   
    if len(result)>10000:
        result = result.head(10000)

    if result.empty:
        raise HTTPException(status_code=404, detail="Company not found")
    return [Model(**row.to_dict()) for _, row in result.iterrows()]


@app.get("/postcode_prefix/{postcode_prefix}",
summary="Retrieves companies incorporated at a postcode prefix e.g. M1",
 response_model=list[Model])
async def get_postprefix_data(postcode_prefix: str):
    result = df[df["postcode_prefix"] == postcode_prefix]
   
    if len(result)>10000:
        result = result.head(10000)

    if result.empty:
        raise HTTPException(status_code=404, detail="Company not found")
    return [Model(**row.to_dict()) for _, row in result.iterrows()]


