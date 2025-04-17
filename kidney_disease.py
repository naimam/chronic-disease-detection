import streamlit as st
import pandas as pd
import joblib

# Load kidney disease model
@st.cache_resource
def load_model():
    return joblib.load("best_chronic_kidney_disease_model.pkl")

model = load_model()

def show_recommendations(high_risk: bool):
    if high_risk:
        st.markdown('<div class="rec-box high-risk">', unsafe_allow_html=True)
        st.markdown("### High-Risk Kidney Disease Recommendation Plan")
        st.write("""
        For patients at high risk of kidney disease, early intervention is crucial to prevent or manage the condition effectively.
        """)

        st.markdown("#### 1️⃣ Lifestyle Changes")
        st.write("""
        - Maintain a consistent daily routine for eating, sleeping, and exercising.
        - Quit smoking, as it can worsen kidney function.
        - Practice stress management techniques like meditation and relaxation.
        - Get regular health check-ups for early detection.
        """)

        st.markdown("#### 2️⃣ Diet & Nutrition")
        st.write("""
        - Follow a **low-sodium** diet to control blood pressure.
        - Limit **protein intake** to avoid kidney overload.
        - Increase **fiber** with fruits, veggies, and grains.
        - Stay hydrated, but balance fluids based on kidney health.
        - Avoid **phosphorus- and potassium-rich foods** if advised.
        """)

        st.markdown("#### 3️⃣ Exercise & Physical Activity")
        st.write("""
        - Get **30 minutes of moderate exercise daily**.
        - Prefer **low-impact workouts** like walking or swimming.
        - Include **light strength training** to maintain muscle health.
        """)

        st.markdown("#### 4️⃣ Monitoring & Tracking")
        st.write("""
        - Regularly check **blood pressure**.
        - Monitor **urine protein** levels.
        - Track **GFR** to assess kidney function.
        - Log **BMI and weight** to avoid obesity.
        """)

        st.markdown("#### 5️⃣ Next Steps")
        st.write("""
        - Visit a **nephrologist** for personalized care.
        - Get routine **blood tests** (e.g., creatinine, eGFR).
        - Consult a **renal dietitian** for a tailored meal plan.
        - Consider joining a **kidney care support group**.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    else:
        st.markdown('<div class="rec-box low-risk">', unsafe_allow_html=True)
        st.markdown("### Low-Risk Kidney Disease Recommendation Plan")
        st.write("""
        Even if not at high risk, maintaining kidney health is essential to prevent future complications.
        """)

        st.markdown("#### 1️⃣ Lifestyle Changes")
        st.write("""
        - Keep an active routine with good diet and sleep habits.
        - Use relaxation techniques for stress management.
        - Avoid smoking and excessive use of NSAIDs.
        """)

        st.markdown("#### 2️⃣ Diet & Nutrition")
        st.write("""
        - Eat a balanced diet with lean proteins, fruits, and vegetables.
        - Drink enough water, but don’t overhydrate.
        - Choose **low-sodium** options.
        - Limit **processed foods** and added sugars.
        """)

        st.markdown("#### 3️⃣ Exercise & Physical Activity")
        st.write("""
        - Do **30 minutes of physical activity daily**.
        - Include **aerobic and flexibility exercises**.
        - Maintain a consistent routine for cardiovascular and renal health.
        """)

        st.markdown("#### 4️⃣ Monitoring & Tracking")
        st.write("""
        - Go for **yearly kidney checkups**.
        - Keep tabs on **blood pressure and weight**.
        - Watch for early signs like swelling or fatigue.
        """)

        st.markdown("#### 5️⃣ Next Steps")
        st.write("""
        - Continue regular screening if there's a family history.
        - Get blood tests (creatinine, BUN, GFR) yearly.
        - Educate yourself about kidney health and consult doctors proactively.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

def show():
    st.title("🩺 Kidney Disease Risk Predictor")
    st.markdown("Enter the following medical information to get your estimated risk of kidney disease.")

    # Sidebar input
    st.sidebar.subheader("Patient Info")
    age = st.sidebar.number_input("Age", min_value=0, max_value=120, step=1)
    resting_blood_pressure = st.sidebar.number_input("Resting Blood Pressure", min_value=0, max_value=200, step=1)
    bmi = st.sidebar.number_input("BMI", min_value=0.0, max_value=50.0, step=0.1)

    if st.sidebar.button("Predict Kidney Disease Risk"):
        input_data = pd.DataFrame([{
            "Age": age,
            "RestingBloodPressure": resting_blood_pressure,
            "BMI": bmi,
        }])

        # Get prediction score
        prediction_proba = model.predict_proba(input_data)[0][1]
        prediction_score = int(prediction_proba * 100)
        high_risk = prediction_score >= 75

        # Output section
        st.markdown("### Kidney Disease Risk Score:")
        st.metric(label="Score", value=f"{prediction_score}%")
        st.progress(prediction_score)

        if high_risk:
            st.markdown("<h4 style='color: red; text-align:center;'>Patient at <strong>high risk</strong> for kidney disease.</h4>", unsafe_allow_html=True)
        else:
            st.markdown("<h4 style='color: green; text-align:center;'>Patient at <strong>low to medium risk</strong> for kidney disease.</h4>", unsafe_allow_html=True)

        show_recommendations(high_risk)
    else:
        st.info("Use the sidebar to input data and run prediction.")

# Run standalone
if __name__ == "__main__":
    show()




# import streamlit as st
# import pandas as pd 

# import streamlit as st

# def show_recommendations(high_risk: bool):
#     if high_risk:
#         st.markdown('<div class="rec-box high-risk">', unsafe_allow_html=True)
#         st.markdown("### High-Risk Kidney Disease Recommendation Plan")
#         st.write("""
#         For patients at high risk of kidney disease, early intervention is crucial to prevent or manage the condition effectively.
#         """)

#         st.markdown("#### 1️⃣ Lifestyle Changes")
#         st.write("""
#         - Encourage the patient to maintain a consistent daily routine for eating, sleeping, and exercising.
#         - Advise smoking cessation, as smoking can worsen kidney function.
#         - Recommend stress management techniques like meditation and relaxation exercises.
#         - Emphasize the importance of regular health check-ups and early detection of kidney issues.
#         """)

#         st.markdown("#### 2️⃣ Diet & Nutrition")
#         st.write("""
#         - Recommend a **low-sodium** diet to manage blood pressure and reduce kidney strain.
#         - Suggest **low-protein** intake to prevent kidney overload.
#         - Advise **high-fiber** foods like fruits, vegetables, and whole grains to promote overall health.
#         - Encourage **adequate hydration**, but balance fluid intake as necessary based on kidney function.
#         - Avoid foods high in **phosphorus** (e.g., dairy products, nuts) and **potassium** (e.g., bananas, tomatoes) if kidney function is significantly impaired.
#         """)

#         st.markdown("#### 3️⃣ Exercise & Physical Activity")
#         st.write("""
#         - Advise at least **30 minutes of moderate-intensity exercise** per day to improve overall health.
#         - Encourage **low-impact activities** like walking, swimming, or cycling to prevent strain on the kidneys.
#         - Recommend **strength training** a few times a week to support muscle health and reduce the risk of frailty.
#         """)

#         st.markdown("#### 4️⃣ Monitoring & Tracking")
#         st.write("""
#         - Instruct the patient to monitor **blood pressure** regularly, as high blood pressure can damage the kidneys.
#         - Advise regular **urinalysis** to track protein levels in the urine (a sign of kidney damage).
#         - Track **glomerular filtration rate (GFR)** regularly to assess kidney function.
#         - Keep track of **weight and BMI** to prevent obesity, which can worsen kidney disease.
#         """)

#         st.markdown("#### 5️⃣ Next Steps")
#         st.write("""
#         - Schedule follow-up appointments with a **nephrologist** for specialized kidney care.
#         - Get routine **blood tests** to monitor kidney function, including **serum creatinine** and **eGFR**.
#         - Work with a dietitian to create a **personalized kidney-friendly diet plan**.
#         - Consider joining a support group or kidney disease education program for guidance and motivation.
#         """)
#         st.markdown('</div>', unsafe_allow_html=True)

#     else:
#         st.markdown('<div class="rec-box low-risk">', unsafe_allow_html=True)
#         st.markdown("### Low-Risk Kidney Disease Recommendation Plan")
#         st.write("""
#         Even if not at high risk for kidney disease, the goal is to maintain kidney health and prevent future risks.
#         """)

#         st.markdown("#### 1️⃣ Lifestyle Changes")
#         st.write("""
#         - Encourage the patient to maintain a healthy and active lifestyle with balanced meals and regular exercise.
#         - Suggest stress management techniques like relaxation exercises or engaging in hobbies.
#         - Reinforce the importance of **not smoking** and maintaining healthy habits for long-term kidney health.
#         """)

#         st.markdown("#### 2️⃣ Diet & Nutrition")
#         st.write("""
#         - Recommend a **well-balanced diet** with sufficient fruits, vegetables, lean proteins, and whole grains.
#         - Advise **adequate hydration**, but avoid excessive fluid intake.
#         - Encourage **low-sodium** choices to maintain blood pressure within a healthy range.
#         - Suggest **limiting processed foods** to prevent excess salt and sugar intake.
#         """)

#         st.markdown("#### 3️⃣ Exercise & Physical Activity")
#         st.write("""
#         - Advise engaging in at least **30 minutes of physical activity per day** to support kidney and cardiovascular health.
#         - Recommend aerobic exercises such as walking, running, or swimming to improve circulation.
#         - Encourage flexibility and balance exercises to improve overall fitness.
#         """)

#         st.markdown("#### 4️⃣ Monitoring & Tracking")
#         st.write("""
#         - Encourage **annual checkups** to monitor kidney function and overall health.
#         - Track **blood pressure** regularly and maintain it within a healthy range.
#         - Stay aware of any symptoms like fatigue, swelling, or changes in urination that may signal kidney issues.
#         """)

#         st.markdown("#### 5️⃣ Next Steps")
#         st.write("""
#         - Continue healthy lifestyle practices to protect kidney health.
#         - Get regular **blood tests** to monitor kidney function, especially if there's a family history of kidney disease.
#         - Stay informed about kidney health and be proactive in seeking medical advice if any symptoms arise.
#         """)
#         st.markdown('</div>', unsafe_allow_html=True)

 
# def show():
#     st.title("🩺 Kidney Disease Risk Predictor")
 
#     st.markdown("Enter the following medical information to get your estimated risk of kidney disease.")
 
#     age = st.number_input("Age", min_value=0, max_value=120, step=1)
#     resting_blood_pressure = st.number_input("Resting Blood Pressure", min_value=0, max_value=200, step=1)
#     bmi = st.number_input("BMI", min_value=0.0, max_value=50.0, step=0.1)
 
#     if st.button("Load Results"):
#         input_data = pd.DataFrame([{
#             "Age": age,
#             "RestingBloodPressure": resting_blood_pressure,
#             "BMI": bmi,
#         }])
 
        
#         prediction_score = 30 # todo: replace with actual model calc val
#         high_risk = prediction_score >= 75

#         st.markdown("### Kidney Disease Risk Score:")
#         st.metric(label="Score", value=str(prediction_score) + "%")
#         st.progress(prediction_score)

#         if high_risk:
#             st.markdown("<h4 style='color: red; text-align:center;'>Patient at <strong>high risk</strong> for kidney disease.</h3>", unsafe_allow_html=True)
#         else:
#             st.markdown("<h4 style='color: green; text-align:center;'>Patient at <strong>low to medium risk</strong> for kidney disease.</h3>", unsafe_allow_html=True)

#         show_recommendations(high_risk)

 
# if __name__ == "__main__":
#     show()