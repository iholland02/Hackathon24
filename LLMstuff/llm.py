from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.llms import Ollama
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

loader = PyMuPDFLoader("plant_facts.pdf")
documents = loader.load()

# Split the documents into chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=500)
texts = text_splitter.split_documents(documents)

# Create embeddings
embeddings = HuggingFaceEmbeddings()

# Create a vector store
db = Chroma.from_documents(texts, embeddings)

retriever = db.as_retriever(search_kwargs={"k": 1})

llm = OllamaLLM(model="llama3.2")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an assistant for question-answering tasks. Use the following pieces of retrieved context."),
    ("human", "Context: {context}"),
    ("human", "Question: {input}"),
    ("human", "Please provide a detailed answer, using information from the context (only if its about plants).")
])

question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)


def ask_question(chain, question):
    result = chain.invoke({"input": question})
    print("\n\nQuestion:", question)
    print("\nAnswer:", result['answer'])


question = input("Ask your question: ")
ask_question(rag_chain, question)