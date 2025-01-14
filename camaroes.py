import subprocess

def desenhar_bandeira_camaroes(nome_arquivo="bandeira_camaroes.svg"):
    """
    Desenha a bandeira de Camarões usando o Inkscape via linha de comando.

    Args:
        nome_arquivo: O nome do arquivo SVG de saída.
    """

    try:
        # Dimensões (proporção 2:3)
        largura = 900
        altura = 600

        # Cores (hexadecimais)
        verde = "#007A50"
        vermelho = "#CE1126"
        amarelo = "#FECB00"

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

                <rect width="{largura/3}" height="{altura}" fill="{verde}" />

                <rect x="{largura/3}" width="{largura/3}" height="{altura}" fill="{vermelho}" />

                <rect x="{2*largura/3}" width="{largura/3}" height="{altura}" fill="{amarelo}" />

                <polygon points="{largura/2},{(altura/2)-50} {(largura/2)+15,{(altura/2)-15}} {(largura/2)+50},{(altura/2)-15} {(largura/2)+25},{(altura/2)+15} {(largura/2)+30},{(altura/2)+50} {(largura/2)},{(altura/2)+30} {(largura/2)-30},{(altura/2)+50} {(largura/2)-25},{(altura/2)+15} {(largura/2)-50},{(altura/2)-15} {(largura/2)-15},{(altura/2)-15}" fill="{amarelo}" />
            </svg>
        """

        # Executa o comando Inkscape
        processo = subprocess.Popen(comando, stdin=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = processo.communicate(input=svg_comandos)

        if processo.returncode != 0:
            print(f"Erro ao executar o Inkscape:\n{stderr}")
        else:
            print(f"Bandeira de Camarões salva em {nome_arquivo}")

    except FileNotFoundError:
        print("Erro: Inkscape não encontrado. Certifique-se de que está instalado e no PATH do sistema.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Exemplo de uso
desenhar_bandeira_camaroes()