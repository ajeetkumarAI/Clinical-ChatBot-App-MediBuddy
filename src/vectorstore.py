# vectorstore.py

import yaml
from langchain_community.vectorstores import FAISS

def load_config():
    with open("config/config.yaml", "r") as f:
        return yaml.safe_load(f)

def get_vectorstore(embeddings, docs):
    config = load_config()
    index_path = config["vectorstore_configuration"]["faiss_index_path"]

    vectorstore = FAISS.from_documents(
        documents=docs,
        embedding=embeddings
    )

    vectorstore.save_local(index_path)
    return vectorstore

def load_vectorstore(embeddings):
    config = load_config()
    index_path = config["vectorstore_configuration"]["faiss_index_path"]

    return FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)

def get_retriever(vector_store):
    config = load_config()
    top_k = config["vectorstore_configuration"]["top_k"]
    return vector_store.as_retriever(search_kwargs={"k": top_k})