import streamlit as st
import pickle
from PIL import Image


def main():
    st.title(":blue[Bank Data Transaction Fraud Detection]")
    st.sidebar.title("Bank Data Transaction Fraud Detection")
    st.sidebar.info("Predict whether Fraud detected or Fraud not detected")
    img = Image.open("bankdata.jpg")
    st.image(img, width=500)

    gender = st.radio("Select Gender", ['Female', 'Male'])
    if gender=='Female':
        gend=0
    else:
        gend=1

    nameOrig = st.text_input('Enter your account number',"Type here")

    if nameOrig:
        account_feature = len(nameOrig)
    else:
        account_feature = 0

    amount = st.number_input('Money in this transaction')
    oldbalanceOrg = st.number_input('Balance before transaction')
    newbalanceOrig = st.number_input('Balance after transaction')
    City = st.text_input("In which city where the transaction happened?","Type here")
    if City:
        city_feature = len(City)
    else:
        city_feature = 0

    transaction_type = ['TRANSFER', 'CASH_IN', 'CASH_OUT']
    trans_type = st.selectbox("Transaction Type:", transaction_type, key="transaction_type")
    tran_type = transaction_type.index(trans_type)

    Card_type = ['Gold', 'Silver', 'Platinum', 'Signature', 'Classic']
    type_card = st.selectbox("Card Type:", Card_type, key="Card_type")
    card = Card_type.index(type_card)

    purpose_type = ['Food', 'Entertainment', 'Fuel', 'Grocery', 'Bills', 'Travel', 'Personal_Care']
    types = st.selectbox("Purpose Type:", purpose_type, key="purpose_type")
    exptype = purpose_type.index(types)

    features = [gend, account_feature, amount, oldbalanceOrg, newbalanceOrig,
                city_feature, tran_type, card, exptype]

    pred = st.button("PREDICT")

    if pred:
            scaler = pickle.load(open("scaler1.sav", 'rb'))
            model = pickle.load(open("rfmodel.sav", 'rb'))

            features_scaled = scaler.transform([features])
            prediction = model.predict(features_scaled)

            if prediction.item() == 0:
                st.success("Fraud not detected")
            else:
                st.success("Fraud detected")
main()

