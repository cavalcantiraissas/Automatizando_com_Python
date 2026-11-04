# Automatizando com Python

**Scripts, ferramentas e automações em Python para resolver problemas do dia a dia: envio de e-mails, resumo diário de notícias, cofre de senhas, QR Codes, contagem regressiva e jogos de terminal.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![SMTP](https://img.shields.io/badge/e--mail-SMTP-EA4335?logo=gmail&logoColor=white)](#projetos)
[![Criptografia](https://img.shields.io/badge/cryptography-Fernet_%2B_PBKDF2-555555)](./gerador_de_senhas.py)
[![Status](https://img.shields.io/badge/cole%C3%A7%C3%A3o-em_andamento-yellow)](#motivação)

Cada pasta é um projeto independente, com README próprio que explica o que ele faz, como funciona por dentro, como executar e quais são as limitações conhecidas. Todos rodam no terminal, em Linux, macOS e Windows.

---

## Sumário

- [Projetos](#projetos)
- [Como executar](#como-executar)
- [Configuração com `.env`](#configuração-com-env)
- [Motivação](#motivação)
- [Autora](#autora)

---

## Projetos

| Projeto | O que faz | Dependências |
|---|---|---|
| [Automação de e-mails](./Automacao-emails) | Envia e-mails por SMTP, lembra os contatos mais usados, registra o histórico e reenvia a última mensagem | `python-dotenv` |
| [Tech News Digest](./tech-news-digest) | Coleta notícias de tecnologia (Hacker News, Dev.to, NewsAPI) e envia um resumo em HTML por e-mail, com resumos opcionais por IA | `requests`, `feedparser`, `python-dotenv` |
| [Gerador de senhas](./gerador_de_senhas.py) | Gera senhas fortes e as guarda num cofre criptografado com uma palavra-chave mestra | `cryptography` |
| [Gerador de QR Code](./Gerador-QrCode) | Converte um link em QR Code e salva a imagem `.png` | `qrcode[pil]` |
| [Contagem regressiva](./Contagem%20Regressiva) | Cadastra eventos e mostra quantos dias faltam, removendo os que já passaram | nenhuma |
| [Jogos](./Jogos) | Bagels, BlackJack e Adivinhe o Número, com contas de jogador e ranking salvos em arquivo | nenhuma |

## Como executar

Cada projeto roda a partir da própria pasta, porque os arquivos de dados (histórico, ranking, cofre) são gravados no diretório atual:

```bash
cd Automacao-emails
python3 -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt                      # só nos projetos com dependências
python3 main.py
```

No Windows, use `python` no lugar de `python3`. O comando exato de cada projeto está no README dele.

## Configuração com `.env`

Os projetos que enviam e-mail ([Automação de e-mails](./Automacao-emails) e [Tech News Digest](./tech-news-digest)) leem as credenciais de um arquivo `.env`. O repositório traz apenas o modelo, `.env.example`, com valores fictícios:

```bash
cp .env.example .env    # depois edite o .env com os seus dados
```

O `.env` está no [`.gitignore`](.gitignore) e nunca deve ser versionado. Para o Gmail, use uma [senha de app](https://myaccount.google.com/apppasswords) (exige verificação em duas etapas), não a senha da conta.

## Motivação

A ideia nasceu da leitura de *Automate the Boring Stuff with Python*, de Al Sweigart: computadores são ótimos em repetição, desde que bem instruídos. Se uma tarefa precisa ser feita dez ou cem vezes, vale ensinar a máquina a fazê-la. Cada script aqui é um pequeno ganho de produtividade, e a coleção cresce conforme surgem novos problemas para automatizar.

## Autora

**Raissa Cavalcanti** · [GitHub](https://github.com/cavalcantiraissas) · [LinkedIn](https://www.linkedin.com/in/cavalcantiraissa/)
