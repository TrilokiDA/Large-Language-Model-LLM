# Created by trilo at 02-01-2024

import gemini
from gemini import Document
import fitz  # PyMuPDF for PDF parsing

# Initialize Gemini (replace with your API key)
gemini.client(api_key="AIzaSyBOEXRoZeBsnwnKM8TmbdMHjTaEpHpeAbY")

def extract_text_from_pdf(pdf_file_path):
    with fitz.open(pdf_file_path) as doc:
        text = ""
        for page in doc:
            text += page.get_text()
    return text

def answer_question_from_pdf(pdf_file_path, question):
    pdf_text = extract_text_from_pdf(pdf_file_path)
    document = Document(pdf_text)

    try:
        # Attempt to answer the question directly from the PDF text
        answer = document.answer(question)
        return answer
    except Exception as e:
        print(f"Error answering question directly from PDF: {e}")

        # If direct answer fails, try using Gemini's search capabilities
        try:
            # Retrieve relevant paragraphs from the PDF using Gemini's search
            relevant_context = document.search(question, max_tokens=512)
            return relevant_context
        except Exception as e:
            print(f"Error retrieving relevant context from Gemini: {e}")
            return "Unable to answer the question based on the PDF content."

# Example usage
pdf_file_path = r"C:\Users\trilo\Downloads\IGNOU MSCAST\Subject\MST-015 Introduction to R Software\Block-1-Fundamentals of R Language.pdf"
question = "What are the fundamental of R"
answer = answer_question_from_pdf(pdf_file_path, question)
print(answer)

