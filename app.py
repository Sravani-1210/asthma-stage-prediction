import streamlit as st
import random
import time

# Page Config
st.set_page_config(page_title="Asthma Detection", layout="centered")

# Background + Style
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #e0f7fa, #ffffff);
}
.big-title {
    text-align: center;
    font-size: 48px;
    font-weight: bold;
    color: #2c3e50;
}
.section {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 12px;
    margin-top: 20px;
    box-shadow: 0px 6px 15px rgba(0,0,0,0.15);
}
</style>
""", unsafe_allow_html=True)

# Logo + Title
st.markdown("<h1 style='text-align:center;'>🫁 Asthma Stage Prediction System</h1>", unsafe_allow_html=True)

st.write("Upload cough or breathing audio to predict asthma stage")

# Upload Section Title
st.markdown("### 📤 Upload Audio")

# Upload File
audio_file = st.file_uploader("Upload Audio File", type=["wav", "mp3"])

if audio_file is not None:

    st.audio(audio_file)

    # Loading Spinner
    with st.spinner("Analyzing audio..."):
        time.sleep(2)

    # Demo Prediction
    stage = random.choice(["Pre-Asthma", "Post-Asthma", "Stable"])
    confidence = random.randint(80, 98)

    # Severity Logic
    if stage == "Pre-Asthma":
        severity = "High Risk"
        color = "#f8d7da"
    elif stage == "Post-Asthma":
        severity = "Medium Risk"
        color = "#fff3cd"
    else:
        severity = "Low Risk"
        color = "#d4edda"

    # Result Card
    st.markdown(f"""
    <div class="section" style="background-color:{color}">
        <h3>Prediction Result</h3>
        <b>Stage:</b> {stage}<br>
        <b>Severity:</b> {severity}<br>
        <b>Confidence:</b> {confidence}%
    </div>
    """, unsafe_allow_html=True)

    # Spacing
    st.write("")
    st.write("")

    # Columns
    col1, col2 = st.columns(2)

    # Precautions
    with col1:
        st.markdown('<div class="section">', unsafe_allow_html=True)
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

        st.markdown('</div>', unsafe_allow_html=True)

    # Guidance
    with col2:
        st.markdown('<div class="section">', unsafe_allow_html=True)
        st.subheader("Daily Life Guidance")

        st.write("• Maintain clean environment")
        st.write("• Avoid allergens")
        st.write("• Practice breathing exercises")
        st.write("• Healthy diet")

        st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<center>Developed by Sravani | Asthma Detection Project</center>", unsafe_allow_html=True)
