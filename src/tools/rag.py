
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough

def setup_rag_chain(vector_store):
    # Define retriever
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})

    # Define prompt template
    template = """You are a customer support assistant. Answer the question based only on the following context:
    {context}

    Question: {question}

    If the question cannot be answered using the context, simply reply "I Don't know"."""
    prompt = ChatPromptTemplate.from_template(template)

    # Define LLM
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

    # Create RAG chain
    rag_chain = (
            {"context": retriever, "question": RunnablePassthrough()}
            | prompt
            | llm
    )

    return rag_chain