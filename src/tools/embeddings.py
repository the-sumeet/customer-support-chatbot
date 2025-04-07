from pathlib import Path

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
import logging

logger = logging.getLogger(__name__)

chroma_db_path = Path(__file__).parent.parent / "chroma_db"

def create_vector_store(documents, persist_directory=str(chroma_db_path)):
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=persist_directory
    )
    vector_store.persist()

    return vector_store

def load_vector_store():
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vectordb = Chroma(embedding_function=embeddings, persist_directory=str(chroma_db_path))

    logger.info("loaded vector store")

    return vectordb
