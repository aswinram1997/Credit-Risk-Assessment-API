import fastapi
import uvicorn
from fastapi import FastAPI, Response
from joblib import load
import pandas as pd
import tensorflow.keras as keras

app = FastAPI()

# Load the numerical imputer
try:
    num_imputer = load("model/num_imputer.joblib")
except Exception as e:
    print("Error loading numerical imputer:", str(e))
    num_imputer = None

# Load the scaler object
try:
    scaler = load("model/scaler.joblib")
except Exception as e:
    print("Error loading scaler:", str(e))
    scaler = None

# Load the encoder object
try:
    encoder = load("model/encoder.joblib")
except Exception as e:
    print("Error loading encoder:", str(e))
    encoder = None

# Load the trained DNN model
try:
    model = keras.models.load_model("model/trained_model.h5")
except Exception as e:
    print("Error loading model:", str(e))
    model = None


@app.get("/")
async def root():
    message = "The Credit Risk Assessment API is up and running!"
    return {"message": message}


@app.post("/predict")
async def predict_loan_status(data: dict):
    if num_imputer is None or scaler is None or encoder is None or model is None:
        return Response(content="Error: Model not loaded.", media_type="application/json")

    try:
        # Get the data from the request
        df = pd.DataFrame(data, index=[0])  # Specify the index explicitly

        # get numerical and categorical columns
        numerical_cols = ['person_age', 'person_income', 'person_emp_length', 'loan_amnt',
                           'loan_int_rate', 'loan_percent_income', 'cb_person_cred_hist_length']
        categorical_cols = ['person_home_ownership', 'loan_intent', 'loan_grade',
                            'cb_person_default_on_file']

        # Preprocess numerical columns
        df_imputed_num = pd.DataFrame(num_imputer.transform(df[numerical_cols]), columns=numerical_cols, index=df.index)
        df_scaled = pd.DataFrame(scaler.transform(df_imputed_num), columns=numerical_cols, index=df.index)

        # Preprocess categorical columns
        df_encoded = pd.DataFrame(encoder.transform(df[categorical_cols]).toarray(),
                                  columns=encoder.get_feature_names(categorical_cols),
                                  index=df.index)

        # Combine the preprocessed numerical and categorical columns
        df_processed = pd.concat([df_scaled, df_encoded], axis=1)

        # Default threshold value for Tensorflow Neural Nets
        threshold = 0.5

        # Make prediction using the loaded model
        prediction_proba = model.predict(df_processed)

        # Convert the probability to binary prediction
        prediction = 1 if prediction_proba[0][0] > threshold else 0

        return Response(content=str(prediction), media_type="application/json")
    
    except Exception as e:
        return Response(content=f"Error: {str(e)}", media_type="application/json")



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
