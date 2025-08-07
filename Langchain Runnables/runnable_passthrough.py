from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnablePassthrough, RunnableParallel

load_dotenv()

model= ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3)

prompt=PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=["topic"]
)

prompt2=PromptTemplate(
    template="Explain me the following joke:{text}",
    input_variables=["text"]
)

parser=StrOutputParser()

joke_gen_chain=RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel({
    "joke": RunnablePassthrough(),
    "explanation": RunnableSequence(prompt2, model, parser)
})
  #Combine

final_chain= RunnableSequence(joke_gen_chain, parallel_chain)

print(final_chain.invoke({"topic": "pakistan"}))