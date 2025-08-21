import os
from scripts.pdf_extractor import extract_text_from_pdf
from scripts.data_cleaner import clean_payslip_data
from scripts.export_to_excel import export_to_excel

def run_automation():
    pdf_dir = "data/pdfs/"
    all_data = []

    for file in os.listdir(pdf_dir):
        if file.endswith(".pdf"):
            pdf_path = os.path.join(pdf_dir, file)
            raw_text = extract_text_from_pdf(pdf_path)
            cleaned_data = clean_payslip_data(raw_text)
            all_data.append(cleaned_data)

    export_to_excel(all_data)
