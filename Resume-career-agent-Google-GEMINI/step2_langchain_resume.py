from pathlib import Path

from src.llm import llm
from src.prompts import resume_prompt


RESUME_PATH = "data/resumes/student_resume.txt"


def main() -> None:
    target_role = input("Target role [AI Engineer]: ").strip() or "AI Engineer"
    resume = Path(RESUME_PATH).read_text(encoding="utf-8")

    messages = resume_prompt.invoke(
        {
            "target_role": target_role,
            "resume": resume,
        }
    )

    response = llm.invoke(messages)
    print("\n=== LANGCHAIN RESUME ANALYSIS ===\n")
    print(response.content)


if __name__ == "__main__":
    main()
