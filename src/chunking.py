# chunking.py

import yaml
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

def load_config():
    with open("config/config.yaml", "r") as f:
        return yaml.safe_load(f)

def split_into_chunks(text):
    config = load_config()
    chunk_cfg = config["chunking_configuration"]

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_cfg["chunk_size"],
        chunk_overlap=chunk_cfg["chunk_overlap"],
        separators=chunk_cfg["separators"]
    )

    chunks = splitter.split_text(text)
    return [Document(page_content=c) for c in chunks]
