import streamlit as st
import random

st.set_page_config(page_title="Asthma Stage Prediction", layout="centered")

st.title("🫁 Asthma Stage Prediction System")

st.write("Upload cough or breathing audio to predict asthma stage")

audio_file = st.file_uploader("Upload Audio File", type=["wav", "mp3"])

if audio_file is not None:
    st.audio(audio_file)

    # Demo prediction
    stage = random.choice(["Pre-Asthma", "Post-Asthma", "Stable"])

    st.subheader("Prediction Result")
    st.success("Predicted Stage: " + stage)

    # Severity
    if stage == "Pre-Asthma":
        severity = "High Risk"
    elif stage == "Post-Asthma":
        severity = "Medium Risk"
    else:
        severity = "Low Risk"

    st.warning("Severity Level: " + severity)

    # Precautions
    st.subheader("Precautions")

    if stage == "Pre-Asthma":
        st.write("• Avoid dust and smoke")
        st.write("• Monitor breathing symptoms")
        st.write("• Consult doctor")

    elif stage == "Post-Asthma":
        st.write("• Continue medication")
        st.write("• Avoid heavy activity")
        st.write("• Follow doctor advice")

    else:
        st.write("• Maintain healthy lifestyle")
        st.write("• Do breathing exercises")
        st.write("• Avoid allergens")

    # Daily guidance
    st.subheader("Daily Life Guidance")
    st.write("• Maintain clean environment")
    st.write("• Avoid allergens")
    st.write("• Practice breathing exercises")
    st.write("• Healthy diet")
