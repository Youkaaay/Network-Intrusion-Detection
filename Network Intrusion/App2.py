import numpy as np
import pickle
import streamlit as st
import pandas as pd
from sklearn import preprocessing

# Loading the saved model
loaded_model = pickle.load(open('uk.pkl', 'rb'))

# Function for prediction
def intrusion_prediction(input_data):
    # Converting input data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # Reshaping the array for single instance prediction
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if prediction[0] == 0:
        return 'The network activity is normal'
    else:
        return 'The network activity is an intrusion'

def main():
    # Giving a title
    st.title('Network Intrusion Detection Web App')

    # Getting input data from the user
    protocol_type = st.text_input('Protocol Type')
    flag = st.text_input('Flag')
    src_bytes = st.text_input('Source Bytes')
    dst_bytes = st.text_input('Destination Bytes')
    count = st.text_input('Count')
    same_srv_rate = st.text_input('Same Service Rate')
    diff_srv_rate = st.text_input('Different Service Rate')
    dst_host_srv_count = st.text_input('Destination Host Service Count')
    dst_host_same_srv_rate = st.text_input('Destination Host Same Service Rate')
    dst_host_same_src_port_rate = st.text_input('Destination Host Same Source Port Rate')

    # Code for prediction
    diagnosis = ''

    # Creating a button for prediction
    if st.button('Check Network Activity'):
        diagnosis = intrusion_prediction([protocol_type, flag, src_bytes, dst_bytes, count, same_srv_rate, diff_srv_rate, dst_host_srv_count, dst_host_same_srv_rate, dst_host_same_src_port_rate])

    st.success(diagnosis)

if __name__ == '__main__':
    main()