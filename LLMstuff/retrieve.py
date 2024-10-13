from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

retriever = db.as_retriever()

llm = Ollama(model="llama3.2")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an assistant for question-answering tasks. Use the following pieces of retrieved context to augment your own knowledge."),
    ("human", "Context: {context}"),
    ("human", "Question: {input}"),
    ("human", "Please provide a detailed answer, combining information from the context (if relevant) and your own knowledge.")
])

question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)


def ask_question(chain, question):
    result = chain.invoke({"input": question})
    print("Question:", question)
    print("\n ** WITH CONTEXT **\n")
    print("Answer:", result['answer'])
    print("\nSources:")
    for doc in result['context']:
        print(doc.metadata)
    print("\n")

    default_result = llm.invoke(question)
    print("\n** WITHOUT CONTEXT **\n")
    print(default_result)

question = "How does the differential transformer differ from a traditional transformer?"
ask_question(rag_chain, question)