# llm.py

import yaml
from langchain_groq import ChatGroq

def load_config():
    with open("config/config.yaml", "r") as f:
        return yaml.safe_load(f)

def get_llm():
    cfg = load_config()["llm_configuration"]

    return ChatGroq(
        model=cfg["llm_model"],
        temperature=cfg["temperature"],
        max_tokens=cfg["max_tokens"]
    )

