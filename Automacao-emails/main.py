import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')
SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = int(os.getenv('SMTP_PORT', 587))

ARQUIVO_CONTAGENS = 'email_counts.txt'
ARQUIVO_HISTORICO = 'historico_envios.txt'
ULTIMO_EMAIL = {'assunto': '', 'corpo': ''}  # guarda o último e-mail enviado

def carregar_contagens():
    contagens = {}
    if os.path.exists(ARQUIVO_CONTAGENS):
        with open(ARQUIVO_CONTAGENS, 'r', encoding='utf-8') as f:
            for linha in f:
                linha = linha.strip()
                if linha:
                    email, qtd = linha.split('|')
                    contagens[email] = int(qtd)
    return contagens

def salvar_contagens(contagens):
    with open(ARQUIVO_CONTAGENS, 'w', encoding='utf-8') as f:
        for email, qtd in contagens.items():
            f.write(f"{email}|{qtd}\n")

def atualizar_contagem(email, contagens):
    contagens[email] = contagens.get(email, 0) + 1
    salvar_contagens(contagens)

def listar_contatos_frequentes(contagens, limite=5):
    ordenados = sorted(contagens.items(), key=lambda x: x[1], reverse=True)
    return [email for email, _ in ordenados[:limite]]

def registrar_envio(destinatarios, assunto):
    """Registra o envio no arquivo de histórico."""
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open(ARQUIVO_HISTORICO, 'a', encoding='utf-8') as f:
        for email in destinatarios:
            f.write(f"{data_hora} | {email} | {assunto}\n")

def exibir_historico():
    """Mostra todos os envios registrados."""
    if not os.path.exists(ARQUIVO_HISTORICO):
        print("\n Nenhum e-mail enviado ainda.\n")
        return
    print("\n HISTÓRICO DE ENVIOS:")
    with open(ARQUIVO_HISTORICO, 'r', encoding='utf-8') as f:
        for linha in f:
            linha = linha.strip()
            if linha:
                print(linha)
    print("")

def enviar_email(remetente, senha, servidor, porta, destinatarios, assunto, corpo):
    try:
        msg = MIMEMultipart()
        msg['From'] = remetente
        msg['To'] = ', '.join(destinatarios)
        msg['Subject'] = assunto
        msg.attach(MIMEText(corpo, 'plain', 'utf-8'))

        with smtplib.SMTP(servidor, porta) as server:
            server.starttls()
            server.login(remetente, senha)
            server.sendmail(remetente, destinatarios, msg.as_string())
        print("\n E-mail(s) enviado(s) com sucesso!")
        return True
    except Exception as e:
        print(f"\n Erro ao enviar e-mail: {e}")
        return False

def ler_corpo_interativamente():
    print("\n Digite o corpo do e-mail (para finalizar, digite 'FIM' em uma linha nova):")
    linhas = []
    while True:
        linha = input()
        if linha.strip().upper() == 'FIM':
            break
        linhas.append(linha)
    return "\n".join(linhas)

def obter_corpo():
    print("\n--- Corpo do e-mail ---")
    opcao = input("Deseja (1) digitar o texto ou (2) ler de um arquivo? [1/2]: ").strip()
    if opcao == '2':
        caminho = input("Caminho do arquivo de texto: ").strip()
        try:
            with open(caminho, 'r', encoding='utf-8') as f:
                corpo = f.read()
            print(" Conteúdo carregado do arquivo.")
            return corpo
        except Exception as e:
            print(f" Erro ao ler arquivo: {e}. Voltando para digitação manual.")
            return ler_corpo_interativamente()
    else:
        return ler_corpo_interativamente()

def obter_destinatarios(contagens):
    destinatarios = []
    frequentes = listar_contatos_frequentes(contagens)

    if frequentes:
        print("\n Contatos mais usados:")
        for i, email in enumerate(frequentes, start=1):
            print(f"{i} - {email} (enviado {contagens[email]} vez(es))")
        print("0 - Digitar novo e-mail")
        print("99 - Enviar para múltiplos contatos (digitar ou selecionar vários)")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == '0':
            novo_email = input("Digite o e-mail do destinatário: ").strip()
            if novo_email:
                destinatarios.append(novo_email)
        elif opcao == '99':
            modo = input("Deseja (1) digitar vários e-mails separados por vírgula ou (2) selecionar índices? ").strip()
            if modo == '1':
                emails = input("Digite os e-mails separados por vírgula: ").strip()
                destinatarios = [e.strip() for e in emails.split(',') if e.strip()]
            elif modo == '2':
                indices = input("Digite os números dos contatos (ex: 1,3,5): ").strip()
                if indices:
                    for idx in indices.split(','):
                        try:
                            i = int(idx.strip())
                            if 1 <= i <= len(frequentes):
                                destinatarios.append(frequentes[i-1])
                        except ValueError:
                            pass
                add_novo = input("Adicionar mais algum e-mail manualmente? (s/n): ").strip().lower()
                if add_novo == 's':
                    extra = input("Digite o e-mail extra: ").strip()
                    if extra:
                        destinatarios.append(extra)
            else:
                print("Opção inválida.")
                return []
        else:
            try:
                idx = int(opcao)
                if 1 <= idx <= len(frequentes):
                    destinatarios.append(frequentes[idx-1])
                else:
                    print("Índice inválido.")
                    return []
            except ValueError:
                print("Entrada inválida.")
                return []
    else:
        print("\nNenhum contato frequente ainda.")
        email = input("Digite o e-mail do destinatário: ").strip()
        if email:
            destinatarios.append(email)
        else:
            return []
    return destinatarios

def enviar_novo_email(contagens):
    global ULTIMO_EMAIL
    destinatarios = obter_destinatarios(contagens)
    if not destinatarios:
        print("Nenhum destinatário informado. Operação cancelada.")
        return

    assunto = input("Assunto do e-mail: ").strip()
    if not assunto:
        print("Assunto não pode ser vazio.")
        return

    corpo = obter_corpo()
    if not corpo.strip():
        print("Corpo do e-mail não pode ser vazio.")
        return

    # Guarda o último e-mail para possível reenvio
    ULTIMO_EMAIL['assunto'] = assunto
    ULTIMO_EMAIL['corpo'] = corpo

    sucesso = enviar_email(EMAIL, PASSWORD, SMTP_SERVER, SMTP_PORT,
                           destinatarios, assunto, corpo)
    if sucesso:
        for email in destinatarios:
            atualizar_contagem(email, contagens)
        registrar_envio(destinatarios, assunto)
        # Recarrega contagens para refletir atualizações
        contagens.update(carregar_contagens())
    return contagens

def reenviar_ultimo_email(contagens):
    global ULTIMO_EMAIL
    if not ULTIMO_EMAIL['assunto'] or not ULTIMO_EMAIL['corpo']:
        print("\n Nenhum e-mail enviado anteriormente para reutilizar.")
        return contagens

    print(f"\n Reenviando o último e-mail (assunto: {ULTIMO_EMAIL['assunto']})")
    destinatarios = obter_destinatarios(contagens)
    if not destinatarios:
        print("Nenhum destinatário informado. Operação cancelada.")
        return contagens

    sucesso = enviar_email(EMAIL, PASSWORD, SMTP_SERVER, SMTP_PORT,
                           destinatarios, ULTIMO_EMAIL['assunto'], ULTIMO_EMAIL['corpo'])
    if sucesso:
        for email in destinatarios:
            atualizar_contagem(email, contagens)
        registrar_envio(destinatarios, ULTIMO_EMAIL['assunto'])
        contagens.update(carregar_contagens())
    return contagens

def exibir_menu():
    print("\n" + "="*40)
    print(" MENU PRINCIPAL")
    print("="*40)
    print("1 - Enviar novo e-mail")
    print("2 - Listar histórico de envios")
    print("3 - Reenviar o último e-mail para novo(s) destinatário(s)")
    print("4 - Sair")
    return input("Escolha uma opção: ").strip()

def main():
    print("=== ENVIO AUTOMÁTICO DE E-MAILS ===\n")
    print(f"Remetente configurado: {EMAIL}\n")

    contagens = carregar_contagens()

    while True:
        opcao = exibir_menu()

        if opcao == '1':
            contagens = enviar_novo_email(contagens)
        elif opcao == '2':
            exibir_historico()
        elif opcao == '3':
            contagens = reenviar_ultimo_email(contagens)
        elif opcao == '4':
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
