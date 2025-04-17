import streamlit as st
import pandas as pd
import joblib

# Load heart disease model
@st.cache_resource
def load_model():
    return joblib.load("best_heart_disease_model.pkl")

model = load_model()

# Recommendation plans
def show_recommendations(high_risk: bool):
    if high_risk:
        st.markdown('<div class="rec-box high-risk">', unsafe_allow_html=True)
        st.markdown("### High-Risk Heart Disease Recommendation Plan")
        st.write("""
        For patients at **high risk** of heart disease, immediate action is essential to prevent or manage the condition.
        """)
        st.markdown("#### 1️⃣ Lifestyle Changes")
        st.write("""
        - Establish a consistent routine for **eating, sleeping, and exercising** to support heart health.
        - Recommend **stress reduction strategies** such as meditation, deep breathing, or relaxation techniques.
        - Advise **quitting smoking** and **limiting alcohol consumption** to reduce cardiovascular risks.
        - Emphasize the importance of **quality sleep (7–9 hours per night)** for overall heart health.
        """)
        st.markdown("#### 2️⃣ Diet & Nutrition")
        st.write("""
        - Encourage a **heart-healthy diet** rich in fruits, vegetables, whole grains, and lean proteins.
        - Recommend reducing **saturated fat intake** and replacing it with **healthy fats** (e.g., olive oil, nuts, avocado).
        - Advise limiting **processed foods, refined sugars, and salt** to maintain healthy blood pressure and cholesterol levels.
        - Increase **fiber intake** with foods like oats, beans, and vegetables to help lower cholesterol.
        - Recommend moderate intake of **omega-3 fatty acids** (e.g., salmon, flaxseeds) to support heart function.
        """)
        st.markdown("#### 3️⃣ Exercise & Physical Activity")
        st.write("""
        - Advise at least **150 minutes of moderate-intensity aerobic exercise per week** (e.g., walking, cycling, swimming).
        - Include **strength training exercises twice a week** to improve cardiovascular health and muscle strength.
        - Encourage **daily movement**, such as walking after meals or using stairs instead of elevators.
        """)
        st.markdown("#### 4️⃣ Monitoring & Tracking")
        st.write("""
        - Monitor **blood pressure regularly** to ensure it stays within a healthy range.
        - Check **cholesterol levels frequently** to track and manage LDL and HDL levels.
        - Keep track of **weight and BMI** to maintain a healthy body weight and reduce heart disease risk.
        - Log **food intake and physical activity** to stay accountable and ensure adherence to a heart-healthy lifestyle.
        """)
        st.markdown("#### 5️⃣ Next Steps")
        st.write("""
        - Schedule **follow-up appointments with a cardiologist** for further heart disease risk assessment.
        - Order routine **blood tests** (lipid profile, blood pressure check, glucose test).
        - Work with a **nutritionist or dietitian** to develop a personalized heart-healthy meal plan.
        - Consider joining a **cardiac rehabilitation program** or support group for guidance and motivation.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="rec-box low-risk">', unsafe_allow_html=True)
        st.markdown("### Low-Risk Heart Disease Recommendation Plan")
        st.write("""
        Even if not **high risk**, it's essential for the patient to maintain a healthy lifestyle to prevent future risks.
        """)
        st.markdown("#### 1️⃣ Lifestyle Changes")
        st.write("""
        - Encourage maintaining an **active lifestyle** with regular exercise and balanced meals.
        - Suggest **stress management practices** such as relaxation techniques or engaging in enjoyable hobbies.
        - Reinforce the importance of **good sleep habits (7–9 hours)** to support overall heart health.
        """)
        st.markdown("#### 2️⃣ Diet & Nutrition")
        st.write("""
        - Recommend a **balanced diet** high in fiber, lean proteins, and healthy fats to support cardiovascular health.
        - Advise limiting **processed foods and sugary snacks** that may lead to weight gain and higher cholesterol.
        - Stay **hydrated** by drinking plenty of water throughout the day to support optimal blood circulation.
        - Practice **portion control** to prevent overeating and maintain a healthy weight.
        """)
        st.markdown("#### 3️⃣ Exercise & Physical Activity")
        st.write("""
        - Encourage at least **30 minutes of physical activity per day** (e.g., walking, swimming, or cycling).
        - Include a mix of **aerobic exercise and strength training** to maintain a healthy heart and strong muscles.
        - Consider **flexibility and balance exercises** (e.g., yoga) to improve overall health and well-being.
        """)
        st.markdown("#### 4️⃣ Monitoring & Tracking")
        st.write("""
        - Schedule **annual checkups** to monitor blood pressure, cholesterol levels, and overall heart health.
        - Track **BMI and weight** to avoid gradual unhealthy weight gain, which may increase heart disease risk.
        - Stay mindful of any **signs or symptoms** like chest discomfort, shortness of breath, or fatigue, which could signal heart issues.
        """)
        st.markdown("#### 5️⃣ Next Steps")
        st.write("""
        - Continue with **healthy habits**, and make gradual improvements where needed.
        - Keep track of any **family history of heart disease** and ensure regular screenings.
        - Learn more about **heart-healthy nutrition and fitness strategies** to stay proactive about your health.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

# Main view
def show():
    st.title("🫀 Heart Disease Risk Predictor")
    st.markdown("Enter the following medical information to get your estimated risk of heart disease.")

    # Sidebar inputs
    st.sidebar.subheader("Patient Info")
    age = st.sidebar.number_input("Age", min_value=0, max_value=120, step=1)
    resting_blood_pressure = st.sidebar.number_input("Resting Blood Pressure", min_value=0, max_value=200, step=1)
    bmi = st.sidebar.number_input("BMI", min_value=0.0, max_value=50.0, step=0.1)

    if st.sidebar.button("Predict Heart Disease Risk"):
        input_data = pd.DataFrame([{
            "Age": age,
            "RestingBloodPressure": resting_blood_pressure,
            "BMI": bmi,
        }])

        prediction_proba = model.predict_proba(input_data)[0][1]
        prediction_score = int(prediction_proba * 100)
        high_risk = prediction_score >= 75

        st.markdown("### Heart Disease Risk Score:")
        st.metric(label="Score", value=f"{prediction_score}%")
        st.progress(prediction_score)

        if high_risk:
            st.markdown("<h4 style='color: red; text-align:center;'>Patient at <strong>high risk</strong> for heart disease.</h4>", unsafe_allow_html=True)
        else:
            st.markdown("<h4 style='color: green; text-align:center;'>Patient at <strong>low to medium risk</strong> for heart disease.</h4>", unsafe_allow_html=True)

        show_recommendations(high_risk)
    else:
        st.info("Use the sidebar to input data and run prediction.")

# For standalone testing
if __name__ == "__main__":
    show()








# import streamlit as st
# import pandas as pd 

# def show_recommendations(high_risk: bool):
#     if high_risk:
#         st.markdown('<div class="rec-box high-risk">', unsafe_allow_html=True)
#         st.markdown("### High-Risk Heart Disease Recommendation Plan")
#         st.write("""
#         For patients at **high risk** of heart disease, immediate action is essential to prevent or manage the condition.
#         """)
     
#         st.markdown("#### 1️⃣ Lifestyle Changes")
#         st.write("""
#         - Establish a consistent routine for **eating, sleeping, and exercising** to support heart health.
#         - Recommend **stress reduction strategies** such as meditation, deep breathing, or relaxation techniques.
#         - Advise **quitting smoking** and **limiting alcohol consumption** to reduce cardiovascular risks.
#         - Emphasize the importance of **quality sleep (7–9 hours per night)** for overall heart health.
#         """)
     
#         st.markdown("#### 2️⃣ Diet & Nutrition")
#         st.write("""
#         - Encourage a **heart-healthy diet** rich in fruits, vegetables, whole grains, and lean proteins.
#         - Recommend reducing **saturated fat intake** and replacing it with **healthy fats** (e.g., olive oil, nuts, avocado).
#         - Advise limiting **processed foods, refined sugars, and salt** to maintain healthy blood pressure and cholesterol levels.
#         - Increase **fiber intake** with foods like oats, beans, and vegetables to help lower cholesterol.
#         - Recommend moderate intake of **omega-3 fatty acids** (e.g., salmon, flaxseeds) to support heart function.
#         """)
     
#         st.markdown("#### 3️⃣ Exercise & Physical Activity")
#         st.write("""
#         - Advise at least **150 minutes of moderate-intensity aerobic exercise per week** (e.g., walking, cycling, swimming).
#         - Include **strength training exercises twice a week** to improve cardiovascular health and muscle strength.
#         - Encourage **daily movement**, such as walking after meals or using stairs instead of elevators.
#         """)
     
#         st.markdown("#### 4️⃣ Monitoring & Tracking")
#         st.write("""
#         - Monitor **blood pressure regularly** to ensure it stays within a healthy range.
#         - Check **cholesterol levels frequently** to track and manage LDL and HDL levels.
#         - Keep track of **weight and BMI** to maintain a healthy body weight and reduce heart disease risk.
#         - Log **food intake and physical activity** to stay accountable and ensure adherence to a heart-healthy lifestyle.
#         """)
     
#         st.markdown("#### 5️⃣ Next Steps")
#         st.write("""
#         - Schedule **follow-up appointments with a cardiologist** for further heart disease risk assessment.
#         - Order routine **blood tests** (lipid profile, blood pressure check, glucose test).
#         - Work with a **nutritionist or dietitian** to develop a personalized heart-healthy meal plan.
#         - Consider joining a **cardiac rehabilitation program** or support group for guidance and motivation.
#         """)
#         st.markdown('</div>', unsafe_allow_html=True)
     
#     else:
#         st.markdown('<div class="rec-box low-risk">', unsafe_allow_html=True)
#         st.markdown("### Low-Risk Heart Disease Recommendation Plan")
#         st.write("""
#         Even if not **high risk**, it's essential for the patient to maintain a healthy lifestyle to prevent future risks.
#         """)
     
#         st.markdown("#### 1️⃣ Lifestyle Changes")
#         st.write("""
#         - Encourage maintaining an **active lifestyle** with regular exercise and balanced meals.
#         - Suggest **stress management practices** such as relaxation techniques or engaging in enjoyable hobbies.
#         - Reinforce the importance of **good sleep habits (7–9 hours)** to support overall heart health.
#         """)
     
#         st.markdown("#### 2️⃣ Diet & Nutrition")
#         st.write("""
#         - Recommend a **balanced diet** high in fiber, lean proteins, and healthy fats to support cardiovascular health.
#         - Advise limiting **processed foods and sugary snacks** that may lead to weight gain and higher cholesterol.
#         - Stay **hydrated** by drinking plenty of water throughout the day to support optimal blood circulation.
#         - Practice **portion control** to prevent overeating and maintain a healthy weight.
#         """)
     
#         st.markdown("#### 3️⃣ Exercise & Physical Activity")
#         st.write("""
#         - Encourage at least **30 minutes of physical activity per day** (e.g., walking, swimming, or cycling).
#         - Include a mix of **aerobic exercise and strength training** to maintain a healthy heart and strong muscles.
#         - Consider **flexibility and balance exercises** (e.g., yoga) to improve overall health and well-being.
#         """)
     
#         st.markdown("#### 4️⃣ Monitoring & Tracking")
#         st.write("""
#         - Schedule **annual checkups** to monitor blood pressure, cholesterol levels, and overall heart health.
#         - Track **BMI and weight** to avoid gradual unhealthy weight gain, which may increase heart disease risk.
#         - Stay mindful of any **signs or symptoms** like chest discomfort, shortness of breath, or fatigue, which could signal heart issues.
#         """)
     
#         st.markdown("#### 5️⃣ Next Steps")
#         st.write("""
#         - Continue with **healthy habits**, and make gradual improvements where needed.
#         - Keep track of any **family history of heart disease** and ensure regular screenings.
#         - Learn more about **heart-healthy nutrition and fitness strategies** to stay proactive about your health.
#         """)
#         st.markdown('</div>', unsafe_allow_html=True)

 
# def show():
#     st.title("🫀 Heart Disease Risk Predictor")
 
#     st.markdown("Enter the following medical information to get your estimated risk of heart disease.")
 
#     age = st.number_input("Age", min_value=0, max_value=120, step=1)
#     resting_blood_pressure = st.number_input("Resting Blood Pressure", min_value=0, max_value=200, step=1)
#     bmi = st.number_input("BMI", min_value=0.0, max_value=50.0, step=0.1)
 
#     if st.button("Load Results"):
#         input_data = pd.DataFrame([{
#             "Age": age,
#             "RestingBloodPressure": resting_blood_pressure,
#             "BMI": bmi,
#         }])
 
#         prediction_score = 80 # todo: replace with actual model calc val
#         high_risk = prediction_score >= 75

#         st.markdown("### Heart Disease Risk Score:")
#         st.metric(label="Score", value=str(prediction_score) + "%")
#         st.progress(prediction_score)

#         if high_risk:
#             st.markdown("<h4 style='color: red; text-align:center;'>Patient at <strong>high risk</strong> for heart disease.</h3>", unsafe_allow_html=True)
#         else:
#             st.markdown("<h4 style='color: green; text-align:center;'>Patient at <strong>low to medium risk</strong> for heart disease.</h3>", unsafe_allow_html=True)

#         show_recommendations(high_risk)

        
 
# if __name__ == "__main__":
#     show()