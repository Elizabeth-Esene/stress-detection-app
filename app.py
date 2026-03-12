#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import joblib
import pandas as pd

# Load your trained model
model = joblib.load("fatigue_model.pkl")

# Map model outputs to activity
activity_map = {0: "Resting", 1: "Walking", 2: "Running"}

# ------------------ APP DESIGN ------------------

# Page title
st.set_page_config(page_title="Fatigue Monitoring System", layout="wide")

st.title("🏃 Fatigue & Stress Monitoring System")
st.markdown("### 🩺 Athlete Health Monitoring Dashboard")
st.markdown("---")

# Sidebar for inputs
st.sidebar.header("📥 Enter Athlete Data")

heart_rate = st.sidebar.number_input("Heart Rate (bpm)", min_value=0)
temperature = st.sidebar.number_input("Body Temperature (°C)", min_value=0.0)
oxygen = st.sidebar.number_input("Blood Oxygen (%)", min_value=0)
steps = st.sidebar.number_input("Step Count", min_value=0)

# Layout columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Vital Signs")

    st.write("Heart Rate:", heart_rate, "bpm")
    st.progress(min(int(heart_rate)/200,1.0))

    st.write("Body Temperature:", temperature, "°C")
    st.progress(min(temperature/50,1.0))

with col2:
    st.subheader("📈 Activity Data")

    st.write("Blood Oxygen:", oxygen, "%")
    st.progress(min(oxygen/100,1.0))

    st.write("Step Count:", steps)

# ------------------ PREDICTION ------------------

if st.button("🔍 Check Status"):

    # Prepare sample for prediction
    sample = [[heart_rate, temperature, oxygen, steps]]

    prediction = model.predict(sample)
    activity = activity_map[prediction[0]]

    st.subheader("🏃 Predicted Activity")
    st.success(f"Predicted Activity: {activity}")

    # Fatigue / stress alerts
    if heart_rate > 120 and steps > 3000:
        st.warning("⚠️ High fatigue risk detected! Athlete may be exhausted.")
    elif heart_rate > 100 and steps > 2000:
        st.warning("⚠️ Moderate fatigue risk. Athlete may be stressed.")
    else:
        st.info("✅ Athlete condition appears normal.")

    # Additional health alerts
    if temperature > 37.5:
        st.warning("⚠️ Elevated body temperature detected. Check for stress or illness.")

    if oxygen < 95:
        st.warning("⚠️ Low blood oxygen level detected.")

    # ------------------ CHART ------------------

    st.subheader("📊 Vital Signs Overview")

    data = pd.DataFrame({
        "Vital Sign": ["Heart Rate", "Temperature", "Oxygen", "Steps"],
        "Value": [heart_rate, temperature, oxygen, steps]
    })

    st.bar_chart(data.set_index("Vital Sign"))

# Footer
st.markdown("---")
st.write("Developed for Biomedical Engineering Fatigue Monitoring Project")
        


# In[ ]:





# In[ ]:




