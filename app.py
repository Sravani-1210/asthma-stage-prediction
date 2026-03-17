import streamlit as st
import librosa
import numpy as np
import joblib
import tempfile

# Load trained model
model = joblib.load("asthma_stage_model.pkl")

# ---------------- STYLE ----------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg,#e8f1f8,#f5fbff);
}

h1 {
    font-size:42px !important;
    text-align:center;
    color:#1F4E79;
}

.precaution-text {
    font-size:20px;
    font-weight:500;
    color:#2c3e50;
}

.guidance-text {
    font-size:20px;
    font-weight:500;
    color:#1b4f72;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------

st.markdown("""
<h1>🫁 AI-Based Asthma Stage Prediction System</h1>
<p style='text-align:center;font-size:18px;'>
Early detection of asthma stages using respiratory audio analysis
</p>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------

st.sidebar.title("Project Dashboard")

st.sidebar.info("""
Model: Random Forest  
Features: MFCC Audio Features  
Dataset: Coswara Respiratory Dataset
""")

st.sidebar.subheader("Asthma Stages")

st.sidebar.write("🟠 Pre-Asthma")
st.sidebar.write("🟡 Post-Asthma")
st.sidebar.write("🟢 Stable")

# ---------------- AUDIO UPLOAD ----------------

st.subheader("Upload Respiratory Audio")

audio_file = st.file_uploader(
    "Upload cough or breathing audio file",
    type=["wav", "mp3"]
)

# ---------------- MFCC FEATURE EXTRACTION ----------------

def extract_mfcc(file_path):
    y, sr = librosa.load(file_path, sr=22050)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
    return np.mean(mfcc.T, axis=0)

# ---------------- PREDICTION ----------------

if audio_file is not None:

    st.audio(audio_file)

    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(audio_file.read())
        tmp_path = tmp.name

    # Extract features
    features = extract_mfcc(tmp_path)

    # Model prediction
    prediction = model.predict([features])[0]

    stage = str(prediction).lower()

    if "pre" in stage:
        stage = "Pre-Asthma"
    elif "post" in stage:
        stage = "Post-Asthma"
    else:
        stage = "Stable"

    # ---------------- RESULT DISPLAY ----------------

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Predicted Stage")
        st.success(stage)

    # Severity level
    if stage == "Pre-Asthma":
        severity = "High Risk"
    elif stage == "Post-Asthma":
        severity = "Medium Risk"
    else:
        severity = "Low Risk"

    with col2:
        st.subheader("Severity Level")
        st.warning(severity)

    # ---------------- PRECAUTIONS ----------------

    st.subheader("⚠ Precautions")

    if stage == "Pre-Asthma":
        st.markdown("<p class='precaution-text'>• Avoid dust and smoke</p>", unsafe_allow_html=True)
        st.markdown("<p class='precaution-text'>• Monitor breathing symptoms</p>", unsafe_allow_html=True)
        st.markdown("<p class='precaution-text'>• Consult doctor if symptoms increase</p>", unsafe_allow_html=True)

    elif stage == "Post-Asthma":
        st.markdown("<p class='precaution-text'>• Continue prescribed medication</p>", unsafe_allow_html=True)
        st.markdown("<p class='precaution-text'>• Avoid physical strain</p>", unsafe_allow_html=True)
        st.markdown("<p class='precaution-text'>• Follow doctor's advice</p>", unsafe_allow_html=True)

    else:
        st.markdown("<p class='precaution-text'>• Maintain healthy lifestyle</p>", unsafe_allow_html=True)
        st.markdown("<p class='precaution-text'>• Do breathing exercises</p>", unsafe_allow_html=True)
        st.markdown("<p class='precaution-text'>• Avoid allergens</p>", unsafe_allow_html=True)

    # ---------------- DAILY GUIDANCE ----------------

    st.subheader("💡 Daily Life Guidance")

    st.markdown("<p class='guidance-text'>• Maintain clean environment</p>", unsafe_allow_html=True)
    st.markdown("<p class='guidance-text'>• Avoid allergens like dust and smoke</p>", unsafe_allow_html=True)
    st.markdown("<p class='guidance-text'>• Practice breathing exercises</p>", unsafe_allow_html=True)
    st.markdown("<p class='guidance-text'>• Maintain healthy diet</p>", unsafe_allow_html=True)

# ---------------- FOOTER ----------------

st.markdown("---")
st.caption("AI-Based Asthma Stage Prediction System | Academic Project")