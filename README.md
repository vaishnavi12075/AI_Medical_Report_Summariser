# 🩺 AI Medical Report Analyzer
An AI-powered web application that converts complex medical reports into simple, easy-to-understand summaries using Large Language Models (LLMs). The application also highlights abnormal findings, allows users to view extracted text, and generates a downloadable PDF summary.
---
# 📌 Project Overview

Medical reports often contain complex terminology that is difficult for patients to understand.

The **AI Medical Report Summariser** helps bridge this gap by allowing users to upload their medical reports in **PDF** or **TXT** format. The application extracts the report content, sends it to an AI model, and generates a patient-friendly explanation.

In addition, the application:

- 📄 Uploads PDF and TXT medical reports
- 🤖 Generates AI-powered summaries
- ⚠️ Detects abnormal findings
- 📥 Downloads summaries as PDF
- 📋 Displays extracted report text
- 📢 Includes a medical disclaimer

---

# ✨ Features
-📄 Upload Medical Report
-🤖 AI generated medical summary
-🩺 Simplified explanation
-⚠️ Highlights abnormal values such as:
  - High
  - Low
  - Elevated
  - Increased
  - Decreased
  - Positive
  - Negative
  - Abnormal
  - Deficient
-🤖 Download summary as pdf
-🗒️ View extracted report text
-🔒 Error handling for invalid files and AI connection issues
-📢 Medical disclaimer

---
# 🛠️ Tech Stack

## Frontend
-Streamlit

## Backend
-Python

## AI Model
- Groq API
- Llama 3.3 70B Versatile

## Libraries

- streamlit
- pypdf
- fpdf
- python-dotenv
- groq
- re

---

# 📂 Project Structure

```text
AI-Medical-Report-Summariser/
│
├── app.py
├── llm.py
├── .env
├── requirements.txt
├── README.md
├── summary.pdf
└── screenshots/
```

---
# 🚀 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/vaishnavi12075/AI-Medical-Report-Summariser.git
cd AI-Medical-Report-Summariser
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Create a `.env` File

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## 5. Run the Application

```bash
streamlit run app.py
```

---
# 🔄 Workflow

```text
          Upload PDF/TXT
                 │
                 ▼
        Extract Text
                 │
                 ▼
      Send to Groq LLM API
                 │
                 ▼
      Generate AI Summary
          │             │
          ▼             ▼
 Display Summary   Detect Abnormal Findings
          │
          ▼
    Generate PDF Summary
          │
          ▼
 Download PDF
```

---


# 🔮 Future Improvements

- 🔍 OCR support for scanned PDFs
- 🌐 Multi-language summaries
- 🎤 Voice-based report explanation
- 💬 Chat with your medical report
- 💊 Separate medicines and prescriptions
- 📈 Disease risk prediction
- ☁️ Cloud deployment
- 👤 User authentication
- 📄 DOCX export
- 📧 Email report summary

---

# 👩‍💻 Author

**Vaishnavi Kota**

B.Tech CSE (AI & ML)

- GitHub: https://github.com/vaishnavi12075
- LinkedIn: https://www.linkedin.com/in/vaishnavi-kota-5a1936390/

---



