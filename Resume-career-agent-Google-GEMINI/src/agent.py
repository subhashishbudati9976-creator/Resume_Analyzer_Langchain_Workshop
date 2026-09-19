from pathlib import Path

from langchain.agents import create_agent
from langchain.tools import tool

from src.llm import llm
from src.rag import get_retriever
from src.tools import (
    calculate_match_percentage,
    calculate_skill_gap,
    create_learning_roadmap,
    recommend_learning,
)


@tool
def search_relevant_jobs(query: str) -> str:
    """Search the job knowledge base for relevant job descriptions."""
    retriever = get_retriever()
    docs = retriever.invoke(query)
    if not docs:
        return "No relevant jobs found."

    blocks = []
    for doc in docs:
        source = Path(doc.metadata.get("source", "unknown")).name
        blocks.append(f"SOURCE: {source}\n{doc.page_content}")
    return "\n\n".join(blocks)


TOOLS = [
    search_relevant_jobs,
    calculate_skill_gap,
    calculate_match_percentage,
    recommend_learning,
    create_learning_roadmap,
]


agent = create_agent(
    model=llm,
    tools=TOOLS,
    system_prompt=(
        "You are an AI career advisor. "
        "Analyze the supplied student resume carefully. "
        "Use the job search tool when current job-role requirements are needed. "
        "Use deterministic tools for calculations and skill-gap analysis. "
        "Do not invent qualifications or experience. "
        "Clearly separate resume facts from recommendations. "
        "Return a concise but useful career report."
    ),
)
