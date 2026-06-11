#  Gerador de QR Code em Python

Um programa desenvolvido em Python que permite gerar QR Codes a partir de links (URLs) informados pelo usuário diretamente pelo terminal.

O QR Code gerado é salvo automaticamente como uma imagem no formato `.png` dentro da pasta do projeto.

---

##  Objetivo

O objetivo deste projeto é facilitar a criação de QR Codes de maneira rápida e prática através de uma interface de linha de comando (CLI).

O usuário informa:

- O link que deseja converter em QR Code;
- O nome do arquivo de saída;

O programa realiza a validação dos dados, cria a imagem do QR Code e salva o arquivo no diretório atual do projeto.

---

##  Funcionalidades

-  Conversão de URLs em QR Code;
-  Geração de imagens no formato `.png`;
-  Definição personalizada do nome do arquivo;
-  Tratamento de caracteres inválidos em nomes de arquivos;
-  Possibilidade de gerar vários QR Codes em uma única execução;
-  Compatível com Windows, Linux e macOS.

---

##  Tecnologias e Ferramentas Utilizadas

- **Python 3**
- **qrcode** – Biblioteca responsável pela criação dos QR Codes;
- **Pillow (PIL)** – Biblioteca utilizada para manipulação e salvamento de imagens;
- **os** – Módulo nativo do Python utilizado para manipulação de caminhos e diretórios.

---

##  Estrutura do Projeto

```text
gerador-qrcode/
│
├── main.py             # Código principal do programa
├── README.md           # Documentação do projeto
```

---

##  Pré-requisitos

Antes de executar o projeto, é necessário possuir:

- Python 3 instalado na máquina;
- Gerenciador de pacotes `pip`.

Para verificar a instalação, execute:

```bash
python --version
```

ou:

```bash
python3 --version
```

---

##  Instalação das Dependências

1. Clone o repositório

2. Acesse a pasta do projeto

3. Instale as bibliotecas necessárias:

```bash
pip install qrcode[pil] pillow
```

---

##  Como Executar o Programa

###  Windows

No Prompt de Comando (CMD) ou PowerShell:

```powershell
python main.py
```

---

###  Linux

No terminal:

```bash
python3 main.py
```

---

###  macOS

No Terminal:

```bash
python3 main.py
```

---

##  Exemplo de Utilização

```text
=== GERADOR DE QR CODE ===

Digite o link (URL) que deseja converter em QR Code:
https://github.com

Digite o título para o arquivo (sem extensão):
meu-qrcode

QR Code gerado com sucesso!

Arquivo salvo em:
C:\Projetos\gerador-qrcode\meu-qrcode.png

Link:
https://github.com
```

---

##  Tratamento de Erros

O programa realiza algumas validações para garantir uma melhor experiência de uso:

- Impede a geração de QR Codes sem uma URL informada;
- Impede a criação de arquivos sem nome;
- Substitui caracteres inválidos no nome do arquivo por `_`;
- Captura possíveis erros durante o processo de geração da imagem.

---

##  Fluxo de Funcionamento

1. O usuário informa uma URL;
2. O usuário escolhe um nome para o arquivo;
3. O sistema valida as entradas fornecidas;
4. O QR Code é gerado utilizando a biblioteca `qrcode`;
5. A imagem é salva em formato `.png`;
6. O usuário pode optar por gerar um novo QR Code ou encerrar o programa.



##  Licença

Este projeto é de uso livre para fins de estudo e aprendizado.
