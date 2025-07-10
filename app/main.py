from fastapi import FastAPI, UploadFile, File, HTTPException
from app.utils import extract_text_from_pdf
from app.resume_chain import get_resume_feedback

app = FastAPI()

@app.post("/analyze/")
async def analyze_resume(resume: UploadFile = File(...), jd: UploadFile = File(...)):
    resume_text = extract_text_from_pdf(resume.file)

    # 🔍 Fallback: check if resume text is empty
    if not resume_text.strip():
        raise HTTPException(status_code=400, detail="Failed to extract text from resume. Please upload a text-based PDF.")

    jd_text = (await jd.read()).decode("utf-8")

    result = get_resume_feedback(resume_text, jd_text)
    return {"feedback": result}

