from langchain_huggingface import HuggingFaceEmbeddings


embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

#text="delhi is the capital of India"


documents=[
    "Delhi is the capital of India.",
    "India is a country in South Asia.",
    "The capital of France is Paris.",
    "The capital of Japan is Tokyo."
]

vector=embedding.embed_query(documents)

print(str(vector))