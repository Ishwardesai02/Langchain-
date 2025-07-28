from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel,RunnableLambda,RunnablePassthrough,RunnableBranch

load_dotenv()

model= ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3)

prompt=PromptTemplate(
    template="Write a Detailed report on {topic}",
    input_variables=["topic"]
)

prompt2=PromptTemplate(
    template="Summarize the following report:{text}",
    input_variables=["text"]
)

parser=StrOutputParser()

report_gen_chain=RunnableSequence(prompt, model, parser)


branch_chain = RunnableBranch(
    (lambda x: len(x.split())>100,RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()
)

final_chain=RunnableSequence(report_gen_chain,branch_chain)

print(final_chain.invoke({"topic":"AI"}))

final_chain.get_graph().print_ascii()