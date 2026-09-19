from src.rag import get_retriever


if __name__ == "__main__":
    retriever = get_retriever()
    query = input("Job search query [AI Engineer Python RAG]: ").strip() or "AI Engineer Python RAG"
    results = retriever.invoke(query)

    for index, doc in enumerate(results, start=1):
        print(f"\n--- RESULT {index} ---")
        print(doc.page_content)
