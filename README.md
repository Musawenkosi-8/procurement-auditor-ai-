
Here is the complete copy-paste README for your GitHub repository with all 4 agents:

```markdown
# 🛡️ Procurement Auditor AI

> An intelligent multi-agent AI system that automates procurement contract auditing, invoice processing, compliance verification, risk assessment, and audit report generation.

[![Status](https://img.shields.io/badge/status-live-success)](https://procurement-auditor-ai-v1-e.crewai.com)
[![CrewAI](https://img.shields.io/badge/CrewAI-1.14.4-blue)](https://crewai.com)
[![Python](https://img.shields.io/badge/Python-3.10+-yellow)](https://python.org)

---

## 🚀 Live API

**Endpoint**: `https://procurement-auditor-ai-v1-e.crewai.com`

**Status**: ✅ Online

The API is live and accepting requests. *Contact me for Bearer Token access.*

---

## 📋 Problem This Solves

Procurement departments face daily challenges with:

- **Invoices** that need validation against contracts
- **Compliance violations** hidden in fine print
- **Risk exposure** from unfavorable terms
- **Manual auditing** that takes hours per document

**This AI system automates the entire 4-step audit process.**

---

## 🤖 The 4 Agents

| # | Agent | Role | Responsibility |
|---|-------|------|----------------|
| 1 | **Invoice Processing Agent** | Document Extractor | Extracts key fields from invoices (amount, date, vendor, PO number) |
| 2 | **Compliance Auditor** | Regulatory Checker | Verifies invoice matches contract terms and compliance standards |
| 3 | **Risk Assessment Analyst** | Risk Evaluator | Identifies pricing discrepancies, late fees, and contractual violations |
| 4 | **Audit Report Generator** | Report Writer | Creates human-readable audit summary with findings and recommendations |

---

## 🔄 How They Work Together

```

Invoice Upload
↓
┌─────────────────────────────────────┐
│ Agent 1: Invoice Processing Agent   │
│ Extracts: amount, date, vendor, PO# │
└─────────────────────────────────────┘
↓
┌─────────────────────────────────────┐
│ Agent 2: Compliance Auditor         │
│ Checks: terms, pricing, delivery    │
└─────────────────────────────────────┘
↓
┌─────────────────────────────────────┐
│ Agent 3: Risk Assessment Analyst    │
│ Flags: discrepancies, violations    │
└─────────────────────────────────────┘
↓
┌─────────────────────────────────────┐
│ Agent 4: Audit Report Generator     │
│ Outputs: Clear audit report         │
└─────────────────────────────────────┘
↓
Final Audit Report

```

---

## 📊 Sample Output

```json
{
  "invoice_id": "INV-2025-0421",
  "vendor": "SupplyCo Ltd",
  "invoice_amount": "$12,500.00",
  "contract_amount": "$10,000.00",
  
  "agent_1_invoice_processing": {
    "extracted_fields": {
      "invoice_date": "2025-03-15",
      "due_date": "2025-04-14",
      "po_number": "PO-9876",
      "line_items": 3
    }
  },
  
  "agent_2_compliance_audit": {
    "status": "FAILED",
    "violations": [
      "Amount exceeds contract by $2,500",
      "Unit price $125 vs agreed $100"
    ]
  },
  
  "agent_3_risk_assessment": {
    "risk_score": 85,
    "risk_level": "HIGH",
    "findings": [
      "Overcharging detected",
      "No approved change order"
    ]
  },
  
  "agent_4_audit_report": {
    "summary": "Invoice does not match contract. Recommend rejecting and requesting corrected invoice.",
    "action_required": "Reject Invoice"
  }
}
```

---

🛠️ Tech Stack

Component Technology
AI Framework CrewAI 1.14.4
LLM GPT-4 (OpenAI)
Language Python 3.10+
Deployment CrewAI AMP Cloud
Tools PDF parsing, web search, file I/O

---

📦 Run Locally

Prerequisites

· Python 3.10 - 3.14
· OpenAI API key

Setup

```bash
# Clone the repository
git clone https://github.com/Musawenkosi-8/procurement-auditor-ai.git
cd procurement-auditor-ai

# Install uv (fast package manager)
pip install uv

# Install dependencies
uv pip install -r requirements.txt

# Add your OpenAI API key
echo "OPENAI_API_KEY=your_key_here" > .env

# Run the crew
crewai run
```


---

🔗 Connect With Me

Musawenkosi Nyawo

· AI Engineer| Agent Developer
· GitHub
· LinkedIn

---

📚 Resources

· Multi-Agent Systems

---

📄 License

MIT License

---

Built with CrewAI - 4 agents collaborating to automate procurement auditing.

```

