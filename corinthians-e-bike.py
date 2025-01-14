import subprocess
import os

def desenhar_bandeira_corinthians_com_bicicleta(nome_arquivo="bandeira_corinthians_bicicleta.svg", arquivo_bicicleta="bicicleta.svg"):
    """Desenha a bandeira do Corinthians com uma bicicleta usando o Inkscape."""

    try:
        # Dimensões
        largura = 900
        altura = 600

        # Cores (aproximadas)
        branco = "#FFFFFF"
        preto = "#000000"

        # Verifica se o arquivo da bicicleta existe
        if not os.path.exists(arquivo_bicicleta):
            raise FileNotFoundError(f"Arquivo da bicicleta '{arquivo_bicicleta}' não encontrado.")

        # Comando principal do Inkscape
        comando = [
            "inkscape",
            "--batch-process",
            "--pipe",
            f"--export-filename={nome_arquivo}",
            "--export-type=svg"
        ]

        svg_comandos = f"""
            <svg
                xmlns="http://www.w3.org/2000/svg"
                width="{largura}"
                height="{altura}">

                <rect width="{largura}" height="{altura}" fill="{branco}" />

                <g transform="translate({largura/2 - 100} {altura/2 - 100}) scale(0.4)">
                    <image href="{arquivo_bicicleta}" width="500" height="500"/>
                </g>
                <g transform="translate({largura/2 - 100} {altura/2 + 150})">
                    <text x="0" y="0" font-size="60" font-family="Arial, sans-serif" text-anchor="middle" fill="{preto}" font-weight="bold">CORINTHIANS</text>
                </g>

            </svg>
        """

        # Executa o comando Inkscape
        processo = subprocess.Popen(comando, stdin=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = processo.communicate(input=svg_comandos)

        if processo.returncode != 0:
            print(f"Erro ao executar o Inkscape:\n{stderr}")
            print(stderr)
        else:
            print(f"Bandeira do Corinthians com bicicleta salva em {nome_arquivo}")

    except FileNotFoundError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


# Exemplo de uso
desenhar_bandeira_corinthians_com_bicicleta()