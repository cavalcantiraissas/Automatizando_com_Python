#  Gerador de Senhas Seguras com Cofre Criptografado

[![Licença MIT](https://img.shields.io/badge/Licen%C3%A7a-MIT-blue.svg)](LICENSE)
[![Python 3.6+](https://img.shields.io/badge/Python-3.6%2B-green.svg)](https://www.python.org/)

##  Sobre o projeto

Este programa é uma solução prática e segura para **gerar senhas fortes** e **armazená-las de forma criptografada** em um único arquivo `.txt`.  
Ele resolve o problema comum de criar senhas fáceis de lembrar, mas frágeis, e de armazená‑las de maneira insegura (bloco de notas, planilhas sem proteção).

O projeto foi desenvolvido como parte de estudos do livro *Automatize Tarefas Chatos com Python* (Al Sweigart) e tem **foco educacional**, demonstrando:

- Uso de expressões regulares (`regex`) para validação de força de senha.
- Geração criptograficamente segura com o módulo `secrets`.
- Criptografia simétrica (Fernet) e derivação de chave com PBKDF2.
- Persistência de dados com JSON e arquivos binários.

---

##  Funcionalidades

| Função                        | Descrição                                                                 |
|-------------------------------|---------------------------------------------------------------------------|
| **Geração de senha forte**     | Mínimo 8 caracteres, incluindo maiúsculas, minúsculas e dígitos.         |
| **Validação com regex**        | Verifica os critérios de segurança usando padrões `re`.                   |
| **Cofre criptografado**        | Arquivo `senhas_criptografadas.txt` protegido por palavra‑chave mestra.   |
| **Consulta de senhas**         | Lista todas as entradas (site + senha) após autenticação.                 |
| **Substituição/Atualização**   | Mesmo site: a senha antiga é sobrescrita pela nova.                       |
| **Portabilidade**              | Funciona em Windows, macOS e Linux (desde que Python 3.6+ esteja instalado). |

---

##  Tecnologias e ferramentas utilizadas

- **Python 3.12** (linguagem principal)
- **Bibliotecas padrão**:
  - `re` → validação com regex
  - `secrets` → geração de números aleatórios criptograficamente seguros
  - `json` → serialização dos dados
  - `os`, `base64`, `hashlib`, `string`
- **Biblioteca externa**:
  - [`cryptography`](https://cryptography.io/) → fornece o esquema Fernet (AES‑128 em modo CBC) e a derivação PBKDF2HMAC.

---

##  Como clonar e executar

### 1. Clonar o repositório
 
### 2. Criar um ambiente virtual

Windows(PowerSheell)
```bash
python -m venv venv
.\venv\Scripts\activate
```
MacOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar a dependência
```bash
pip install cryptography
```
### 4. Executar o programa
```bash
python gerador_de_senhas.py
```
> Nota: Em alguns sistemas, o comando pode ser python3 em vez de python.

## Estrutura de Segurança

- A palavra‑chave mestra nunca é armazenada em texto puro.
- A chave de criptografia é derivada com PBKDF2 (100.000 iterações, SHA‑256) e um salt aleatório de 16 bytes.
- O arquivo senhas_criptografadas.txt contém salt + ciphertext – mesmo aberto, não revela as senhas.
- A descriptografia só ocorre após fornecimento da palavra‑chave correta no momento da execução.

> Contribuições são bem‑vindas! Abra uma issue ou um pull request.

## Autora

Raissa Cavalcanti
- [Github](https://github.com/cavalcantiraissas)
- [Linkedin]([https://www.linkedin.com/in/cavalcantiraissa/)
- E‑mail: Cavalcanti.c.raissa@gmail.com


