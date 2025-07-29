from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader('D:\Campus X Langchain\Langchain Document Loaders\jung21_interspeech.pdf')

docs=loader.load()

print(len(docs[0].page_content))

print(docs[1].metadata)