from langchain.document_loaders import PyPDFLoader, WebBaseLoader, Docx2txtLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


def load_documents(pdf_paths, docs_paths, website_urls):
    # Load PDFs (unchanged)
    pdf_loaders = [PyPDFLoader(pdf_path) for pdf_path in pdf_paths]
    pdf_docs = []
    for loader in pdf_loaders:
        pdf_docs.extend(loader.load())

    docx_loaders = [Docx2txtLoader(doc_path) for doc_path in docs_paths]
    docx_docs = []
    for loader in docx_loaders:
        docx_docs.extend(loader.load())

    # Load multiple websites - MODIFIED FOR MULTIPLE URLs
    web_docs = []
    for url in website_urls:
        web_loader = WebBaseLoader(url)
        web_docs.extend(web_loader.load())

    # Combine all documents
    all_docs = pdf_docs + web_docs + docx_docs

    # Split documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    splits = text_splitter.split_documents(all_docs)

    return splits