import streamlit as st
import pandas as pd 

def show_recommendations(high_risk: bool):
    if high_risk:
        st.markdown('<div class="rec-box high-risk">', unsafe_allow_html=True)
        st.markdown("### **High-Risk Breast Cancer Recommendation Plan**")
        st.write("""
        For patients at **high risk** of breast cancer, early screening and proactive lifestyle changes are essential for prevention and early detection.
        """)

        st.markdown("#### 1️⃣ **Lifestyle Changes**")
        st.write("""
        - Encourage the patient to maintain a **healthy body weight**, as obesity is a known risk factor.
        - Recommend limiting **alcohol intake** and avoiding smoking to reduce risk.
        - Promote **stress management techniques** like yoga, mindfulness, or journaling.
        - Discuss reducing exposure to **endocrine disruptors** (e.g., BPA in plastics, certain cosmetics).
        """)

        st.markdown("#### 2️⃣ **Diet & Nutrition**")
        st.write("""
        - Recommend a **plant-based, antioxidant-rich diet** including berries, leafy greens, and cruciferous vegetables (broccoli, cauliflower).
        - Suggest foods rich in **omega-3 fatty acids** (flaxseeds, walnuts, salmon) to support cellular health.
        - Limit **red and processed meats** and high-fat dairy products.
        - Encourage **fiber intake** through whole grains, fruits, and vegetables to support hormone regulation.
        """)

        st.markdown("#### 3️⃣ **Exercise & Physical Activity**")
        st.write("""
        - Advise at least **150 minutes of moderate-intensity aerobic exercise per week**.
        - Recommend adding **strength training** exercises 2–3 times a week.
        - Promote **daily movement** and limiting sedentary behavior, especially for those with desk jobs.
        """)

        st.markdown("#### 4️⃣ **Monitoring & Tracking**")
        st.write("""
        - Recommend **annual mammograms** or more frequent screenings if genetically predisposed.
        - Encourage **monthly breast self-exams** and being aware of any changes in size, shape, or feel.
        - Monitor for early signs such as lumps, skin dimpling, or nipple discharge.
        - Keep records of **family history** and genetic test results if applicable.
        """)

        st.markdown("#### 5️⃣ **Next Steps**")
        st.write("""
        - Refer to a **genetic counselor** if BRCA1/BRCA2 or other hereditary factors are suspected.
        - Discuss **chemoprevention options** or preventive surgery in high-genetic-risk cases.
        - Coordinate care with an **oncologist or breast specialist** for a tailored prevention strategy.
        - Provide resources for **support groups** and **mental health counseling** to manage anxiety or fear.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    else:
        st.markdown('<div class="rec-box low-risk">', unsafe_allow_html=True)
        st.markdown("### **Low-Risk Breast Cancer Recommendation Plan**")
        st.write("""
        For patients at **low risk** of breast cancer, focus should be on maintaining healthy habits and regular screenings to ensure continued well-being.
        """)

        st.markdown("#### 1️⃣ **Lifestyle Changes**")
        st.write("""
        - Promote a **balanced lifestyle** with regular physical activity and sufficient sleep.
        - Suggest reducing or eliminating **alcohol** and avoiding smoking.
        - Encourage **self-care practices** like stress management and limiting exposure to environmental toxins.
        """)

        st.markdown("#### 2️⃣ **Diet & Nutrition**")
        st.write("""
        - Recommend a **colorful, nutrient-dense diet** with a variety of fruits, vegetables, and whole grains.
        - Suggest limiting **processed foods and saturated fats**.
        - Encourage maintaining a **healthy weight** through portion control and mindful eating.
        """)
        
        st.markdown("#### 3️⃣ **Exercise & Physical Activity**")
        st.write("""
        - Encourage **at least 30 minutes of daily physical activity**.
        - Recommend including **aerobic exercises** and light resistance training for long-term health.
        - Suggest active hobbies like dancing, hiking, or cycling to keep motivation high.
        """)

        st.markdown("#### 4️⃣ **Monitoring & Tracking**")
        st.write("""
        - Recommend **clinical breast exams every 1–3 years**, based on age and provider guidance.
        - Educate on how to perform **breast self-exams** and recognize signs of abnormal changes.
        - Encourage keeping a **health journal** to track screenings, family history, and any new symptoms.
        """)

        st.markdown("#### 5️⃣ **Next Steps**")
        st.write("""
        - Continue with **routine screenings** as per national guidelines (typically starting at age 40).
        - Provide educational materials on **risk factors and early signs** of breast cancer.
        - Reassess risk level periodically, especially if there is a change in family history or health status.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

 
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

        show_recommendations(high_risk)

        
 
if __name__ == "__main__":
    show()