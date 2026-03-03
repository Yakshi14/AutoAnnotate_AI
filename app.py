import streamlit as st
import pandas as pd
import json


from services.file_parser import parse_file
from services.annotator import annotate_batch

st.set_page_config(page_title="AutoAnnotate AI", layout="wide")

st.title("🧠 AutoAnnotate AI")
st.markdown("AI-powered Human-in-the-Loop Data Annotation Platform")

# Sidebar
st.sidebar.header("⚙ Settings")

confidence_threshold = st.sidebar.slider(
    "Confidence Threshold",
    0.0, 1.0, 0.6
)

labels_input = st.sidebar.text_input(
    "Candidate Labels (comma separated)",
    "Technology, Finance, Sports, Politics, Healthcare"
)

labels = [label.strip() for label in labels_input.split(",")]

uploaded_file = st.file_uploader(
    "Upload JSON, TXT, or PDF",
    type=["json", "txt", "pdf"]
)

if uploaded_file:

    st.info("Parsing file...")
    data = parse_file(uploaded_file)

    if not data:
        st.error("Unsupported or empty file.")
        st.stop()

    st.info("Running AI annotation...")
    annotated_data = annotate_batch(data, labels)

    if not annotated_data:
      st.error("No annotations returned. Check API token or rate limits.")
      st.stop()

    df = pd.DataFrame(annotated_data)

    df["needs_review"] = df["confidence"] < confidence_threshold

    st.success("Annotation complete!")

    st.subheader("📊 Annotated Data")

    show_low_confidence = st.checkbox("Show only low-confidence samples")

    if show_low_confidence:
        display_df = df[df["needs_review"] == True]
    else:
        display_df = df

    edited_df = st.data_editor(
        display_df,
        use_container_width=True
    )

    st.subheader("📥 Download Annotated File")

    json_output = edited_df.to_json(
        orient="records",
        indent=2
    )

    st.download_button(
        label="Download Annotated JSON",
        data=json_output,
        file_name="annotated_output.json",
        mime="application/json"
    )
