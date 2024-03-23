import numpy as np
from joblib import load
import streamlit as st
import pandas as pd
from sklearn import preprocessing

# Loading the saved model
loaded_model = load('uk.joblib')

# Function for prediction
def intrusion_prediction(input_data):

    predictions = []

    # Loop over the first 10 rows of the input data
    for i in range(min(10, len(input_data))):
        # Reshape the input data for single instance prediction
        input_data_reshaped = input_data.iloc[[i]].values.reshape(1, -1)
        
        prediction = loaded_model.predict(input_data_reshaped)

        if prediction[0] == 0:
            predictions.append('The network activity in row {} is normal'.format(i+1))
        else:
            predictions.append('The network activity in row {} is an intrusion'.format(i+1))

    return predictions

def main():
    # Giving a title
    st.title('Network Intrusion Detection Web App')

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
            for prediction in predictions:
                st.success(prediction)

if __name__ == '__main__':
    main()