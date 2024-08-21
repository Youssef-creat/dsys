import streamlit as st
import pandas as pd
import pickle

# Load the pre-trained model
model_path = 'C:/Users/Youssef/.spyder-py3/model.pkl'
model = pickle.load(open(model_path, 'rb'))

# Streamlit app
st.title("Churn Prediction App")

# Input fields
user_id = st.text_input("User ID")
region = st.selectbox("Region", ["North", "South", "East", "West"])
tenure = st.number_input("Tenure", min_value=0)
montant = st.number_input("Montant", min_value=0.0)
frequence_rech = st.number_input("Frequence Recharge", min_value=0)
revenue = st.number_input("Revenue", min_value=0.0)
arpu_segment = st.number_input("ARPU Segment", min_value=0.0)
frequence = st.number_input("Frequence", min_value=0)
data_volume = st.number_input("Data Volume", min_value=0)
on_net = st.number_input("On Net", min_value=0)
orange = st.number_input("Orange", min_value=0)
tigo = st.number_input("Tigo", min_value=0)
zone1 = st.number_input("Zone1", min_value=0)
zone2 = st.number_input("Zone2", min_value=0)
mrg = st.number_input("MRG", min_value=0)
regularity = st.number_input("Regularity", min_value=0)
top_pack = st.selectbox("Top Pack", ["Pack1", "Pack2", "Pack3"])
freq_top_pack = st.number_input("Freq Top Pack", min_value=0)

# Button to make prediction
if st.button("Predict"):
    input_data = pd.DataFrame({
        'user_id': [user_id],
        'REGION': [region],
        'TENURE': [tenure],
        'MONTANT': [montant],
        'FREQUENCE_RECH': [frequence_rech],
        'REVENUE': [revenue],
        'ARPU_SEGMENT': [arpu_segment],
        'FREQUENCE': [frequence],
        'DATA_VOLUME': [data_volume],
        'ON_NET': [on_net],
        'ORANGE': [orange],
        'TIGO': [tigo],
        'ZONE1': [zone1],
        'ZONE2': [zone2],
        'MRG': [mrg],
        'REGULARITY': [regularity],
        'TOP_PACK': [top_pack],
        'FREQ_TOP_PACK': [freq_top_pack]
    })

    # Process and predict
    # Assuming you've encoded the categorical variables in your model
    input_data_encoded = pd.get_dummies(input_data, columns=['REGION', 'TOP_PACK'])
    prediction = model.predict(input_data_encoded)
    st.write("Prediction:", "Churn" if prediction[0] == 1 else "No Churn")
