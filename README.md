# Resume Feedback Agent 🧠📄

This project uses FastAPI + LangChain + Gemini + Streamlit to give AI-powered resume feedback.

## Features

- Upload Resume (PDF) + Job Description (TXT)
- Real-time feedback using Gemini 1.5
- Frontend with Streamlit
- Clean JSON feedback output

## How to Run

```bash
# Start FastAPI server
uvicorn app.main:app --reload

# In a separate terminal
streamlit run streamlit_ui.py
