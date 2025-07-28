from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel,RunnableLambda,RunnablePassthrough

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

def word_count(text):
    return len(text.split())

joke_gen_chain=RunnableSequence(prompt,model,StrOutputParser())

parallel_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    'word_count':RunnableLambda(word_count)
})

final_chain=RunnableSequence(joke_gen_chain,parallel_chain)

print(final_chain.invoke({"topic":"AI"}))


final_chain.get_graph().print_ascii()