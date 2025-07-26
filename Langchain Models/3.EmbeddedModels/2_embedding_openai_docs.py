from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-large",
                 dimensions=32)

documents=[
    "Delhi is the capital of India.",
    "India is a country in South Asia.",
    "The capital of France is Paris.",
    "The capital of Japan is Tokyo."
]

result=embeddings.embed_query("delhi is the capital of india")

print(str(result))