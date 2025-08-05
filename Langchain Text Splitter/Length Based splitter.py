from langchain.text_splitter import CharacterTextSplitter


text="""The LangChain framework is a powerful tool for building applications with language models. It provides a modular and flexible architecture that allows developers to create complex workflows by chaining together various components such as prompts, models, and output parsers. This enables the development of sophisticated applications that can handle tasks like text generation, question answering, and more."""

splitter=CharacterTextSplitter(
    chunk_size=10,
    chunk_overlap=0,
    separator=''
)

result=splitter.split_text(text)

print(result)