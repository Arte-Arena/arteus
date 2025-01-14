import subprocess

def desenhar_bandeira_reino_unido(nome_arquivo="bandeira_reino_unido.svg"):
    """Desenha a bandeira do Reino Unido usando o Inkscape."""

    try:
        # Dimensões (proporção 1:2)
        largura = 900
        altura = 450

        # Cores
        vermelho = "#C8102E"  # Vermelho
        branco = "#FFFFFF"  # Branco
        azul = "#00247D"  # Azul

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

                <rect width="{largura}" height="{altura}" fill="{azul}" />

                {_desenhar_cruzes(largura, altura, vermelho, branco)}

            </svg>
        """

        # Executa o comando Inkscape
        processo = subprocess.Popen(comando, stdin=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = processo.communicate(input=svg_comandos)

        if processo.returncode != 0:
            print(f"Erro ao executar o Inkscape:\n{stderr}")
        else:
            print(f"Bandeira do Reino Unido salva em {nome_arquivo}")

    except FileNotFoundError:
        print("Erro: Inkscape não encontrado. Certifique-se de que está instalado e no PATH do sistema.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def _desenhar_cruzes(largura, altura, vermelho, branco):
    """Desenha as cruzes da Union Jack."""
    largura_cruzes = largura * 0.15
    altura_cruzes = altura * 0.15
    offset = largura * 0.05

    svg = ""

    # Cruz de São Jorge (Inglaterra)
    svg += f'<rect x="{(largura - largura_cruzes) / 2}" y="0" width="{largura_cruzes}" height="{altura}" fill="{branco}" />'
    svg += f'<rect x="0" y="{(altura - altura_cruzes) / 2}" width="{largura}" height="{altura_cruzes}" fill="{branco}" />'
    svg += f'<rect x="{(largura - largura_cruzes*0.6) / 2}" y="0" width="{largura_cruzes*0.6}" height="{altura}" fill="{vermelho}" />'
    svg += f'<rect x="0" y="{(altura - altura_cruzes*0.6) / 2}" width="{largura}" height="{altura_cruzes*0.6}" fill="{vermelho}" />'

    # Cruz de Santo André (Escócia)
    svg += f'<rect transform="rotate(45 {largura/2} {altura/2})" x="{(largura - largura_cruzes) / 2}" y="{(altura - largura_cruzes)/2}" width="{largura_cruzes}" height="{largura*1.5}" fill="{branco}" />'
    svg += f'<rect transform="rotate(-45 {largura/2} {altura/2})" x="{(largura - largura_cruzes) / 2}" y="{(altura - largura_cruzes)/2}" width="{largura_cruzes}" height="{largura*1.5}" fill="{branco}" />'

    # Cruz de São Patrício (Irlanda)
    svg += f'<rect transform="rotate(45 {largura/2} {altura/2})" x="{(largura - largura_cruzes*0.6) / 2}" y="{(altura - largura_cruzes*0.6)/2}" width="{largura_cruzes*0.6}" height="{largura*1.5}" fill="{vermelho}" />'
    svg += f'<rect transform="rotate(-45 {largura/2} {altura/2})" x="{(largura - largura_cruzes*0.6) / 2}" y="{(altura - largura_cruzes*0.6)/2}" width="{largura_cruzes*0.6}" height="{largura*1.5}" fill="{vermelho}" />'

    return svg

# Exemplo de uso
desenhar_bandeira_reino_unido()

