import svgwrite


def draw_brazil_flag(filename):

    dwg = svgwrite.Drawing(filename, profile='tiny', size=(600, 400))


    # Desenhar o fundo verde

    dwg.add(dwg.rect(insert=(0, 0), size=(600, 400), fill='green'))


    # Desenhar o losango amarelo

    dwg.add(dwg.polygon(points=[(300, 0), (600, 200), (300, 400), (0, 200)], fill='yellow'))


    # Desenhar o círculo azul

    dwg.add(dwg.circle(center=(300, 200), r=80, fill='blue'))


    # Desenhar a faixa branca

    dwg.add(dwg.rect(insert=(180, 190), size=(240, 20), fill='white'))


    # Adicionar estrelas (simplificado)

    stars = [

        (270, 180), (290, 170), (310, 180), (330, 170), (350, 180),

        (290, 210), (310, 210), (330, 210), (270, 220), (350, 220)

    ]

    for star in stars:

        dwg.add(dwg.circle(center=star, r=3, fill='white'))


    # Salvar o arquivo SVG

    dwg.save()


# Chamar a função para desenhar a bandeira

draw_brazil_flag("brasil2.svg")