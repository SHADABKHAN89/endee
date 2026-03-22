# AI Resume Analyzer using RAG + Job Matching

## 📌 Overview
This project is an AI-powered Resume Analyzer that uses semantic search and embeddings to evaluate resumes and match them with job descriptions.

---

## 🎯 Problem Statement
Manual resume screening is time-consuming and inefficient. Recruiters need an automated system to evaluate candidates quickly.

---

## 💡 Solution
This system:
- Extracts text from resumes
- Converts them into embeddings
- Performs semantic search (RAG concept)
- Computes job match score (0–100%)
- Provides hiring recommendation

---

## 🛠️ Tech Stack
- Python
- Sentence Transformers
- NumPy
- Streamlit

---

## ⚙️ System Design
1. Resume uploaded
2. Text extracted and chunked
3. Embeddings generated
4. Stored in vector store
5. User query → semantic search
6. Job description → similarity score
7. Final recommendation generated

---

## 🔍 Features
- Resume Upload (PDF)
- Semantic Search (RAG)
- Candidate Q&A
- Job Match Score (0–100%)
- Hiring Recommendation

---

## 🚀 Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/your-username/ai-resume-analyzer
cd ai-resume-analyzer