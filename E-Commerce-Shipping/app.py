from fastapi import FastAPI,Request,Response
import uvicorn
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import pickle
import pandas as pd
from pydantic import BaseModel

app = FastAPI()

templates = Jinja2Templates(directory="templates")

with open("e_shipping_complete.pkl","rb") as f :
    save_data = pickle.load(f)
    model = save_data['model']

class Features(BaseModel):
    Warehouse_block:str
    Mode_of_Shipment:str
    Customer_care_calls:int
    Customer_rating: int
    Cost_of_the_Product:int
    Prior_purchases: int
    Product_importance:str
    Gender:str
    Discount_offered:int
    Weight_in_gms:int

@app.get("/",response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html",{"request":request})

@app.post("/predict")
async def predict(features: Features) :
    input_data = pd.DataFrame([features.model_dump()])
    print(input_data)

    prediction = model.predict(input_data)
    return {'prediction': int(prediction[0])}