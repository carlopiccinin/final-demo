import fitz  # Modulo di PyMuPDF
from reportlab.pdfgen import canvas

def sovrascrivi_testo_al_pdf(input_file, output_file, testo_da_sovrascrivere, posizione_x, posizione_y):
    # Apri il file PDF originale
    pdf_doc = fitz.open(input_file)

    # Seleziona la prima pagina
    pagina = pdf_doc[0]

    # Disegna il nuovo testo sulla pagina
    pdf_canvas = canvas.Canvas(output_file, pagesize=(pagina.rect.width, pagina.rect.height))
    pdf_canvas.drawString(posizione_x, pagina.rect.height - posizione_y, testo_da_sovrascrivere)
    pdf_canvas.save()

    # Sovrascrivi il contenuto della pagina con il nuovo testo
    pagina.showPDFpage(pdf_doc, 0)

    # Salva il PDF modificato su un nuovo file
    pdf_doc.save(output_file)

# Esempio di utilizzo:
input_pdf = "2000503 - QUESTIONARIO PF clean (002).pdf"
output_pdf = "percorso_del_tuo_file_modificato.pdf"
testo_da_sovrascrivere = "La tua nuova scritta qui"
posizione_x = 50
posizione_y = 45

sovrascrivi_testo_al_pdf(input_pdf, output_pdf, testo_da_sovrascrivere, posizione_x, posizione_y)
