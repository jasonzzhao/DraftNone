import streamlit as st
from io import BytesIO
from pydub import AudioSegment
from fpdf import FPDF
import base64

# Show title and description
st.title("🚔 Police Incident Report Drafter")
st.write(
    "Upload an audio file (MP3 or WAV) containing details of a police incident, and this app will generate a PDF report!"
)

# Let the user upload an audio file
uploaded_file = st.file_uploader("Upload an audio file", type=("mp3", "wav"))

if uploaded_file:
    # Convert the uploaded audio file to text (placeholder logic)
    st.audio(uploaded_file, format="audio/mp3")  # Play the uploaded audio
    audio = AudioSegment.from_file(uploaded_file)

    # Placeholder for transcription (replace with an actual transcription tool like OpenAI Whisper or similar)
    transcription = "This is a placeholder transcription of the audio file."

    # Create a PDF report
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Police Incident Report", ln=True, align="C")
    pdf.ln(10)
    pdf.multi_cell(0, 10, txt=transcription)

    # Save PDF to a BytesIO object
    pdf_output = BytesIO()
    pdf.output(pdf_output)
    pdf_output.seek(0)

    # Display the PDF in the app
    base64_pdf = base64.b64encode(pdf_output.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="500" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

    # Provide a download link for the PDF
    st.download_button(
        label="Download Incident Report PDF",
        data=pdf_output,
        file_name="incident_report.pdf",
        mime="application/pdf",
    )
