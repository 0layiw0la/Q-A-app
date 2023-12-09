from transformers import pipeline, AutoModelForQuestionAnswering, AutoTokenizer
import streamlit as st
import docx
from PyPDF2 import PdfReader

# Context based q&a
@st.cache_resource
def load_model():
    nlp = pipeline("question-answering", model="deepset/deberta-v3-large-squad2")
    return nlp

def extract_text_from_txt(file):
    text = str(file.read())
    return text

def extract_text_from_docx(file):
    doc = docx.Document(file)
    full_text = ""
    for para in doc.paragraphs:
        full_text += para.text + "\n"
    return full_text

def extract_text_from_pdf(file):
    pdf_reader = PdfReader(file)
    full_text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        full_text += page.extract_text() + "\n"
    return full_text

def answer(question,context):
    nlp = load_model()
    QA_input = {
        'question':question,
        'context':context
    }
    response = nlp(QA_input)
    if response['score'] < 0.0000001:
        return ' Unfortunately, I need more information to provide a suitable answer. Please provide me with the context and the specific question you have.  :( '
    else:
        return response['answer']
