import numpy as np
from joblib import load
import streamlit as st
import pandas as pd
from sklearn import preprocessing
from PIL import Image

# Loading the saved model
loaded_model = load('uk.joblib')

# Function for prediction
def intrusion_prediction(input_data):
    predictions = []

    # Reshape the input data for prediction
    input_data_reshaped = input_data.values.reshape(-1, 1)

    prediction = loaded_model.predict(input_data_reshaped)

    for i, result in enumerate(prediction):
        if result == 0:
            predictions.append(('normal', f'The network activity in row {i+1} is normal'))
        else:
            predictions.append(('intrusion', f'The network activity in row {i+1} is an intrusion'))

    return predictions

def main():
    # Set page configuration
    #st.set_page_config(layout="wide")

    # Load background image
    background_image = Image.open("Cyber-Security.png")
    # Resize image to desired dimensions
    resized_image = background_image.resize((300, 100))
    st.image(resized_image, use_column_width=True)

    # Adding styling for the title
    st.markdown(
        """
        <style>
        .title-box {
            background-color: rgba(255, 255, 255, 0.7); /* Set background color with transparency */
            padding: 10px; /* Add padding */
            border-radius: 5px; /* Add border radius */
            margin-bottom: 20px; /* Add margin */
            display: flex; /* Use flexbox for centering */
            justify-content: center; /* Horizontally center the content */
            align-items: center; /* Vertically center the content */
        }
        .title {
            text-align: center; /* Center the text */
        }
        .intrusion {
            color: red; /* Set text color to red for intrusion */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Creating a box around the title
    st.markdown('<div class="title-box"><h1 class="title">Network Intrusion Detection Web App</h1></div>', unsafe_allow_html=True)
    

    # Upload data file
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

    if uploaded_file is not None:
        # Read uploaded data
        data = pd.read_csv(uploaded_file)
        st.write(data)

        # Code for prediction
        diagnosis = ''
        # Creating a button for prediction
        if st.button('Check Network Activity'):
            predictions = intrusion_prediction(data)
            for status, prediction in predictions:
                if status == 'intrusion':
                    st.markdown(f'<span class="intrusion">{prediction}</span>', unsafe_allow_html=True)
                else:
                    st.success(prediction)

if __name__ == '__main__':
    main()