from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3)

model2= ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3)

prompt1=PromptTemplate(
    template="Generate short and simple notes from the following text\n{text}",
    input_variables=["text"]
)

prompt2=PromptTemplate(
    template="Generate a 5  questions on the following text: {text}",
    input_variables=["text"]  
)

prompt3=PromptTemplate(
    template="Merge the following notes and questions into a single document: {notes} and {questions}",
    input_variables=["notes", "questions"]
)

parser=StrOutputParser()

parallel_chain = RunnableParallel(
    {
        "notes": prompt1 | model | parser,
        "questions": prompt2 | model2 | parser
    }
)
#merge_chain = prompt3 | model | parser

chain= parallel_chain | prompt3 | model | parser

text="linear regression is a statistical method used to model the relationship between a dependent variable and one or more independent variables. It assumes that the relationship is linear, meaning that a change in the independent variable(s) will result in a proportional change in the dependent variable. Linear regression is commonly used for prediction and forecasting, as well as for understanding the strength and nature of relationships between variables. It is widely applied in various fields such as economics, biology, and social sciences. It can be used to analyze trends, make predictions, and inform decision-making processes. In Machine Learning, linear regression is often used as a baseline model for regression tasks due to its simplicity and interpretability. It is Superior to more complex models in scenarios where the relationship between variables is indeed linear or nearly linear."

print(chain.invoke({"text":text }))

chain.get_graph().print_ascii()