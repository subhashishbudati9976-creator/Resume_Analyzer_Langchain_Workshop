from pydantic import BaseModel, Field


class ResumeAnalysis(BaseModel):
    candidate_name: str = Field(description="Candidate full name")
    education: str = Field(description="Education summary")
    technical_skills: list[str] = Field(default_factory=list)
    projects: list[str] = Field(default_factory=list)
    experience: list[str] = Field(default_factory=list)
    certifications: list[str] = Field(default_factory=list)
    strengths: list[str] = Field(default_factory=list)
    weaknesses: list[str] = Field(default_factory=list)
    missing_skills: list[str] = Field(default_factory=list)
