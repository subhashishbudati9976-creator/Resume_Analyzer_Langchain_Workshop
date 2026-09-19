from pathlib import Path

from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from config import MODEL_NAME

# Use a currently supported Gemini embedding model available to the account.
# For the workshop, keep this configurable if Google changes the model name.
EMBEDDING_MODEL = "models/gemini-embedding-001"
VECTORSTORE_PATH = "vectorstore/jobs"


def load_job_documents():
    documents = []
    for file in sorted(Path("data/jobs").glob("*.txt")):
        documents.extend(TextLoader(str(file), encoding="utf-8").load())
    return documents


def build_vectorstore():
    documents = load_job_documents()
    splitter = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=100)
    chunks = splitter.split_documents(documents)

    embeddings = GoogleGenerativeAIEmbeddings(model=EMBEDDING_MODEL)
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(VECTORSTORE_PATH)
    return vectorstore


def load_vectorstore():
    embeddings = GoogleGenerativeAIEmbeddings(model=EMBEDDING_MODEL)
    return FAISS.load_local(
        VECTORSTORE_PATH,
        embeddings,
        allow_dangerous_deserialization=True,
    )


def get_retriever():
    vectorstore = load_vectorstore()
    return vectorstore.as_retriever(search_kwargs={"k": 3})
