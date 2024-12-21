import streamlit as st
import pandas as pd
import pickle as pk
import numpy as np
from PIL import Image
import warnings
warnings.filterwarnings("ignore")

# Load dataset for feature extraction
data_file = 'updated_pollution_dataset.csv'
data = pd.read_csv(data_file)
columns = data.columns 

# load model
with open('aqi_prediction.pkl', 'rb') as file:
    model = pk.load(file)

# Exclude target column for prediction
target_column = "Air Quality"
feature_columns = [col for col in columns if col != target_column]

def model_prediction(test_array):
    test_array = np.array(test_array).reshape(1, -1)  # Convert to 2D array
    prediction = model.predict(test_array)
    if prediction[0] == 'Hazardous':
        return "Hazardous"
    elif prediction[0] == 'Poor':
        return "Poor"
    elif prediction[0] == 'Moderate':
        return "Moderate"
    else:
        return "Good"

# Add Slidebar
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page", ["Home", "About", "AQI Categorization"])

# Home page
if app_mode == "Home":
    st.header("AQI Categorization Model")
    image_path = "aqi_image.jpeg"
    img = Image.open(image_path)
    st.image(img)
    st.markdown("""
    My intention is to make people aware of the quality of air they are breathing.
    
    ## Woking
    1. Fill all the details asked in the input sections
    2. Our system will analyze the input
    3. The prediction of the Air Quality will be displayed
    
    ## Why this model ?
    1. It predicts the results with 96.1% accuracy
    2. It has a good UI which helps easy interaction
    3. It produces efficient and fast results.
    
    ## Where to Check AQ
    Go to the **AQI Categorization** section in the Dashboard to access the AQI Class predictor model.
    
    ## About Section
    You can also access dataset, my details and other projects via **About** section in Dashboard             
    """)
    
# About page
elif(app_mode == 'About'):
    st.header("About Section")
    st.markdown("""
    #### About Dataset:
    This dataset focuses on air quality assessment across various regions. The dataset contains 5000 samples and captures critical environmental and demographic factors that influence pollution levels.            
    #### Content:
    1. Train (4000)
    2. Test (1000)
    
    #### About me:
    I'm an AI/ML anthusiast and have made several projects like- Sign Language Detction, Dog breed prediction, Feature Extractor using NLP, Diabetes prediction, etc. 
    
    #### Contact Info
    Mail: it12212043@gmail.com
    Github- https://github.com/Abhisek-Tiwari
    """)

# Prediction page
elif app_mode == "AQI Categorization":
    st.header("AQI Categorization")
    
    # Collect user inputs
    st.write("### Input Features for Prediction")
    user_inputs = {}

    for column in feature_columns:
        user_inputs[column] = st.text_input(f"Enter value for {column}:")

    # Validate inputs and convert to proper types
    input_array = []
    for column in feature_columns:
        try:
            input_array.append(float(user_inputs[column]))  # Convert all inputs to float
        except ValueError:
            st.error(f"Invalid input for {column}. Please enter a numeric value.")
            st.stop()

    # Prediction
    if st.button("Predict"):
        st.write("### Prediction Results")
        prediction_result = model_prediction(input_array)
        st.success(f"Predicted Air Quality: {prediction_result}")
    