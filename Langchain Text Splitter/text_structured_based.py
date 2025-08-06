from langchain.text_splitter import TextSplitter,RecursiveCharacterTextSplitter

text="""The LangChain framework is a powerful tool for building applications with language models. It provides a modular and flexible architecture that allows developers to create complex workflows by chaining together various components such as prompts, models, and output parsers. This enables the development of sophisticated applications that can handle tasks like text generation, question answering, and more."""

splitter=RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0
)

chunks=splitter.split_text(text)

print(len(chunks))
print(chunks)