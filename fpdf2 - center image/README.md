# Center Image
O  script `center_image_fpdf.py` contém uma função que centraliza uma imagem em um PDF. 
Parâmetros:
  - **pdf_obj**: Objeto pdf FPDF
  - **img_path**: Caminho da imagem
  - **container_width**: Largura do container, se não for informado, será usada a largura do PDF
  - **container_height**: Altura do container
  - **container_x**: Posição x do container
  - **container_y**: Posição y do container
  - **image_margin**: Margem entre a imagem e o container, considere que em qualquer um dos eixos haverá margem * 2 (esquerda e direita ou cima e baixo)
  - **pdf_margin**: Margem do arquivo PDF

Exemplo de uso:
```python
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
```

> O container não necessariamente precisar existir dentro do PDF, ele é usado para ser a área de referência onde a imagem será centralizada.