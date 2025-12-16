import os
from PyPDF2 import PdfMerger

INPUT_DIR = "data/input"
OUTPUT_DIR = "data/output"
OUTPUT_FILE = "merged.pdf"

def merge_pdfs(input_dir, output_dir, output_file):
    merger = PdfMerger()

    pdf_files = sorted([
        f for f in os.listdir(input_dir)
        if f.lower().endswith(".pdf")
    ])

    if not pdf_files:
        print("No PDF files found in input folder.")
        return

    for pdf in pdf_files:
        pdf_path = os.path.join(input_dir, pdf)
        merger.append(pdf_path)
        print(f"Added: {pdf}")

    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, output_file)

    with open(output_path, "wb") as f:
        merger.write(f)

    merger.close()
    print(f"\nMerged PDF saved to: {output_path}")

if __name__ == "__main__":
    merge_pdfs(INPUT_DIR, OUTPUT_DIR, OUTPUT_FILE)
