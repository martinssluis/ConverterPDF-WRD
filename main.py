import tkinter as tk
from tkinter import filedialog, messagebox
from fpdf import FPDF
from docx import Document
from pdf2docx import Converter
import os

# Função para converter PDF para Word
def pdf_to_word():
    pdf_file = filedialog.askopenfilename(title="Selecione um arquivo PDF", filetypes=[("PDF files", "*.pdf")])
    if pdf_file:
        word_file = pdf_file.replace('.pdf', '.docx')
        cv = Converter(pdf_file)
        cv.convert(word_file, start=0, end=None)
        cv.close()
        messagebox.showinfo("Sucesso", f"PDF convertido para Word com sucesso: {word_file}")

# Função para converter Word para PDF
def word_to_pdf():
    word_file = filedialog.askopenfilename(title="Selecione um arquivo Word", filetypes=[("Word files", "*.docx")])
    if word_file:
        pdf_file = word_file.replace('.docx', '.pdf')
        doc = Document(word_file)
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        
        for para in doc.paragraphs:
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, para.text)
        
        pdf.output(pdf_file)
        messagebox.showinfo("Sucesso", f"Word convertido para PDF com sucesso: {pdf_file}")

# Configuração da interface gráfica
app = tk.Tk()
app.title("Conversor PDF/Word")
app.geometry("300x150")

# Botões para conversão
btn_pdf_to_word = tk.Button(app, text="Converter PDF para Word", command=pdf_to_word)
btn_pdf_to_word.pack(pady=10)

btn_word_to_pdf = tk.Button(app, text="Converter Word para PDF", command=word_to_pdf)
btn_word_to_pdf.pack(pady=10)

# Executa a aplicação
app.mainloop()
