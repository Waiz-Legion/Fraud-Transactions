import streamlit as st
from xgboost import XGBClassifier
import pickle
import random
import numpy as np

with open('best_mod.pkl', 'rb') as f:
    model = pickle.load(f)
st.title('Fake Profile Detection')

def main():
    column_names = ['Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
       'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20',
       'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount']

    inp = []
    for col in column_names:
        if col!='Time' or col!='Amount':
            t = st.text_input(col)
            inp.append(t)
    if st.button('predict'):
        pred = model.predict(np.array([inp], dtype = 'object'))
        if pred == 0:
            st.success('No Fraud')
        else:
            st.error('Fraud')





    
if __name__ == '__main__':
    main()