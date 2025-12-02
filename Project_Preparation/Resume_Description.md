## Resume Bullet Points (RAG + GenAI Project)
Clinical Guidelines RAG Chatbot | Groq + Llama 3 + FAISS + Streamlit

Built an AI-powered Clinical Guidelines Assistant using RAG architecture, enabling clinicians to upload medical PDFs and get evidence-based answers grounded strictly in their documents.

Developed a complete document ingestion pipeline using pdfplumber, recursive chunking (1000 tokens, 200 overlap), HuggingFace embeddings (MiniLM), and FAISS vector indexing.

Implemented semantic retrieval with top-k vector search and built a context-aware prompt to eliminate hallucinations: “Answer ONLY from the provided medical context.”

Integrated Groq Llama-3.3 70B for ultra-low-latency inference, improving response times by 10–20x compared to standard LLM APIs.

Designed an interactive Streamlit UI for uploading PDFs, generating knowledge bases, querying medical data, and displaying contextual citations.

Achieved high retrieval accuracy by optimizing chunking strategy, embedding selection, and vector similarity thresholds.

Ensured safety by implementing fallback logic (e.g., “Not in the provided clinical documents”) to avoid hallucination in high-risk medical queries.

Demonstrated ability to build end-to-end GenAI systems, including data preprocessing, embeddings, vector stores, retrieval, LLM orchestration, and user interface development.

Improved clinical document search from minutes to seconds, enabling faster and more reliable healthcare decision-making.


##
🎯 Impact-Focused Version (For Stronger Storytelling)

Developed a high-accuracy Clinical AI Assistant that transforms unstructured medical PDFs into a searchable knowledge base using RAG, improving clinician decision efficiency.

Integrated Groq’s ultra-fast Llama-3.3 70B model to achieve sub-second medical query responses.

Engineered a robust retrieval pipeline with FAISS, improving similarity search precision and ensuring safety-critical accuracy in medical responses.

Delivered a production-ready Streamlit application enabling hospitals to deploy AI-assisted guideline search internally with full document grounding.



##
⭐ Shorter Version (for compact resumes)

Created a RAG-based Clinical Guidelines Chatbot using Groq Llama-3, FAISS, and HuggingFace embeddings to provide document-grounded, evidence-based answers from medical PDFs.

Built end-to-end pipeline including PDF parsing, recursive chunking, semantic embeddings, vector indexing, retrieval, and context-driven LLM generation.

Designed responsive Streamlit interface for real-time querying, contextual citations, and knowledge base creation.

Reduced guideline lookup time by >90% while minimizing hallucinations through context-restricted prompts and retrieval optimization.
