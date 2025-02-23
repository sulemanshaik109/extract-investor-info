# Extract Investor Insights from PDF

## Overview
This Python script extracts and summarizes key investor insights from a given PDF document. It utilizes `pdfplumber` for text extraction and filters relevant sentences based on user-provided or default keywords.

## Features
- Extracts raw text from a PDF file
- Cleans and preprocesses extracted text
- Summarizes key insights based on keywords
- Supports user-defined keywords for targeted extraction

## Requirements
Ensure you have Python installed (>=3.6) and install dependencies using:
```bash
pip install pdfplumber
```

## Usage
### Run the script
```bash
python extract_investor_info.py
```

### Input
- Enter the full path to the PDF file when prompted.
- Provide comma-separated keywords for filtering insights (optional).

### Output
- Extracted and cleaned text
- Key investor insights based on specified keywords

## Example
```
Enter the full path of the PDF file: C:\Users\User\Documents\Report.pdf
Enter keywords for extraction (comma-separated): revenue, profit, growth

Investor Insights:
- The company's revenue increased by 15% in Q4.
- The growth strategy focuses on international expansion.
```

## Notes
- If no keywords are provided, default keywords such as `growth`, `profit`, `loss`, `revenue`, `investment`, `strategy`, `market`, `forecast`, and `earnings` will be used.

## License
This project is licensed under the MIT License.

## Author
[Suleman Shaik]

