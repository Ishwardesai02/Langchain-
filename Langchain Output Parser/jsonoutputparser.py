from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser ,JsonOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3)




parser=JsonOutputParser()

template=PromptTemplate(
    template="Give me the name , age , and city of fictional person \n {format_instruction}",
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)


prompt=template.format()

result=model.invoke(prompt)

final_result=parser.parse(result.content)

print(final_result)