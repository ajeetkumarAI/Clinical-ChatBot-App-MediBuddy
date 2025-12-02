# rag_pipeline.py

from src.loaders import load_pdf
from src.chunking import split_into_chunks
from src.embeddings import get_embeddings
from src.vectorstore import get_vectorstore, load_vectorstore, get_retriever
from src.llm import get_llm

def build_rag_pipeline(pdf_path):
    # 1. Load PDF
    text = load_pdf(pdf_path)

    # 2. Convert to chunks
    docs = split_into_chunks(text)

    # 3. Create Embeddings
    embeddings = get_embeddings()

    # 4. Create VectorStore
    try:
        vector_db = load_vectorstore(embeddings)
    except:
        vector_db = get_vectorstore(embeddings, docs)

    # 5. Retriever
    retriever = get_retriever(vector_db)

    # 6. LLM
    llm = get_llm()

    return retriever, llm
