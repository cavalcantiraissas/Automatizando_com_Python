import qrcode
from PIL import Image
import os

def criar_qrcode():
    print("=== GERADOR DE QR CODE ===")
    print()
    
    # Solicitar o link ao usuário
    link = input("Digite o link (URL) que deseja converter em QR Code: ").strip()
    
    # Verificar se o link foi fornecido
    if not link:
        print("Erro: Nenhum link foi fornecido!")
        return
    
    # Solicitar o título/nome do arquivo
    titulo = input("Digite o título para o arquivo (sem extensão): ").strip()
    
    # Verificar se o título foi fornecido
    if not titulo:
        print("Erro: Nenhum título foi fornecido!")
        return
    
    # Remover caracteres inválidos para nome de arquivo
    caracteres_invalidos = '<>:"/\\|?*'
    for char in caracteres_invalidos:
        titulo = titulo.replace(char, '_')
    
    # Nome do arquivo com extensão .png
    nome_arquivo = f"{titulo}.png"
    
    # Caminho completo (pasta do projeto atual)
    caminho_completo = os.path.join(os.getcwd(), nome_arquivo)
    
    try:
        # Configurar o QR Code
        qr = qrcode.QRCode(
            version=1,  # Controla o tamanho do QR Code (1 é o menor)
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Correção de erros
            box_size=10,  # Tamanho de cada box em pixels
            border=4,  # Tamanho da borda (mínimo é 4 pela especificação)
        )
        
        # Adicionar o link ao QR Code
        qr.add_data(link)
        qr.make(fit=True)
        
        # Criar a imagem do QR Code
        imagem_qr = qr.make_image(fill_color="black", back_color="white")
        
        # Salvar a imagem na pasta do projeto
        imagem_qr.save(caminho_completo)
        
        print()
        print(f" QR Code gerado com sucesso!")
        print(f" Arquivo salvo em: {caminho_completo}")
        print(f" Link: {link}")
        
    except Exception as e:
        print(f" Erro ao gerar o QR Code: {e}")

def main():
    while True:
        criar_qrcode()
        print()
        resposta = input("Deseja gerar outro QR Code? (s/n): ").strip().lower()
        if resposta != 's':
            print("Programa encerrado!")
            break
        print()

if __name__ == "__main__":
    main()
