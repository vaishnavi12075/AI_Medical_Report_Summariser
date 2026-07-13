from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client=Groq(api_key=os.getenv("GROQ_API_KEY"))
def generate_summary(text):
    prompt=f"""
You are an experienced medical assistant.
Return the response in the following Markdown format exactly.
Do not change the headings.
Do not merge sections.
## Patient Condition
Explain the patient's current conditon in simple language.
## Medical Diagnosis

Mention the diagnosis or possible conditions mentioned in the report.

## Medicines Mentioned

STRICT RULES FOR THIS SECTION:
- Output ONLY the medicine names.
- Each medicine MUST be written on a separate line.
- Each line MUST start exactly with "MEDICINE:".
- Do NOT mention uses, purposes, or descriptions.
- Do NOT combine multiple medicines on one line.
- Do NOT write any sentence after a medicine name.
- If no medicines are present, write exactly:
None

VALID FORMAT EXAMPLE:

MEDICINE: Paracetamol 650 mg
MEDICINE: Oral Iron
MEDICINE: Vitamin D3

INVALID FORMAT EXAMPLES:

MEDICINE: Paracetamol 650 mg - used for fever 

MEDICINE: Paracetamol 650 mg MEDICINE: Oral Iron

Vitamin D3 is not prescribed.

## Important Observations

Mention important test results, abnormal values, and key findings.

## Lifestyle Recommendations
Provide simple lifestyle suggestions based on the report.

## Medical Terms Explained

Instructions:

-Explain everything in simple language so that a normal person can understand.
-Whenever you find a medical term,immediately explain it in everyday language.
-Write it in this format:
Hypertension->high blood pressure
Hyperglycemia->High blood sugar
Dyspnea->shortness of breath
Myocardial Infarction->Heart Attack

IMPORTANT
-Avoid complicated medical jargon
-Allow each term is present in separate single line

-Assume the reader has no medical background
-If no difficult medical terms are present,mention "No complex medical terms found."

Medical Report:

{text}
"""
    response=client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
            "role":"user",
            "content":prompt
        }
        ]
    )
    summary=response.choices[0].message.content
    return summary