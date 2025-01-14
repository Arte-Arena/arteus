import subprocess

def desenhar_bandeira_egito(nome_arquivo="bandeira_egito.svg"):
    """
    Desenha a bandeira do Egito usando o Inkscape via linha de comando.

    Args:
        nome_arquivo: O nome do arquivo SVG de saída.
    """

    try:
        # Largura e altura da bandeira (proporção 2:3)
        largura = 900
        altura = 600

        # Cores (hexadecimais)
        vermelho = "#C8102E"
        branco = "#FFFFFF"
        preto = "#000000"
        ouro = "#B3995D" # Cor aproximada para o falcão

        # Comando principal do Inkscape
        comando = [
            "inkscape",
            "--batch-process",
            "--pipe", # Leitura de comandos via pipe
            f"--export-filename={nome_arquivo}",
            "--export-type=svg"
        ]

        # Comandos para o Inkscape (SVG embutido)
        svg_comandos = f"""
            <svg
                xmlns="http://www.w3.org/2000/svg"
                width="{largura}"
                height="{altura}">

                <rect width="{largura}" height="{altura/3}" fill="{vermelho}" />

                <rect y="{altura/3}" width="{largura}" height="{altura/3}" fill="{branco}" />

                <rect y="{2*altura/3}" width="{largura}" height="{altura/3}" fill="{preto}" />

                <g transform="translate({largura/2} {altura/2}) scale(0.2)">
                    <ellipse rx="250" ry="150" fill="{ouro}" />
                    <polygon points="0,-200 -100,-100 -50,0 0,50 50,0 100,-100" fill="{ouro}" />
                </g>

            </svg>
        """

        # Executa o comando Inkscape com os comandos SVG
        processo = subprocess.Popen(comando, stdin=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = processo.communicate(input=svg_comandos)

        if processo.returncode != 0:
            print(f"Erro ao executar o Inkscape:\n{stderr}")
        else:
            print(f"Bandeira do Egito salva em {nome_arquivo}")

    except FileNotFoundError:
        print("Erro: Inkscape não encontrado. Certifique-se de que está instalado e no PATH do sistema.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")