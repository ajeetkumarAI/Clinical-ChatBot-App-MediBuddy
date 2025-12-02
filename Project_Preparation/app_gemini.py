import streamlit as st
import os
import pdfplumber
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate

# ---------------------------------------------------
# Load env
# ---------------------------------------------------
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# ---------------------------------------------------
# Streamlit UI
# ---------------------------------------------------
st.set_page_config(page_title="🧠 Clinical Guidelines Chatbot", layout="wide")
st.title("🏥 AI Clinical Document Assistant")
st.write("Upload clinical PDFs and ask evidence-based questions.")

# ---------------------------------------------------
# Gemini Flash LLM
# ---------------------------------------------------
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0.1
)

# ---------------------------------------------------
# Gemini Embeddings
# ---------------------------------------------------
embedding_model = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=GOOGLE_API_KEY
)

# ---------------------------------------------------
# Extract text from PDFs
# ---------------------------------------------------
def extract_pdf_text(file):
    """Extract text from PDF using pdfplumber"""
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

# ---------------------------------------------------
# Build Vector Store
# ---------------------------------------------------
def create_vectorstore(documents):
    """Create FAISS vector store from documents"""
    vectorstore = FAISS.from_documents(
        documents=documents,
        embedding=embedding_model
    )
    return vectorstore

# ---------------------------------------------------
# Initialize session state
# ---------------------------------------------------
if 'vectorstore' not in st.session_state:
    st.session_state.vectorstore = None

# ---------------------------------------------------
# Streamlit Upload
# ---------------------------------------------------
uploaded_files = st.file_uploader(
    "Upload Medical PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:
    all_texts = []

    for file in uploaded_files:
        with st.spinner(f"Reading {file.name}..."):
            pdf_text = extract_pdf_text(file)
            all_texts.append(pdf_text)

    if st.button("🚀 Create Medical Knowledge Base"):
        with st.spinner("Processing documents and creating embeddings..."):
            # Combine all texts
            combined_text = "\n\n".join(all_texts)
            
            # Split text into chunks
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200,
                length_function=len,
                separators=["\n\n", "\n", ". ", " ", ""]
            )
            
            chunks = text_splitter.split_text(combined_text)
            
            # Create documents
            documents = [Document(page_content=chunk) for chunk in chunks]
            
            # Create vector store
            st.session_state.vectorstore = create_vectorstore(documents)

        st.success(f"✅ Knowledge Base created successfully with {len(documents)} document chunks!")

# ---------------------------------------------------
# Question Answering Interface
# ---------------------------------------------------
if st.session_state.vectorstore is not None:
    st.subheader("Ask a Clinical Question")

    query = st.text_input("Enter your question:")

    if st.button("🔍 Get Answer") and query:
        with st.spinner("Analyzing medical knowledge..."):
            # Create retriever
            retriever = st.session_state.vectorstore.as_retriever(
                search_type="similarity",
                search_kwargs={"k": 5}
            )
            
            # Retrieve relevant documents
            relevant_docs = retriever.invoke(query)

            # Build context from retrieved documents
            context = "\n\n".join([doc.page_content for doc in relevant_docs])

            # Create prompt
            prompt_template = """You are a medical AI assistant. Answer ONLY using the provided context.
Be precise, evidence-based, and cite specific information from the context when possible.

Context:
{context}

Question:
{question}

If the answer is not found in the provided clinical documents, reply: "Not in provided clinical documents."

Answer:"""

            prompt = PromptTemplate(
                template=prompt_template,
                input_variables=["context", "question"]
            )

            # Format prompt with context and query
            formatted_prompt = prompt.format(context=context, question=query)

            # Get response from LLM
            response = llm.invoke(formatted_prompt)

        st.markdown("### 📌 Evidence-based Answer")
        st.write(response.content)

        with st.expander("📚 Source Context"):
            for i, doc in enumerate(relevant_docs, 1):
                st.markdown(f"**Source {i}:**")
                st.write(doc.page_content)
                st.markdown("---")
else:
    st.info("👆 Upload PDFs and create a knowledge base to get started!")





