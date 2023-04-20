from fpdf import svg
from PIL import Image

def center_image(pdf_obj, img_path, container_width=0, container_height=0, container_x=0, container_y=0, image_margin=0, pdf_margin=0):
    '''
        Centraliza a imagem no container, por padrão o tamanho da imagem será aumentado/diminuído para caber no container,
        se a imagem tiver a mesma proporção do container a imagem ficará do mesmo tamanho do container menos a margem.

        param pdf_obj: Objeto pdf FPDF
        param img_path: Caminho da imagem
        param container_width: Largura do container, se não for informado, será usada a largura do PDF
        param container_height: Altura do container, se não for informado, será usada a largura do PDF
        param container_x: Posição x do container
        param container_y: Posição y do container
        param image_margin: Margem entre a imagem e o container, considere que em qualquer um dos eixos haverá margem * 2 (esquerda e direita ou cima e baixo)
        param pdf_margin: Margem do PDF, considere que em qualquer um dos eixos haverá margem * 2 (esquerda e direita ou cima e baixo)

        example: center_image(pdf_obj, 'img.png', 100, 100, 0, 0, 10)

        raise ValueError: Se a margem for menor que 0

        return: {
            'width': largura da imagem,
            'height': altura da imagem,
            'x': posição x da imagem,
            'y': posição y da imagem
        }
    '''
    container_width = pdf_obj.w - (pdf_margin * 2) if container_width == 0 else container_width       # Se o container for 0, ele pega o tamanho da página menos a margem
    container_height = pdf_obj.h - pdf_margin if container_height == 0 else container_height    # Se o container for 0, ele pega o tamanho da página menos a margem

    if image_margin < 0:
        raise ValueError('A margem não pode ser menor que 0')

    if img_path.endswith('.svg'):
        image = svg.SVGObject.from_file(img_path)
    
    else:
        image = Image.open(img_path)

    image_ratio = image.width / image.height
    container_ratio = container_width / container_height

    if image_ratio == container_ratio:      # Container com a mesma proporção da imagem
        pdf_obj.image(name=img_path, w=container_width - image_margin, h=container_height - image_margin, x=container_x + image_margin, y=container_y + image_margin)
        return {
            'width': container_width - image_margin,
            'height': container_height - image_margin,
            'x': container_x + image_margin,
            'y': container_y + image_margin
        }
    
    elif image_ratio > container_ratio:           # Imagem na horizontal e container na vertical
        new_width = container_width - (image_margin * 2)
        new_height = new_width / image_ratio
        new_y = container_y + ((container_height - new_height) / 2)
        new_x = container_x + image_margin

        pdf_obj.image(name=img_path, w=new_width, h=new_height, x=new_x, y=new_y)
        return {
            'width': new_width,
            'height': new_height,
            'x': new_x,
            'y': new_y
        }
    
    else:                                   # Imagem na vertical e container na horizontal
        new_height = container_height - (image_margin * 2)
        new_width = new_height * image_ratio
        new_x = container_x + ((container_width - new_width) / 2)
        new_y = container_y + image_margin

        pdf_obj.image(name=img_path, w=new_width, h=new_height, x=new_x, y=new_y)
        return {
            'width': new_width,
            'height': new_height,
            'x': new_x,
            'y': new_y
        }
