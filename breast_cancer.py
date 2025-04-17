import streamlit as st
import pandas as pd
import joblib

# Load the breast cancer model
@st.cache_resource
def load_model():
    return joblib.load("best_breast_cancer_model.pkl")

model = load_model()

def show_recommendations(high_risk: bool):
    if high_risk:
        st.markdown("### High-Risk Recommendation Plan")
        st.write("""
        Patients at high risk should consider the following:
        - Schedule a mammogram immediately
        - Consult a specialist for a full risk assessment
        - Discuss genetic testing if there's family history
        - Begin lifestyle changes (e.g., diet, exercise, smoking cessation)
        """)
    else:
        st.markdown("### Low-Risk Recommendation Plan")
        st.write("""
        Patients at low to medium risk should:
        - Continue regular screening based on age and guidelines
        - Maintain healthy lifestyle habits
        - Watch for symptoms and consult doctor if any arise
        """)

def show():
    st.title("🎗️ Breast Cancer Risk Predictor")
    st.markdown("Enter the following medical information to get your estimated risk of breast cancer.")

    # Sidebar inputs for now (move if needed)
    st.sidebar.subheader("Patient Info")
    age = st.sidebar.number_input("Age", min_value=0, max_value=120, step=1)

    if st.sidebar.button("Predict Breast Cancer Risk"):
        input_data = pd.DataFrame([{
            "Age": age,
        }])

        # Predict using model
        prediction_proba = model.predict_proba(input_data)[0][1]
        prediction_score = int(prediction_proba * 100)
        high_risk = prediction_score >= 75

        # Results
        st.markdown("### Breast Cancer Risk Score:")
        st.metric(label="Score", value=f"{prediction_score}%")
        st.progress(prediction_score)

        if high_risk:
            st.markdown("<h4 style='color: red; text-align:center;'>Patient at <strong>high risk</strong> for breast cancer.</h4>", unsafe_allow_html=True)
        else:
            st.markdown("<h4 style='color: green; text-align:center;'>Patient at <strong>low to medium risk</strong> for breast cancer.</h4>", unsafe_allow_html=True)

        show_recommendations(high_risk)
    else:
        st.info("Use the sidebar to input data and run prediction.")




# import streamlit as st
# import pandas as pd 
 
# def show():
#     st.title("🩷 Breast Cancer Risk Predictor")
 
#     st.markdown("Enter the following medical information to get your estimated risk of breast cancer.")
 
#     age = st.number_input("Age", min_value=0, max_value=120, step=1)
 
#     if st.button("Load Results"):
#         input_data = pd.DataFrame([{
#             "Age": age,
#         }])
 
#         prediction_score = 80 # todo: replace with actual model calc val
#         high_risk = prediction_score >= 75

#         st.markdown("### Breast Cancer Risk Score:")
#         st.metric(label="Score", value=str(prediction_score) + "%")
#         st.progress(prediction_score)

#         if high_risk:
#             st.markdown("<h4 style='color: red; text-align:center;'>Patient at <strong>high risk</strong> for breast cancer.</h3>", unsafe_allow_html=True)
#         else:
#             st.markdown("<h4 style='color: green; text-align:center;'>Patient at <strong>low to medium risk</strong> for breast cancer.</h3>", unsafe_allow_html=True)

#         #show_recommendations(high_risk)

        
 
# if __name__ == "__main__":
#     show()