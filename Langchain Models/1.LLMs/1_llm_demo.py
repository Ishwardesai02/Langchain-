from langchain import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm=OpenAI(model="mistralai/mistral-7b-instruct")

result=llm.invoke("what is capital of india?")

print(result)