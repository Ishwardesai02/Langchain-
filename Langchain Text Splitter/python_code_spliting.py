from langchain.text_splitter import TextSplitter,RecursiveCharacterTextSplitter
from langchain_text_splitters import Language

text="""
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b        
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
def power(a, b):    
    return a ** b
def factorial(n):       

    if n < 0:
        raise ValueError("Cannot compute factorial of a negative number")       
    if n == 0 or n == 1:
        return 1
    result = 1  
    for i in range(2, n + 1):
        result *= i
    return result
    return a % b
def modulus(a, b): 
    if b == 0:
        raise ValueError("Cannot compute modulus by zero")
    return a % b 
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a   

    
"""

splitter=RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=100,
    chunk_overlap=0

)

chunks=splitter.split_text(text)

print(len(chunks))

print(chunks[1])
