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

    # Numeric Inputs
    age = st.number_input("Age", min_value=1, max_value=100, step=1)
    bp = st.number_input("Blood Pressure (mm Hg)", min_value=50, max_value=180, step=1)
    sg = st.number_input("Specific Gravity", min_value=1.005, max_value=1.025, step=0.001, format="%.3f")
    al = st.number_input("Albumin", min_value=0, max_value=5, step=1)
    su = st.number_input("Sugar", min_value=0, max_value=5, step=1)
    bgr = st.number_input("Blood Glucose Random (mg/dL)", min_value=50, max_value=500, step=1)
    bu = st.number_input("Blood Urea (mg/dL)", min_value=1, max_value=300, step=1)
    sc = st.number_input("Serum Creatinine (mg/dL)", min_value=0.1, max_value=15.0, step=0.1)
    sod = st.number_input("Sodium (mEq/L)", min_value=100, max_value=150, step=1)
    pot = st.number_input("Potassium (mEq/L)", min_value=2.5, max_value=7.0, step=0.1)
    hemo = st.number_input("Hemoglobin (g/dL)", min_value=3.0, max_value=17.5, step=0.1)
    pcv = st.number_input("Packed Cell Volume (%)", min_value=10, max_value=55, step=1)
    wc = st.number_input("White Blood Cell Count (/mm³)", min_value=3000, max_value=20000, step=100)
    rc = st.number_input("Red Blood Cell Count (millions/μL)", min_value=2.0, max_value=6.5, step=0.1)

    # Categorical Inputs
    rbc = st.selectbox("Red Blood Cells", options=["Select...", "normal", "abnormal"])
    pc = st.selectbox("Pus Cell", options=["Select...", "normal", "abnormal"])
    pcc = st.selectbox("Pus Cell Clumps", options=["Select...", "present", "not present"])
    ba = st.selectbox("Bacteria", options=["Select...", "present", "not present"])
    htn = st.selectbox("Hypertension", options=["Select...", "yes", "no"])
    dm = st.selectbox("Diabetes Mellitus", options=["Select...", "yes", "no"])
    cad = st.selectbox("Coronary Artery Disease", options=["Select...", "yes", "no"])
    appet = st.selectbox("Appetite", options=["Select...", "good", "poor"])
    pe = st.selectbox("Pedal Edema", options=["Select...", "yes", "no"])
    ane = st.selectbox("Anemia", options=["Select...", "yes", "no"])
 
    if st.button("Load Results"):
        if (
            rbc == "Select..." or pc == "Select..." or pcc == "Select..."
            or ba == "Select..." or htn == "Select..." or dm == "Select..."
            or cad == "Select..." or appet == "Select..." or pe == "Select..."
            or ane == "Select..."
        ):
            st.error("Please select all categorical values (no 'Select...').")
        else:
            input_data = pd.DataFrame([{
                "age": age,
                "bp": bp,
                "sg": sg,
                "al": al,
                "su": su,
                "rbc": rbc,
                "pc": pc,
                "pcc": pcc,
                "ba": ba,
                "bgr": bgr,
                "bu": bu,
                "sc": sc,
                "sod": sod,
                "pot": pot,
                "hemo": hemo,
                "pcv": pcv,
                "wc": wc,
                "rc": rc,
                "htn": htn,
                "dm": dm,
                "cad": cad,
                "appet": appet,
                "pe": pe,
                "ane": ane
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

# Run standalone
if __name__ == "__main__":
    show()
