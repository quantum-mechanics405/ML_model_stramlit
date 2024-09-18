import streamlit as st
import pickle
# Load the model from the file
with open(r'california_housing_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)
st.title('Prediction of Logistic regression')
c1, c2, c3 = st.columns([1,1,1])
C1 = c1.number_input('MedInc',value=3.8125)
C2 = c2.number_input('HouseAge',value=49)
C3 = c3.number_input('AveRooms',value=4.47)

c1, c2, c3 = st.columns([1,1,1])
C4 = c1.number_input('AveOccup',value=1.0410)
C5 = c2.number_input('Latitude',value=37.88)
C6 = c3.number_input('Longitude',value=-122.23)

c1, c2, c3 = st.columns([1,1,1])
C7 = c1.number_input('Population',value=33.77)
C8 = c2.number_input('Households',value=118.16)
X_new = [[C1,C2,C3,C4,C5,C6,C7,C8]]

predictions = loaded_model.predict(X_new)
if st.button('Predict'):
    st.success(f'Estimated cost is {predictions}$')
