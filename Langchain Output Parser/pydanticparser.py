from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser ,JsonOutputParser ,PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3)

class Person(BaseModel):

    name: str = Field(description='Name of the person')
    age: int = Field(gt=18,description='Age of the person')
    city: str = Field(description='City of the person')


parser=PydanticOutputParser(pydantic_object=Person)

template=PromptTemplate(
    template="Generate the name ,age and city of a fictional {place} person \n {format_instruction}",
    input_variables=["place"],
    partial_variables={"format_instruction":parser.get_format_instructions()}
)


prompt = template.invoke({"place":"Indian"})

result = model.invoke(prompt)

final_result=parser.parse(result.content)

print(final_result)


#using chain
chain = template | model | parser

result = chain.invoke({"place":"Indian"})

print(result)