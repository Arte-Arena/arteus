import subprocess

def desenhar_bandeira_brasil(nome_arquivo="bandeira_brasil.svg"):
    """
    Desenha a bandeira do Brasil usando o Inkscape via linha de comando.

    Args:
        nome_arquivo: O nome do arquivo SVG de saída.
    """

    try:
        # Dimensões baseadas na proporção 10:7
        largura = 900
        altura = int(largura * 0.7)  # Mantém a proporção 10:7

        # Cores (hexadecimais)
        verde = "#009B3D"
        amarelo = "#FCD116"
        azul = "#002776"
        branco = "#FFFFFF"

        # Comando principal do Inkscape
        comando = [
            "inkscape",
            "--batch-process",
            "--pipe",
            f"--export-filename={nome_arquivo}",
            "--export-type=svg"
        ]

        # Comandos SVG
        svg_comandos = f"""
            <svg
                xmlns="http://www.w3.org/2000/svg"
                width="{largura}"
                height="{altura}">

                <rect width="{largura}" height="{altura}" fill="{verde}" />

                <polygon points="{largura/2},{altura/10} {largura/10},{altura/2} {largura/2},{altura*9/10} {largura*9/10},{altura/2}" fill="{amarelo}" />

                <circle cx="{largura/2}" cy="{altura/2}" r="{altura/3}" fill="{azul}" />

                <path d="M {largura*0.25},{(altura/2)} L {largura*0.75},{(altura/2)} " stroke="{branco}" stroke-width="12" />

                <text x="{largura/2}" y="{altura/2 + 15}" font-size="24" font-family="Arial" text-anchor="middle" fill="{branco}" transform="rotate(-14 {largura/2} {altura/2})">ORDEM E PROGRESSO</text>

            </svg>
        """

        # Executa o comando Inkscape
        processo = subprocess.Popen(comando, stdin=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = processo.communicate(input=svg_comandos)

        if processo.returncode != 0:
            print(f"Erro ao executar o Inkscape:\n{stderr}")
        else:
            print(f"Bandeira do Brasil salva em {nome_arquivo}")

    except FileNotFoundError:
        print("Erro: Inkscape não encontrado. Certifique-se de que está instalado e no PATH do sistema.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")