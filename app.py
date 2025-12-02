import streamlit as st
from src.rag_pipeline import build_rag_pipeline
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Streamlit UI
st.set_page_config(page_title="GenAI Clinical Guidelines Assistant", layout="wide")
st.title("GenAI-powered Clinical Guidelines Assistant")

# PDF Upload
file = st.file_uploader("Upload a PDF", type=["pdf"])

if file:
    # Save uploaded PDF
    with open("uploaded.pdf", "wb") as f:
        f.write(file.getbuffer())

    # Build RAG pipeline (retriever + LLM)
    retriever, llm = build_rag_pipeline("uploaded.pdf")
    st.success("PDF processed successfully!")

    # Question input
    query = st.text_input("Ask a question")

    if st.button("Ask") and query:
        with st.spinner("Analyzing medical knowledge..."):
            # Retrieve relevant documents
            relevant_docs = retriever.invoke(query)  # <-- updated method

            # Build context from retrieved documents
            context = "\n\n".join([doc.page_content for doc in relevant_docs])

            # Prepare prompt
            prompt = f"""
You are a medical AI assistant. Answer ONLY using the provided context.
Be precise, evidence-based, and cite specific information from the context when possible.

Context:
{context}

Question:
{query}

If the answer is not found in the provided clinical documents, reply: "Not in provided clinical documents."

ANSWER:
            """

            # Get response from LLM
            response = llm.invoke(prompt)

        # Display answer
        st.markdown("### 📌 Evidence-based Answer")
        st.write(response.content)

        # Optionally show sources
        with st.expander("📚 Source Context"):
            for i, doc in enumerate(relevant_docs, 1):
                st.markdown(f"**Source {i}:**")
                st.write(doc.page_content)
                st.markdown("---")
else:
    st.info("👆 Upload PDFs to create a knowledge base and start asking questions!")
