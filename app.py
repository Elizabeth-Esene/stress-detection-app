#!/usr/bin/env python
# coding: utf-8

# In[2]:
import streamlit as st
import pandas as pd
import joblib

# ------------------ LOAD MODEL ------------------
# Make sure "fatigue_model.pkl" is in the same directory
model = joblib.load("fatigue_model.pkl")

# Map model output to activity labels
activity_map = {0: "Resting", 1: "Walking", 2: "Running"}

# ------------------ PAGE SETUP ------------------
st.set_page_config(page_title="Fatigue Monitoring System", layout="wide")
st.title("🏃 Fatigue & Stress Monitoring System")
st.markdown("### 🩺 Athlete Health Monitoring Dashboard")
st.markdown("---")

# ------------------ INPUTS (on main page) ------------------
st.subheader("📥 Enter Athlete Data")

# Use columns for clean layout
col1, col2 = st.columns(2)

with col1:
    heart_rate = st.number_input(
        "Heart Rate (bpm)", min_value=0, max_value=220, value=70, key="hr"
    )
    temperature = st.number_input(
        "Body Temperature (°C)", min_value=30.0, max_value=45.0, value=36.5, key="temp"
    )

with col2:
    oxygen = st.number_input(
        "Blood Oxygen (%)", min_value=50, max_value=100, value=98, key="oxy"
    )
    steps = st.number_input(
        "Step Count", min_value=0, max_value=50000, value=0, key="steps"
    )

# ------------------ DISPLAY VITAL SIGNS ------------------
st.markdown("---")
st.subheader("📊 Vital Signs Overview")

col3, col4 = st.columns(2)

with col3:
    st.write("❤️ Heart Rate:", heart_rate, "bpm")
    st.progress(min(float(heart_rate)/200, 1.0))

    st.write("🌡 Body Temperature:", temperature, "°C")
    st.progress(min(float(temperature)/50, 1.0))

with col4:
    st.write("🩸 Blood Oxygen:", oxygen, "%")
    st.progress(min(float(oxygen)/100, 1.0))

    st.write("👣 Step Count:", steps)

# ------------------ PREDICTION & ALERTS ------------------
st.markdown("---")
if st.button("🔍 Check Status"):
    
    # Prepare input for prediction
    sample = [[float(heart_rate), float(temperature), float(oxygen), float(steps)]]
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
    st.subheader("📊 Vital Signs Chart")
    data = pd.DataFrame({
        "Vital Sign": ["Heart Rate", "Temperature", "Oxygen", "Steps"],
        "Value": [heart_rate, temperature, oxygen, steps]
    })
    st.bar_chart(data.set_index("Vital Sign"))

# ------------------ FOOTER ------------------
st.markdown("---")
st.write(" Fatigue and stress Monitoring Sytem")
        


# In[ ]:





# In[ ]:




