import os
from PyPDF2 import PdfMerger

def get_next_output_filename(folder, base_name="merged", extension=".pdf"):
    number = 0
    while True:
        output_path = os.path.join(folder, f"{base_name}_{number}{extension}")
        if not os.path.exists(output_path):
            return output_path
        number += 1

def merge_numbered_pdfs(folder):
    merger = PdfMerger()

    # Get all files ending in .pdf and starting with a number
    pdf_files = [f for f in os.listdir(folder) if f.lower().endswith('.pdf') and f[:-4].isdigit()]

    # Sort files like ['1.pdf', '2.pdf', ..., '10.pdf']
    pdf_files = sorted(pdf_files, key=lambda x: int(x[:-4]))

    if not pdf_files:
        print("No valid numbered PDF files found.")
        return

    for pdf in pdf_files:
        full_path = os.path.join(folder, pdf)
        try:
            print(f"Trying to merge: {full_path}")
            merger.append(full_path)
            print(f"Merged: {pdf}")
        except Exception as e:
            print(f"Skipped {pdf}: {e}")

    output_file = get_next_output_filename(folder)
    merger.write(output_file)
    merger.close()k
    print(f"\n✅ Merged PDF saved as: {output_file}")

# 🔧 Example usage
merge_numbered_pdfs("pfd")  # Replace 'clutter' with your folder name
