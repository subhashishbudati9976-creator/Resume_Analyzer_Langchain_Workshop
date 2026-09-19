# Complete Execution Steps — Project Guide

## A. Before the Project start

### 1. Install Python

Use Python 3.10 or newer. Verify:

```bash
python --version
```

On Windows, if `python` does not work:

```cmd
py --version
```

### 2. Extract the ZIP

Open a terminal in the extracted project folder:

```bash
cd resume-career-agent
```

### 3. Create a virtual environment

Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Windows CMD:

```cmd
py -m venv .venv
.venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install packages

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## B. Create a free Gemini API key for the Project

Google AI Studio: https://aistudio.google.com/

Official Gemini API key documentation: https://ai.google.dev/gemini-api/docs/api-key

Official Gemini getting-started documentation: https://ai.google.dev/gemini-api/docs/get-started

Official Gemini pricing/free-tier information: https://ai.google.dev/gemini-api/docs/pricing

### Participant procedure

1. Open Google AI Studio.
2. Sign in with a Google account.
3. Find the API key / Get API key option.
4. Create an API key.
5. Copy the key.
6. Return to the project folder.
7. Copy `.env.example` to `.env`.
8. Open `.env`.
9. Replace the placeholder with the real key.

Example:

```text
GEMINI_API_KEY=AIza...
MODEL_NAME=gemini-3.5-flash-lite
```

Do not share the key. Do not commit `.env` to Git.

### Free usage warning

Google currently offers a Gemini API free tier with limited access/quotas. Free-tier availability, supported models and rate limits can change. The Project should use short prompts and a limited number of requests. For a group test, then you should test the expected number of requests and have a fallback plan.

## C. API test

Run:

```bash
python step1_gemini_test.py
```

If successful, you should see a generated explanation.

If this fails, stop and resolve the API-key/model issue before continuing.

## D. LangChain resume analysis

Run:

```bash
python step2_langchain_resume.py
```

Enter:

```text
AI Engineer
```

The program sends the sample resume through LangChain to Gemini.

## E. Build the RAG knowledge base

Run:

```bash
python step3_build_vectorstore.py
```

This loads the text job descriptions, splits them, creates embeddings and saves a FAISS vector store under:

```text
vectorstore/jobs
```

## F. Test retrieval

Run:

```bash
python step4_test_retriever.py
```

Try:

```text
AI Engineer Python Machine Learning RAG LangChain
```

You should see relevant job-description chunks.

## G. Run the final agent

```bash
python app.py
```

Example input:

```text
Target role [AI Engineer]: AI Engineer
Resume path [data/resumes/student_resume.txt]:
```

The final agent should analyze the resume, retrieve relevant jobs and use the career tools to produce a report.

## H. PDF resume test

Copy a text-based PDF resume into `data/resumes/`, for example:

```text
data/resumes/student1.pdf
```

Run:

```bash
python app.py
```

Then enter:

```text
Target role [AI Engineer]: AI Engineer
Resume path [data/resumes/student_resume.txt]: data/resumes/student1.pdf
```

## I. Project Execution sequence

### Stage 1 — Direct Gemini



```text
Python → API → Gemini → Response
```

Run `step1_gemini_test.py`.

### Stage 2 — LangChain

Understand:

```text
Python → LangChain → Gemini → Response
```

Run `step2_langchain_resume.py`.

### Stage 3 — RAG

Understand why a model needs external job information.

Run `step3_build_vectorstore.py` and `step4_test_retriever.py`.

### Stage 4 — Tools

Understand skill-gap, match-score, learning and roadmap tools.

### Stage 5 — Agent

Run `app.py` and explain the agent's tool-selection loop.

## J. Common errors

### 1. Key missing

Check `.env` and ensure the file is in the project root.

### 2. Key/quota error

Check Google AI Studio, the selected model, free-tier quota and project restrictions.

### 3. Model error

Change `MODEL_NAME` to a currently available Gemini API model.

### 4. PowerShell activation blocked

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

### 5. Vector store missing

Run:

```bash
python step3_build_vectorstore.py
```

### 6. PDF text extraction is empty

The sample implementation expects a text-based PDF. Scanned resumes may require OCR or a multimodal extraction approach.

## K. Final successful run


```text
Resume PDF
   ↓
Extract text
   ↓
LangChain + Gemini
   ↓
Resume analysis
   ↓
RAG job retrieval
   ↓
Agent
   ↓
Skill-gap tool
   ↓
Learning tool
   ↓
Roadmap tool
   ↓
Final career report
```
