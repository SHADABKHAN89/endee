from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer
import numpy as np


model = SentenceTransformer('all-MiniLM-L6-v2')


vector_store = []
text_store = []



def load_resume(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text



def chunk_text(text, chunk_size=300):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]



def store_chunks(chunks):
    global vector_store, text_store

    
    vector_store.clear()
    text_store.clear()

    for chunk in chunks:
        embedding = model.encode(chunk)
        vector_store.append(embedding)
        text_store.append(chunk)



def search(query):
    if not vector_store:
        return "No resume data available."

    q_embedding = model.encode(query)

    similarities = []
    for vec in vector_store:
        sim = np.dot(q_embedding, vec) / (
            np.linalg.norm(q_embedding) * np.linalg.norm(vec)
        )
        similarities.append(sim)

    
    top_indices = np.argsort(similarities)[-3:][::-1]

    context = " ".join([text_store[i] for i in top_indices])
    return context



def compute_match_score(resume_text, job_desc):
    if not resume_text or not job_desc:
        return 0.0

    res_emb = model.encode(resume_text)
    job_emb = model.encode(job_desc)

    similarity = np.dot(res_emb, job_emb) / (
        np.linalg.norm(res_emb) * np.linalg.norm(job_emb)
    )

    score = round(similarity * 100, 2)
    return score