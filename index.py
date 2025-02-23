import pdfplumber
import re
import argparse

def extract_text_from_pdf(pdf_path):
    """Extracts raw text from a given PDF file using pdfplumber."""
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    except Exception as e:
        print(f"Error reading PDF file: {e}")
    return text if text else "No text extracted."

def clean_text(text):
    """Cleans and preprocesses the extracted text."""
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def simple_summarization(text, keywords=None):
    """Extracts key sentences related to finance and investment insights."""
    if not text or text == "No text extracted.":
        return "No valid text to summarize."
    
    sentences = re.split(r'(?<=\w\.)\s', text)
    keywords = keywords or ["future growth prospects", "changes in buisness", "earnings", "strategy"]
    
    summary = "\n".join([sentence for sentence in sentences if any(keyword in sentence.lower() for keyword in keywords)])
    
    return summary if summary else "No key investor insights found."

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract and summarize investor insights from a PDF.")
    parser.add_argument("pdf_path", type=str, help="Path to the PDF file")
    parser.add_argument("--keywords", type=str, nargs="+", help="Optional custom keywords for extraction")
    
    args = parser.parse_args()

    raw_text = extract_text_from_pdf(args.pdf_path)
    if raw_text != "No text extracted.":
        cleaned_text = clean_text(raw_text)
        insights = simple_summarization(cleaned_text, args.keywords)
        print("Investor Insights:\n", insights)
    else:
        print("No valid content extracted from PDF.")
