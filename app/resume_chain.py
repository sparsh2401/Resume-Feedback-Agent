from langchain_google_genai import ChatGoogleGenerativeAI # type: ignore
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3)

# Prompt template for feedback
template = """
You are a career advisor. Compare the resume with the job description.
Give a score out of 10 and detailed feedback under:
- Missing Skills
- Relevant Experience
- Resume Formatting
- Overall Suggestions

Job Description:
{jd}

Resume:
{resume}

Output in markdown format.
"""

prompt = PromptTemplate.from_template(template)

def get_resume_feedback(resume_text, jd_text):
    chain = prompt | llm
    result = chain.invoke({"resume": resume_text, "jd": jd_text})

    # Only return the content (not metadata)
    return result.content if hasattr(result, "content") else result
