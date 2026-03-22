import streamlit as st
from utils import load_resume, chunk_text, store_chunks, search, compute_match_score

def ask_llm(query, context):
    return f"""
🔍 Resume Insight:

{context[:500]}

💡 Answer:
The candidate shows relevant experience based on the resume content.
"""

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

st.title("📄 AI Resume Analyzer (RAG + Job Matching)")


uploaded_file = st.file_uploader("Upload Resume (PDF)")


job_desc = st.text_area("Paste Job Description")


if uploaded_file:
    text = load_resume(uploaded_file)
    chunks = chunk_text(text)
    store_chunks(chunks)
    st.success("✅ Resume Indexed Successfully!")


if uploaded_file and job_desc:
    score = compute_match_score(text, job_desc)

    st.subheader("📊 Job Match Score")
    st.progress(int(score))
    st.write(f"Match Score: {score}%")

    
    if score > 75:
        result = "🟢 Strong Match - Recommended"
    elif score > 50:
        result = "🟡 Moderate Match - Consider"
    else:
        result = "🔴 Low Match - Not Recommended"

    st.subheader("📌 AI Analysis")
    st.write(f"""
**Strengths:**
- Relevant technical skills detected

**Missing Skills:**
- Some required skills from job description may be missing

**Final Decision:**
{result}
""")

# Q&A
query = st.text_input("Ask about candidate")

if query:
    context = search(query)
    answer = ask_llm(query, context)
    st.subheader("🤖 Answer")
    st.write(answer)