import streamlit as st
import pandas as pd 
 
def show():
    st.title("🩺 Kidney Disease Risk Predictor")
 
    st.markdown("Enter the following medical information to get your estimated risk of kidney disease.")
 
    age = st.number_input("Age", min_value=0, max_value=120, step=1)
    resting_blood_pressure = st.number_input("Resting Blood Pressure", min_value=0, max_value=200, step=1)
    bmi = st.number_input("BMI", min_value=0.0, max_value=50.0, step=0.1)
 
    if st.button("Load Results"):
        input_data = pd.DataFrame([{
            "Age": age,
            "RestingBloodPressure": resting_blood_pressure,
            "BMI": bmi,
        }])
 
        # st.markdown("### Your Diabetes Risk Score:")
        # st.metric(label="Score", value=str(prediction_score) + "%")
        # st.progress(prediction_score)
 
        # if high_risk:
        #     st.markdown("<h4 style='color: red; text-align:center;'>You are at <strong>high risk</strong> for diabetes.</h3>", unsafe_allow_html=True)
        # else:
        #     st.markdown("<h4 style='color: green; text-align:center;'>You are at <strong>low to medium risk</strong> for diabetes.</h3>", unsafe_allow_html=True)
 
        # show_recommendations(high_risk)
 
if __name__ == "__main__":
    show()