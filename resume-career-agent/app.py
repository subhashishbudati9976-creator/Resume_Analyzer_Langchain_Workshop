from pathlib import Path

from src.agent import agent


RESUME_PATH = "data/resumes/student_resume.txt"


def load_resume(path: str) -> str:
    file_path = Path(path)
    if file_path.suffix.lower() == ".pdf":
        from pypdf import PdfReader

        reader = PdfReader(str(file_path))
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    return file_path.read_text(encoding="utf-8")


def main() -> None:
    target_role = input("Target role [AI Engineer]: ").strip() or "AI Engineer"
    resume_path = input(f"Resume path [{RESUME_PATH}]: ").strip() or RESUME_PATH

    resume = load_resume(resume_path)

    request = f"""
Analyze this student's resume for the target role: {target_role}

RESUME
------
{resume}
------

Produce a career-readiness report with:
1. Candidate summary
2. Current technical skills
3. Strengths
4. Weaknesses
5. Relevant roles from the job knowledge base
6. Matching and missing skills
7. Recommended learning topics
8. Three-month roadmap
9. Final recommendation

Use tools when helpful. Do not invent experience.
"""

    result = agent.invoke(
        {
            "messages": [
                {"role": "user", "content": request}
            ]
        }
    )

    final_message = result["messages"][-1]
    print("\n==================================================")
    print("STUDENT AI CAREER REPORT")
    print("==================================================\n")
    print(final_message.content)


if __name__ == "__main__":
    main()
