
import streamlit as st
from transformers import pipeline

# Load the BERT question-answering pipeline
qa_pipeline = pipeline("question-answering")

def answer_question(question, context):
    result = qa_pipeline.question_answering(question=question, context=context)
    return result['answer']

# Streamlit app layout
st.title("Question Answering Chatbot")

context = st.text_area("Enter the context:")
question = st.text_input("Ask a question based on the context:")

if st.button("Get Answer"):
    if context and question:
        answer = answer_question(question, context)
        st.write(f"Question: {question}")
        st.write(f"Answer: {answer}")
    else:
        st.write("Please provide both context and question.")
