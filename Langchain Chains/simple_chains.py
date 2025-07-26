from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3)


prompt=PromptTemplate(
    template="Genrate 5 intresting facts about {topic}",
    input_variables=["topic"]
)

parser=StrOutputParser()

chain = prompt | model | parser

print(chain.invoke({"topic":"black hole"}))

chain.get_graph().print_ascii()