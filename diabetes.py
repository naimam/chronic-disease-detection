import streamlit as st
import pandas as pd
import joblib
 
@st.cache_resource
def load_model():
    return joblib.load("best_diabetes_model.pkl")
 
model = load_model()
 
def show_recommendations(high_risk: bool):
    if high_risk:
        st.markdown('<div class="rec-box high-risk">', unsafe_allow_html=True)
        st.markdown("### **High-Risk Diabetes Recommendation Plan**")
        st.write("""
        For patients at **high risk** of diabetes, immediate intervention is crucial to prevent or manage the disease effectively.
        """)

        st.markdown("#### 1️⃣ **Lifestyle Changes**")
        st.write("""
        - Encourage the patient to establish a **consistent daily routine** for eating, sleeping, and exercising.
        - Recommend **stress reduction techniques** such as mindfulness, meditation, or yoga.
        - Advise the patient to **quit smoking** and limit alcohol consumption to reduce complications.
        - Emphasize the importance of **quality sleep** (7–9 hours per night) to stabilize blood sugar levels.
        """)

        st.markdown("#### 2️⃣ **Diet & Nutrition**")
        st.write("""
        - Guide the patient to follow a **low-carb, high-fiber diet** to maintain stable blood sugar levels.
        - Recommend **whole grains** (brown rice, quinoa, whole wheat) over refined grains.
        - Advise avoiding **sugary drinks** (soda, fruit juices) and processed foods high in added sugars.
        - Suggest increasing **protein intake** (lean meats, fish, eggs, beans) to support metabolism.
        - Encourage consumption of **non-starchy vegetables** (broccoli, spinach, peppers, cucumbers).
        - Recommend **healthy fats** (avocados, nuts, olive oil) instead of trans fats.
        """)

        st.markdown("#### 3️⃣ **Exercise & Physical Activity**")
        st.write("""
        - Advise the patient to aim for **150 minutes of moderate-intensity exercise per week** (e.g., brisk walking, cycling, swimming).
        - Include **resistance training** (weight lifting, resistance bands) twice a week to improve insulin sensitivity.
        - Encourage **daily movement**, such as taking stairs instead of elevators and walking after meals.
        """)

        st.markdown("#### 4️⃣ **Monitoring & Tracking**")
        st.write("""
        - Instruct the patient to **check blood sugar levels regularly** (as per your guidance).
        - Monitor **blood pressure and cholesterol** to prevent cardiovascular complications.
        - Track **weight and BMI**, as excess weight increases diabetes risk.
        - Suggest logging **food intake and activity levels** in a journal or app for accountability.
        """)

        st.markdown("#### 5️⃣ **Next Steps**")
        st.write("""
        - Schedule **follow-up appointments** for a comprehensive diabetes risk assessment.
        - Order routine blood tests (**A1C, fasting blood sugar, cholesterol, kidney function**).
        - Collaborate with a **nutritionist or dietitian** to create a personalized meal plan for the patient.
        - Recommend joining a **support group or diabetes education program** for additional guidance and motivation.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    else:
        st.markdown('<div class="rec-box low-risk">', unsafe_allow_html=True)
        st.markdown("### **Low-Risk Diabetes Recommendation Plan**")
        st.write("""
        For patients at **low risk** of diabetes, the focus should be on maintaining good health and preventing future risks.
        """)

        st.markdown("#### 1️⃣ **Lifestyle Changes**")
        st.write("""
        - Encourage the patient to maintain a **healthy and active lifestyle** with balanced meals and regular exercise.
        - Suggest **stress management techniques** like relaxation exercises or engaging in hobbies.
        - Reinforce the importance of **good sleep habits** to support overall well-being.
        """)

        st.markdown("#### 2️⃣ **Diet & Nutrition**")
        st.write("""
        - Recommend a **balanced diet** rich in fiber, lean proteins, and healthy fats.
        - Advise avoiding **excess processed foods and sugary snacks** to prevent insulin resistance.
        - Encourage staying **hydrated** by drinking at least 8 glasses of water daily.
        - Suggest **portion control** to maintain a healthy weight and prevent future risks.
        """)

        st.markdown("#### 3️⃣ **Exercise & Physical Activity**")
        st.write("""
        - Advise the patient to engage in at least **30 minutes of physical activity per day**.
        - Recommend mixing **aerobic exercises** (walking, running, swimming) with strength training.
        - Suggest **flexibility and balance exercises** (yoga, Pilates) to improve overall health.
        """)

        st.markdown("#### 4️⃣ **Monitoring & Tracking**")
        st.write("""
        - Recommend **annual physical checkups** to monitor blood sugar, cholesterol, and blood pressure.
        - Advise tracking **BMI and weight trends** to avoid gradual unhealthy weight gain.
        - Educate the patient to stay aware of symptoms like **excessive thirst, frequent urination, or fatigue**, which could signal early diabetes signs.
        """)

        st.markdown("#### 5️⃣ **Next Steps**")
        st.write("""
        - Encourage the patient to continue **healthy habits** and make small improvements where needed.
        - Suggest routine **blood sugar screenings** (especially if there's a family history of diabetes).
        - Provide resources for learning about **nutrition and fitness** to stay proactive about health.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
 
 
def show():
    st.title("🩺 Diabetes Risk Predictor")
 
    st.markdown("Enter the following medical information to get patient's estimated risk of diabetes.")
 
    age = st.number_input("Age", min_value=0, max_value=120, step=1)
    pregnancies = st.number_input("Number of Pregnancies", min_value=0, max_value=20, step=1)
    glucose = st.number_input("Glucose Level", min_value=0, max_value=300, step=1)
    blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=200, step=1)
    skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100, step=1)
    insulin = st.number_input("Insulin Level", min_value=0, max_value=900, step=1)
    bmi = st.number_input("BMI", min_value=0.0, max_value=50.0, step=0.1)
    dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5, step=0.01)
 
    if st.button("Load Results"):
        input_data = pd.DataFrame([{
            "Pregnancies": pregnancies,
            "Glucose": glucose,
            "BloodPressure": blood_pressure,
            "SkinThickness": skin_thickness,
            "Insulin": insulin,
            "BMI": bmi,
            "DiabetesPedigreeFunction": dpf,
            "Age": age
        }])
 
        prediction_proba = model.predict_proba(input_data)[0][1]
        prediction_score = int(prediction_proba * 100)
        high_risk = prediction_score >= 75
 
        st.markdown("### Diabetes Risk Score:")
        st.metric(label="Score", value=str(prediction_score) + "%")
        st.progress(prediction_score)
 
        if high_risk:
            st.markdown("<h4 style='color: red; text-align:center;'>Patient at <strong>high risk</strong> for diabetes.</h3>", unsafe_allow_html=True)
        else:
            st.markdown("<h4 style='color: green; text-align:center;'>Patient at <strong>low to medium risk</strong> for diabetes.</h3>", unsafe_allow_html=True)
 
        show_recommendations(high_risk)
 
if __name__ == "__main__":
    show()