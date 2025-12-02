# embeddings.py

import yaml
from langchain_huggingface import HuggingFaceEmbeddings

def load_config():
    with open("config/config.yaml", "r") as f:
        return yaml.safe_load(f)

def get_embeddings():
    config = load_config()
    model_name = config["embedding_configuration"]["embedding_model"]
    return HuggingFaceEmbeddings(model_name=model_name)
