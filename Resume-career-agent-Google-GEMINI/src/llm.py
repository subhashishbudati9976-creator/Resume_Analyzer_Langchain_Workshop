from langchain_google_genai import ChatGoogleGenerativeAI

from config import MODEL_NAME


llm = ChatGoogleGenerativeAI(
    model=MODEL_NAME,
    temperature=0,
)
