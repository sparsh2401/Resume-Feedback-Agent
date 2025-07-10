import streamlit as st
import requests
import PyPDF2

# Helper function to check if a PDF looks like a resume
def is_resume_pdf(file) -> bool:
    try:
        reader = PyPDF2.PdfReader(file)
        full_text = "\n".join(page.extract_text() or "" for page in reader.pages).lower()

        # Define some common resume keywords
        keywords = ["education", "experience", "skills", "projects", "contact", "profile", "summary"]

        return any(keyword in full_text for keyword in keywords)
    except Exception as e:
        print(f"PDF read error: {e}")
        return False


st.set_page_config(page_title="Resume Feedback Agent", layout="centered")

st.title("📄 Resume Feedback Agent")
st.caption("Upload your resume and job description to get instant AI-powered feedback.")

# Upload fields
resume_file = st.file_uploader("Upload your Resume (PDF only)", type=["pdf"])
jd_file = st.file_uploader("Upload Job Description (Text file)", type=["txt"])

if resume_file and jd_file:
    # Validate resume content
    if not is_resume_pdf(resume_file):
        st.error("❌ The uploaded PDF doesn't appear to be a resume. Please upload a valid resume.")
    else:
        resume_file.seek(0)  # Reset file pointer after reading

        if st.button("📤 Submit for Analysis"):
            with st.spinner("Analyzing your resume..."):
                response = requests.post(
                    "http://127.0.0.1:8000/analyze/",
                    files={
                        "resume": (resume_file.name, resume_file, "application/pdf"),
                        "jd": (jd_file.name, jd_file, "text/plain")
                    }
                )
                if response.status_code == 200:
                    st.markdown("### ✅ Feedback Report")
                    st.markdown(response.json()["feedback"])
                else:
                    st.error("❌ Failed to get feedback. Check the server and try again.")
