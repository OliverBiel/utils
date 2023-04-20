from fpdf import FPDF
from center_image_fpdf import center_image


pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)

pdf.cell(w=0, h=10, txt='Centralizando imagens', align='C')
pdf.ln(10)
pdf.cell(w=0, h=100, border=1)
data = center_image(pdf_obj=pdf, img_path='img.jpg', container_height=100, container_x=0, container_y=pdf.get_y(), image_margin=5)
print(data)      # Dados da posição e tamanho da imagem
pdf.output('example.pdf')