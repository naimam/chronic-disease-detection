import streamlit as st
import pandas as pd 
 
def show():
    st.title("🩷 Breast Cancer Risk Predictor")
 
    st.markdown("Enter the following medical information to get your estimated risk of breast cancer.")
 
    age = st.number_input("Age", min_value=0, max_value=120, step=1)
 
    if st.button("Load Results"):
        input_data = pd.DataFrame([{
            "Age": age,
        }])
 
        prediction_score = 80 # todo: replace with actual model calc val
        high_risk = prediction_score >= 75

        st.markdown("### Breast Cancer Risk Score:")
        st.metric(label="Score", value=str(prediction_score) + "%")
        st.progress(prediction_score)

        if high_risk:
            st.markdown("<h4 style='color: red; text-align:center;'>Patient at <strong>high risk</strong> for breast cancer.</h3>", unsafe_allow_html=True)
        else:
            st.markdown("<h4 style='color: green; text-align:center;'>Patient at <strong>low to medium risk</strong> for breast cancer.</h3>", unsafe_allow_html=True)

        #show_recommendations(high_risk)

        
 
if __name__ == "__main__":
    show()