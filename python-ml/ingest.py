from drive_utils import list_folders, list_pdfs, download_pdf
from vector_store import astra_vector_store
from pdf_utils import extract_text, chunk_text
from dotenv import load_dotenv
import os

load_dotenv() 

ROOTFOLDERID = os.getenv("ROOTFOLDERID")

ROOT_FOLDER_ID = ROOTFOLDERID

def process_pdf(file_id, file_name, company, year):
    local_pdf = download_pdf(file_id, file_name)
    texts = extract_text(local_pdf)

    if not texts:
        return

    chunks = chunk_text(texts)

    metadatas = [{
        "company": company.lower(),
        "year": year,
        "student": file_name,
        "drive_file_id": file_id
    }] * len(chunks)

    astra_vector_store.add_texts(chunks, metadatas)


def run_ingestion():
    companies = list_folders(ROOT_FOLDER_ID)

    for company in companies:
        years = list_folders(company["id"])
        for year in years:
            pdfs = list_pdfs(year["id"])
            for pdf in pdfs:
                process_pdf(
                    pdf["id"],
                    pdf["name"],
                    company["name"],
                    year["name"]
                )


if __name__ == "__main__":
    run_ingestion()
