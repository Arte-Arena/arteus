import subprocess
import math

def desenhar_bandeira_turquia(nome_arquivo="bandeira_turquia.svg"):
    """
    Desenha a bandeira da Turquia usando o Inkscape via linha de comando.

    Args:
        nome_arquivo: O nome do arquivo SVG de saída.
    """

    try:
        # Dimensões (proporção 2:3)
        largura = 900
        altura = 600

        # Cores
        vermelho = "#E30A17"  # Vermelho da Turquia
        branco = "#FFFFFF"

        # Comando principal do Inkscape
        comando = [
            "inkscape",
            "--batch-process",
            "--pipe",
            f"--export-filename={nome_arquivo}",
            "--export-type=svg"
        ]

        # Cálculo das dimensões e posições
        raio_circulo_externo = altura * 0.4
        raio_circulo_interno = altura * 0.25
        raio_estrela = altura * 0.15

        cx = largura * 0.3
        cy = altura / 2

        # Função para calcular os pontos de uma estrela (reutilizada)
        def calcular_pontos_estrela(cx, cy, raio_externo, raio_interno, num_pontas=5):
            pontos = []
            for i in range(2 * num_pontas):
                angulo = math.pi * i / num_pontas - math.pi / 2
                raio = raio_externo if i % 2 == 0 else raio_interno
                x = cx + raio * math.cos(angulo)
                y = cy + raio * math.sin(angulo)
                pontos.append(f"{x},{y}")
            return " ".join(pontos)

        svg_comandos = f"""
            <svg
                xmlns="http://www.w3.org/2000/svg"
                width="{largura}"
                height="{altura}">

                <rect width="{largura}" height="{altura}" fill="{vermelho}" />

                <circle cx="{cx}" cy="{cy}" r="{raio_circulo_externo}" fill="{branco}" />
                <circle cx="{cx + raio_circulo_externo*0.15}" cy="{cy}" r="{raio_circulo_interno}" fill="{vermelho}" />
                <polygon points="{calcular_pontos_estrela(cx + raio_circulo_externo*0.4, cy, raio_estrela, raio_estrela/2.63)}" fill="{branco}" />

            </svg>
        """

        # Executa o comando Inkscape
        processo = subprocess.Popen(comando, stdin=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = processo.communicate(input=svg_comandos)

        if processo.returncode != 0:
            print(f"Erro ao executar o Inkscape:\n{stderr}")
        else:
            print(f"Bandeira da Turquia salva em {nome_arquivo}")

    except FileNotFoundError:
        print("Erro: Inkscape não encontrado. Certifique-se de que está instalado e no PATH do sistema.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Exemplo de uso
desenhar_bandeira_turquia()

