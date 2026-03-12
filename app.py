#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import joblib

# Load your trained model
model = joblib.load("fatigue_model.pkl")

# Map model outputs to activity
activity_map = {0: "Resting", 1: "Walking", 2: "Running"}

# App title
st.title("Fatigue & Stress Monitoring System")
st.write("Enter the  readings below:")

# User inputs
heart_rate = st.number_input("Heart Rate (bpm)")
temperature = st.number_input("Body Temperature (°C)")
oxygen = st.number_input("Blood Oxygen (%)")
steps = st.number_input("Step Count")

# Predict button
if st.button("Check Status"):

    # Prepare sample for prediction
    sample = [[heart_rate, temperature, oxygen, steps]]
    prediction = model.predict(sample)
    activity = activity_map[prediction[0]]

    # Display activity
    st.success(f"Predicted Activity: {activity}")

    # Add fatigue/stress alerts
    if heart_rate > 120 and steps > 3000:
        st.warning("⚠️ High fatigue risk detected! Athlete may be exhausted.")
    elif heart_rate > 100 and steps > 2000:
        st.warning("⚠️ Moderate fatigue risk. Athlete may be stressed.")
    else:
        st.info("Athlete condition appears normal.")

    # Optional: check temperature and oxygen
    if temperature > 37.5:
        st.warning("⚠️ Elevated body temperature detected. Check for stress or illness.")
    if oxygen < 95:
        st.warning("⚠️ Low blood oxygen.")
        


# In[ ]:





# In[ ]:




