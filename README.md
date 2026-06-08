# 🛡️ Procurement Auditor AI

An intelligent multi-agent system that automates procurement document auditing, contract risk assessment, and compliance verification.

## 🚀 Live Demo
**Access the live API**: https://procurement-auditor-ai-v1-ee5a99a7-bd10-467-b8697239.crewai.com

## 🤖 Agents in This Crew

| Agent | Role | Tools Used |
|-------|------|-------------|
| **Contract Analyzer** | Reviews procurement documents for risks | PDF parser, text extraction |
| **Compliance Checker** | Verifies against regulatory standards | Web search, document comparison |
| **Report Generator** | Creates audit summaries | File writer, markdown formatter |

## 📋 What It Does
- Upload procurement contracts/documents
- AI identifies risky clauses and missing compliance items
- Generates human-readable audit report
- Flags potential fraud indicators

## 🛠️ Tech Stack
- **Framework**: CrewAI 1.14.4
- **LLM**: GPT-4 (OpenAI)
- **Language**: Python 3.10+
- **Deployment**: CrewAI AMP Cloud

## 📦 Run Locally

```bash
# Clone the repo
git clone https://github.com/Muisavenkosi-8/procurement-auditor-ai.git
cd procurement-auditor-ai

# Install dependencies
pip install uv
uv pip install -r requirements.txt

# Add your OpenAI API key to .env file
echo "OPENAI_API_KEY=your_key_here" > .env

# Run the crew
crewai run
