# prompt_ui.py
from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import streamlit as st
import os

# Load .env
load_dotenv()

# ✅ Define LLM from Hugging Face
llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.1",  # Or any other chat-compatible HF model
    task="text-generation",
    max_new_tokens=512,
    temperature=0.7
)

# ✅ Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a research assistant that explains research papers."),
    ("human", "Explain '{paper_input}' in a {style_input} style. Be {length_input}.")
])

# ✅ Streamlit UI
st.title("🧠 Research Paper Explainer")

paper_input = st.selectbox("Choose a paper:", [
    "Attention Is All You Need",
    "BERT: Pre-training of Deep Bidirectional Transformers",
    "GPT-3: Language Models are Few-Shot Learners",
    "Diffusion Models Beat GANs on Image Synthesis"
])

style_input = st.selectbox("Select style:", [
    "Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"
])

length_input = st.selectbox("Select length:", [
    "Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"
])

# ✅ Chain: prompt | llm
chain = prompt | llm

if st.button("Summarize"):
    response = chain.invoke({
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input
    })
    st.write(response)
