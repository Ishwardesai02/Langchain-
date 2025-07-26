from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3)


prompt1=PromptTemplate(
    template="Generate a detailed report on {topic}",
    input_variables=["topic"]
)

prompt2=PromptTemplate(
    template="Generate a 5 line summary on the following text: {text}",
    input_variables=["text"]
)

parser=StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

print(chain.invoke({"topic":"cricket"}))

chain.get_graph().print_ascii()