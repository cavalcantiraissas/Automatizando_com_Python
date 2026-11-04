# Gerador de QR Code

**Converte um link digitado no terminal em QR Code e salva a imagem `.png` com o nome escolhido.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![qrcode](https://img.shields.io/badge/qrcode-Pillow-555555)](https://pypi.org/project/qrcode/)
[![Coleção](https://img.shields.io/badge/cole%C3%A7%C3%A3o-Automatizando_com_Python-6f42c1)](../)

Um jeito rápido de gerar QR Codes para cartazes, apresentações ou cartões, sem depender de sites de terceiros.

---

## Destaques

- **Nome de arquivo seguro:** os caracteres `< > : " / \ | ? *`, inválidos no Windows, viram `_`.
- **Vários códigos por execução:** ao fim de cada geração, o programa pergunta se deve gerar outro.
- **Tamanho automático:** `QRCode(version=1, ...)` com `make(fit=True)` cresce a versão conforme o tamanho do link.

## Como funciona

O link é codificado com correção de erro nível L (até 7% de recuperação), módulos de 10 px e borda de 4 módulos, o mínimo da especificação. A imagem é gerada em preto e branco e salva no diretório atual.

## Como executar

```bash
cd Gerador-QrCode
pip install -r requirements.txt
python3 main.py
```

```text
=== GERADOR DE QR CODE ===

Digite o link (URL) que deseja converter em QR Code: https://github.com
Digite o título para o arquivo (sem extensão): meu-qrcode

 QR Code gerado com sucesso!
 Arquivo salvo em: /caminho/para/Gerador-QrCode/meu-qrcode.png
 Link: https://github.com
```

## Estrutura do projeto

| Arquivo | Descrição |
|---|---|
| `main.py` | Leitura do link e do nome, geração e gravação da imagem |
| `requirements.txt` | Dependência externa (`qrcode[pil]`) |

## Limitações

- O texto não é validado como URL; qualquer texto vira QR Code.
- Um arquivo com o mesmo nome é sobrescrito sem aviso.

---

[← Automatizando com Python](../)
