#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de Senhas Seguras com Armazenamento Criptografado
--------------------------------------------------------
Programa profissional que permite:
- Gerar senhas fortes (>=8 caracteres, maiúscula, minúscula, dígito)
- Armazenar senhas em um arquivo .txt criptografado
- Consultar todas as senhas armazenadas (mediante palavra‑chave correta)
- Atualizar o arquivo com novas senhas ou substituir senhas de sites existentes

A palavra‑chave é definida pelo usuário na primeira execução e deve ser usada
sempre nas execuções seguintes. O arquivo gerado é binário (salt + dados
criptografados) e não pode ser lido diretamente.
"""

import re
import json
import os
import secrets
import string
import base64
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

# =============================================================================
# CONSTANTES
# =============================================================================
ARQUIVO_SENHAS = "senhas_criptografadas.txt"  # Nome do cofre de senhas
TAMANHO_SALT = 16                             # Tamanho do salt (bytes)
ITERACOES_PBKDF2 = 100_000                    # Número de iterações do PBKDF2


# =============================================================================
# FUNÇÕES DE VALIDAÇÃO E GERAÇÃO DE SENHA
# =============================================================================
def validar_forca_senha(senha: str) -> bool:
    """
    Verifica se a senha é forte:
    - Pelo menos 8 caracteres
    - Pelo menos uma letra maiúscula
    - Pelo menos uma letra minúscula
    - Pelo menos um dígito

    Utiliza expressões regulares (regex).
    """
    if len(senha) < 8:
        return False
    if not re.search(r'[A-Z]', senha):
        return False
    # CORREÇÃO: antes estava 'az]' -> faltava o colchete e hífen
    if not re.search(r'[a-z]', senha):
        return False
    if not re.search(r'\d', senha):
        return False
    return True


def gerar_senha(tamanho: int) -> str:
    """
    Gera uma senha aleatória que atende aos critérios de força.
    O tamanho é definido pelo usuário (mínimo 8).
    Utiliza loop em vez de recursão para evitar estouro de pilha.
    """
    if tamanho < 8:
        tamanho = 8

    maiusculas = string.ascii_uppercase
    minusculas = string.ascii_lowercase
    digitos = string.digits
    todos = maiusculas + minusculas + digitos

    # Garantir que pelo menos um de cada categoria obrigatória esteja presente
    while True:
        senha_lista = [
            secrets.choice(maiusculas),
            secrets.choice(minusculas),
            secrets.choice(digitos)
        ]
        for _ in range(tamanho - 3):
            senha_lista.append(secrets.choice(todos))

        # Embaralhamento criptograficamente seguro
        rng = secrets.SystemRandom()
        rng.shuffle(senha_lista)

        senha = ''.join(senha_lista)
        if validar_forca_senha(senha):
            return senha
        # Se falhar (improvável), tenta novamente


# =============================================================================
# FUNÇÕES CRIPTOGRÁFICAS
# =============================================================================
def derivar_chave(palavra_chave: str, salt: bytes) -> bytes:
    """
    Deriva uma chave de 32 bytes a partir da palavra‑chave e do salt,
    usando PBKDF2 com SHA-256.
    """
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=ITERACOES_PBKDF2,
    )
    chave = base64.urlsafe_b64encode(kdf.derive(palavra_chave.encode('utf-8')))
    return chave


def criptografar_senhas(dados: dict, palavra_chave: str) -> bytes:
    """
    Serializa o dicionário de senhas para JSON, criptografa com Fernet
    e retorna salt + dados criptografados.
    """
    json_str = json.dumps(dados, indent=2, ensure_ascii=False)
    json_bytes = json_str.encode('utf-8')

    salt = os.urandom(TAMANHO_SALT)
    chave = derivar_chave(palavra_chave, salt)
    fernet = Fernet(chave)
    dados_cripto = fernet.encrypt(json_bytes)

    return salt + dados_cripto


def descriptografar_senhas(conteudo_cripto: bytes, palavra_chave: str) -> dict:
    """
    Extrai o salt, deriva a chave e descriptografa o conteúdo.
    Retorna o dicionário original.
    Lança InvalidToken se a palavra‑chave estiver incorreta.
    """
    if len(conteudo_cripto) < TAMANHO_SALT:
        raise ValueError("Arquivo corrompido: tamanho insuficiente.")

    salt = conteudo_cripto[:TAMANHO_SALT]
    dados_cripto = conteudo_cripto[TAMANHO_SALT:]

    chave = derivar_chave(palavra_chave, salt)
    fernet = Fernet(chave)
    json_bytes = fernet.decrypt(dados_cripto)

    dados = json.loads(json_bytes.decode('utf-8'))
    return dados


def carregar_cofre(palavra_chave: str) -> dict:
    """
    Carrega o arquivo de senhas criptografado.
    Se o arquivo não existir, retorna um dicionário vazio.
    Se existir e a palavra‑chave estiver errada, levanta InvalidToken.
    """
    if not os.path.exists(ARQUIVO_SENHAS):
        return {}

    with open(ARQUIVO_SENHAS, 'rb') as f:
        conteudo = f.read()

    if not conteudo:
        return {}

    return descriptografar_senhas(conteudo, palavra_chave)


def salvar_cofre(dados: dict, palavra_chave: str) -> None:
    """
    Criptografa o dicionário e salva no arquivo.
    """
    conteudo_cripto = criptografar_senhas(dados, palavra_chave)
    with open(ARQUIVO_SENHAS, 'wb') as f:
        f.write(conteudo_cripto)


# =============================================================================
# FUNÇÕES DE INTERAÇÃO COM O USUÁRIO
# =============================================================================
def exibir_menu() -> str:
    """Exibe o menu principal e retorna a opção escolhida."""
    print("\n" + "=" * 50)
    print("GERENCIADOR DE SENHAS SEGURAS")
    print("=" * 50)
    print("1 - Gerar nova senha para um site/aplicação")
    print("2 - Listar todas as senhas armazenadas")
    print("3 - Sair")
    opcao = input("Escolha uma opcao (1/2/3): ").strip()
    return opcao


def obter_palavra_chave() -> str:
    """Solicita a palavra‑chave ao usuário."""
    return input("Digite a palavra-chave para acessar o cofre de senhas: ").strip()


def gerar_e_armazenar(cofre: dict, palavra_chave: str) -> dict:
    """
    Solicita o site e o tamanho da senha, gera uma senha forte,
    atualiza o dicionário e salva.
    Retorna o dicionário atualizado.
    """
    site = input("\nNome do site/aplicacao: ").strip()
    if not site:
        print("[ERRO] Nome do site nao pode ser vazio.")
        return cofre

    while True:
        try:
            tamanho = int(input("Comprimento da senha (minimo 8): "))
            if tamanho < 8:
                print("[ATENCAO] Usando comprimento minimo 8.")
                tamanho = 8
            break
        except ValueError:
            print("[ERRO] Digite um numero inteiro valido.")

    print(f"\n[INFO] Gerando senha com {tamanho} caracteres...")
    senha = gerar_senha(tamanho)

    print(f"[OK] Senha gerada: {senha}")
    print("[ATENCAO] Anote esta senha em local seguro. Ela sera armazenada criptografada.")

    cofre[site] = senha
    salvar_cofre(cofre, palavra_chave)
    print(f"[OK] Senha para '{site}' armazenada com sucesso no arquivo '{ARQUIVO_SENHAS}'.")

    return cofre


def listar_senhas(cofre: dict) -> None:
    """Exibe todas as entradas (site + senha) armazenadas no cofre."""
    if not cofre:
        print("\n[INFO] Nenhuma senha armazenada ainda.")
        return

    print("\n" + "=" * 50)
    print("SENHAS ARMAZENADAS")
    print("=" * 50)
    for i, (site, senha) in enumerate(cofre.items(), start=1):
        print(f"{i}. {site} : {senha}")
    print("=" * 50)


# =============================================================================
# FUNÇÃO PRINCIPAL
# =============================================================================
def main():
    print("=" * 60)
    print("GERADOR DE SENHAS SEGURAS COM ARMAZENAMENTO CRIPTOGRAFADO")
    print("=" * 60)

    palavra_chave = obter_palavra_chave()
    if not palavra_chave:
        print("[ERRO] Palavra-chave nao pode ser vazia. Encerrando.")
        return

    try:
        cofre = carregar_cofre(palavra_chave)
    except InvalidToken:
        print("\n[ERRO] Palavra-chave incorreta! Nao foi possivel descriptografar o arquivo.")
        print("       Verifique a palavra-chave e tente novamente.")
        return
    except Exception as e:
        print(f"\n[ERRO] Falha ao carregar o cofre: {e}")
        return

    # Se o arquivo não existia, cofre é vazio. Criamos o arquivo criptografado vazio.
    if not os.path.exists(ARQUIVO_SENHAS):
        print("[INFO] Nenhum arquivo de senhas encontrado. Um novo cofre sera criado.")
        salvar_cofre(cofre, palavra_chave)
        print(f"[OK] Cofre criado com sucesso em '{ARQUIVO_SENHAS}'.")

    while True:
        opcao = exibir_menu()
        if opcao == "1":
            cofre = gerar_e_armazenar(cofre, palavra_chave)
        elif opcao == "2":
            try:
                # Recarrega o cofre para garantir dados atualizados
                cofre = carregar_cofre(palavra_chave)
                listar_senhas(cofre)
            except InvalidToken:
                print("[ERRO] Palavra-chave incorreta ou arquivo corrompido.")
                break
            except Exception as e:
                print(f"[ERRO] Erro ao listar senhas: {e}")
                break
        elif opcao == "3":
            print("\n[INFO] Encerrando programa. Ate logo!")
            break
        else:
            print("[ERRO] Opcao invalida. Digite 1, 2 ou 3.")


if __name__ == "__main__":
    main()
