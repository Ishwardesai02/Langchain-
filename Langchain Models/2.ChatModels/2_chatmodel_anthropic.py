from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI(model="anthropic/claude-3-opus",temperature=0.1,max_completion_tokens=100)

result=model.invoke("what is capital of india?")

print(result.content)   


