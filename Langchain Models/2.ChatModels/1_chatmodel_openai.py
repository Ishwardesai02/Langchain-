from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI(model="mistralai/mistral-7b-instruct",temperature=0.1,max_completion_tokens=10)

result=model.invoke("what is capital of india?")

print(result.content)   


