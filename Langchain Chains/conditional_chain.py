from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel,RunnableBranch,RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal


load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3)

parser=StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(description="Give the sentiment of the following feedback.")

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1=PromptTemplate(
    template="classify the following feedback into positive, negative:\n {feedback} \n {format_instruction}",
    input_variables=["feedback"],
    partial_variables={"format_instruction": parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2

prompt2=PromptTemplate(
     template="Write an appropriate response to this positive feedback.",
     input_variables=["feedback"]
)

prompt3=PromptTemplate(
     template="Write an appropriate response to this negative feedback.",
     input_variables=["feedback"]
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment=='positive',prompt2 | model | parser),
    (lambda x:x.sentiment=='negative',prompt3 | model | parser),
    RunnableLambda(lambda x:"could not classify feedback")
)


#result=classifier_chain.invoke({"feedback": "The product is great, but the delivery was slow."}).sentiment
#print(result)

chain=classifier_chain | branch_chain

result=chain.invoke({'feedback':'This is terrible phone'})
print(result)