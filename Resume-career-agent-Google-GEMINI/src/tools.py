from langchain.tools import tool

COURSES = {
    "deep learning": [
        "Neural Networks",
        "CNN",
        "RNN",
        "Transformers",
    ],
    "rag": [
        "Document Loading",
        "Chunking",
        "Embeddings",
        "Vector Databases",
        "Retrievers",
        "RAG Evaluation",
    ],
    "langchain": [
        "Prompt Templates",
        "Structured Output",
        "Tools",
        "Retrieval",
        "Agents",
    ],
    "docker": [
        "Images",
        "Containers",
        "Docker Compose",
    ],
    "cloud": [
        "Cloud Fundamentals",
        "Containers",
        "Deployment",
    ],
}


@tool
def calculate_skill_gap(candidate_skills: list[str], required_skills: list[str]) -> list[str]:
    """Return required job skills that are missing from the candidate."""
    candidate = {s.lower().strip() for s in candidate_skills}
    required = {s.lower().strip() for s in required_skills}
    return sorted(required - candidate)


@tool
def calculate_match_percentage(matching_skills: int, required_skills: int) -> float:
    """Calculate the percentage match between matching and required skills."""
    if required_skills <= 0:
        return 0.0
    return round((matching_skills / required_skills) * 100, 2)


@tool
def recommend_learning(skill: str) -> list[str]:
    """Recommend learning topics for one missing skill."""
    return COURSES.get(skill.lower().strip(), [f"Build a focused learning plan for {skill}."])


@tool
def create_learning_roadmap(missing_skills: list[str]) -> dict[str, list[str]]:
    """Create a simple three-month learning roadmap from missing skills."""
    roadmap = {"Month 1": [], "Month 2": [], "Month 3": []}

    priority = [
        "python",
        "machine learning",
        "deep learning",
        "rag",
        "langchain",
        "agentic ai",
        "docker",
        "cloud",
    ]

    normalized = [s.lower().strip() for s in missing_skills]
    ordered = [s for s in priority if s in normalized]
    ordered.extend(s for s in normalized if s not in ordered)

    for i, skill in enumerate(ordered):
        roadmap[f"Month {(i % 3) + 1}"].append(skill)

    return roadmap
