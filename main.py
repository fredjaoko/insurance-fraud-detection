from fastapi import FastAPI, APIRouter, Depends, HTTPException, status
import uvicorn
from insurancefraud import Insurance
import numpy as np
import pandas as pd
import pickle


app = FastAPI()
pickle_in = open('model.pkl', 'rb')
classifier = pickle.load(pickle_in)

@app.get("/")
def index():
    return {"message": "Hello World"}


@app.get("/welcome")
def get_name(name: str):
    return {"message": "Hello {name}"}

@app.post("/predict")
def predict(data: Insurance):
    data = pd.dataframe(data)

    #preprocessing

    # extracting categorical columns
    cat_df = data.select_dtypes(include = ['object'])

    #encoding the categorical columns
    cat_df = pd.get_dummies(cat_df, drop_first = True)

    # extracting the numerical columns

    num_df = data.select_dtypes(include = ['int'])

    # combining the Numerical and Categorical dataframes to get the final dataset

    X = pd.concat([num_df, cat_df], axis = 1)


    #prediction
    samples_to_predict = np.array(X)

    predictions = classifier.predict(samples_to_predict)

    return {"predictions": predictions.tolist()}







if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)