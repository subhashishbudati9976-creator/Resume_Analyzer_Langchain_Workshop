from langchain_core.prompts import ChatPromptTemplate

resume_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert technical recruiter and career advisor.
Analyze student resumes for technical roles.
Do not invent qualifications, experience, projects or skills.
Base observations on the supplied resume.
""",
        ),
        (
            "human",
            """
Analyze the following resume for the target role: {target_role}

Resume:
----------------
{resume}
----------------

Give:
1. Candidate summary
2. Current technical skills
3. Relevant projects
4. Relevant experience
5. Strengths
6. Weaknesses
7. Likely skill gaps for the target role
8. Concrete resume improvement suggestions
""",
        ),
    ]
)
