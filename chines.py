import subprocess
import math

def desenhar_bandeira_china(nome_arquivo="bandeira_china.svg"):
    """
    Desenha a bandeira da China usando o Inkscape via linha de comando.

    Args:
        nome_arquivo: O nome do arquivo SVG de saída.
    """

    try:
        # Dimensões (proporção 2:3)
        largura = 900
        altura = 600

        # Cores
        vermelho = "#DE2910"  # Vermelho da China
        amarelo = "#FFFF00"

        # Comando principal do Inkscape
        comando = [
            "inkscape",
            "--batch-process",
            "--pipe",
            f"--export-filename={nome_arquivo}",
            "--export-type=svg"
        ]

        # Função para calcular os pontos de uma estrela
        def calcular_pontos_estrela(cx, cy, raio_externo, raio_interno, num_pontas=5):
            pontos = []
            for i in range(2 * num_pontas):
                angulo = math.pi * i / num_pontas - math.pi / 2
                raio = raio_externo if i % 2 == 0 else raio_interno
                x = cx + raio * math.cos(angulo)
                y = cy + raio * math.sin(angulo)
                pontos.append(f"{x},{y}")
            return " ".join(pontos)

        # Cálculo das posições e tamanhos das estrelas
        raio_estrela_grande = altura * 0.15
        cx_estrela_grande = largura * 0.15
        cy_estrela_grande = altura * 0.25

        raio_estrela_pequena = altura * 0.05
        distancia_estrelas_pequenas = altura * 0.1

        estrelas_pequenas = [
            (cx_estrela_grande + distancia_estrelas_pequenas * math.cos(math.radians(i * 30)), cy_estrela_grande + distancia_estrelas_pequenas * math.sin(math.radians(i * 30)))
            for i in [30, 60, 90]
        ]

        svg_comandos = f"""
            <svg
                xmlns="http://www.w3.org/2000/svg"
                width="{largura}"
                height="{altura}">

                <rect width="{largura}" height="{altura}" fill="{vermelho}" />

                <polygon points="{calcular_pontos_estrela(cx_estrela_grande, cy_estrela_grande, raio_estrela_grande, raio_estrela_grande/2.63)}" fill="{amarelo}" />
        """

        for cx, cy in estrelas_pequenas:
            svg_comandos += f"""
                <polygon points="{calcular_pontos_estrela(cx, cy, raio_estrela_pequena, raio_estrela_pequena/2.63)}" fill="{amarelo}" />
            """

        svg_comandos += "</svg>"

        # Executa o comando Inkscape
        processo = subprocess.Popen(comando, stdin=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = processo.communicate(input=svg_comandos)

        if processo.returncode != 0:
            print(f"Erro ao executar o Inkscape:\n{stderr}")
        else:
            print(f"Bandeira da China salva em {nome_arquivo}")

    except FileNotFoundError:
        print("Erro: Inkscape não encontrado. Certifique-se de que está instalado e no PATH do sistema.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Exemplo de uso
desenhar_bandeira_china()
