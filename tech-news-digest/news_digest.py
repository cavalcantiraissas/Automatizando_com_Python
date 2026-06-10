#!/usr/bin/env python3
"""
News Digest – Robô diário de notícias de tecnologia para programadores.

Coleta notícias de feeds RSS e da NewsAPI, opcionalmente resume com IA (Gemini),
e envia um e-mail formatado em HTML para o destinatário configurado.
"""

import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import requests
import feedparser
from dotenv import load_dotenv

# ================= CONFIGURAÇÕES INICIAIS =================
# Carrega as variáveis do arquivo .env que fica na mesma pasta
load_dotenv()

# --- Configurações de e-mail (obrigatórias) ---
# Estas variáveis DEVEM estar definidas no arquivo .env
EMAIL_ORIGEM = os.getenv("EMAIL_ORIGEM")       # Seu e-mail Gmail
EMAIL_DESTINO = os.getenv("EMAIL_DESTINO")     # Para quem enviar (pode ser o mesmo)
SENHA_APP = os.getenv("GMAIL_APP_PASSWORD")    # Senha de aplicativo do Gmail (16 caracteres)

# --- Configurações de notícias (opcionais) ---
NEWS_API_KEY = os.getenv("NEWS_API_KEY")       # Chave da NewsAPI (gratuita)
# Tópicos usados na busca da NewsAPI (palavras‑chave em inglês)
TOPICOS_NOTICIAS = [
    "programming",
    "artificial intelligence",
    "software development",
    "devops",
    "python",
]

# --- Configurações de IA (opcional) ---
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
USAR_IA = False          # Altere para True se tiver uma chave Gemini válida

if USAR_IA and GEMINI_API_KEY:
    import google.generativeai as genai
    genai.configure(api_key=GEMINI_API_KEY)
    modelo_ia = genai.GenerativeModel("gemini-1.5-flash")
    print(" IA Gemini ativada para gerar resumos!")
else:
    USAR_IA = False
    print("ℹ IA desativada. Enviando apenas títulos e links.")


# ================= FUNÇÕES DE COLETA =================
def buscar_noticias_rss():
    """Coleta notícias de feeds RSS pré-definidos (atualiza diariamente)."""
    noticias = []
    feeds_rss = {
        "Hacker News": "https://hnrss.org/frontpage",
        "Dev.to (Python)": "https://dev.to/feed/tag/python",
        "Dev.to (WebDev)": "https://dev.to/feed/tag/webdev",
    }
    for nome_fonte, url_feed in feeds_rss.items():
        try:
            feed = feedparser.parse(url_feed)
            for entrada in feed.entries[:5]:   # 5 notícias por fonte
                noticias.append({
                    "titulo": entrada.title,
                    "link": entrada.link,
                    "fonte": nome_fonte,
                    "descricao": entrada.get("summary", "Sem descrição."),
                    "data": entrada.get("published", datetime.now().strftime("%Y-%m-%d")),
                })
        except Exception as e:
            print(f"Erro no feed '{nome_fonte}': {e}")
    return noticias


def buscar_noticias_api():
    """Coleta notícias via NewsAPI usando os tópicos definidos."""
    if not NEWS_API_KEY:
        print("NewsAPI Key não encontrada. Pulando essa fonte.")
        return []
    noticias = []
    url_base = "https://newsapi.org/v2/everything"
    for topico in TOPICOS_NOTICIAS:
        params = {
            "q": topico,
            "language": "en",
            "sortBy": "publishedAt",
            "pageSize": 3,
            "apiKey": NEWS_API_KEY,
        }
        try:
            resp = requests.get(url_base, params=params, timeout=10)
            resp.raise_for_status()
            dados = resp.json()
            if dados["status"] == "ok":
                for artigo in dados["articles"]:
                    # Evita duplicatas simples (pelo título)
                    if not any(artigo["title"] == n["titulo"] for n in noticias):
                        noticias.append({
                            "titulo": artigo["title"],
                            "link": artigo["url"],
                            "fonte": artigo["source"]["name"],
                            "descricao": artigo.get("description", "Sem descrição."),
                            "data": artigo.get("publishedAt", datetime.now().strftime("%Y-%m-%d")),
                        })
        except Exception as e:
            print(f"Erro na NewsAPI para '{topico}': {e}")
    return noticias


# ================= FUNÇÃO DE SUMARIZAÇÃO COM IA =================
def resumir_com_ia(titulo, descricao):
    """Gera um resumo curto usando o Google Gemini."""
    if not USAR_IA:
        return None
    prompt = f"""
    Artigo: {titulo}
    Descrição: {descricao}
    Gere um resumo de até 20 palavras e uma frase sobre por que isso é relevante para um profissional de tecnologia.
    """
    try:
        resposta = modelo_ia.generate_content(prompt)
        return resposta.text.strip()
    except Exception as e:
        print(f"Erro na IA para '{titulo}': {e}")
        return None


# ================= CONSTRUÇÃO DO E-MAIL HTML =================
def gerar_email_html(noticias):
    """Cria o corpo do e-mail em HTML com as notícias."""
    data_atual = datetime.now().strftime("%d/%m/%Y")
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body {{ font-family: Arial, sans-serif; background-color: #f4f4f4; margin: 0; padding: 20px; }}
            .container {{ max-width: 800px; margin: auto; background-color: white; border-radius: 10px; }}
            .header {{ background-color: #2c3e50; color: white; text-align: center; padding: 20px; border-radius: 10px 10px 0 0; }}
            .header h1 {{ margin: 0; }}
            .noticias {{ padding: 20px; }}
            .card {{ border-bottom: 1px solid #eee; padding: 15px 0; }}
            .fonte {{ background-color: #e74c3c; color: white; font-size: 12px; padding: 2px 8px; border-radius: 20px; display: inline-block; }}
            .titulo a {{ color: #3498db; text-decoration: none; font-weight: bold; }}
            .descricao {{ color: #555; margin: 8px 0; }}
            .resumo-ia {{ background-color: #f9f9f9; border-left: 4px solid #9b59b6; padding: 10px; font-style: italic; margin-top: 10px; }}
            .data {{ color: #999; font-size: 12px; margin-top: 8px; }}
            .footer {{ background-color: #f4f4f4; text-align: center; padding: 15px; font-size: 12px; border-radius: 0 0 10px 10px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1> Seu Resumo Diário de Tecnologia</h1>
                <p>{data_atual}</p>
            </div>
            <div class="noticias">
    """
    for n in noticias:
        html += f"""
        <div class="card">
            <div class="fonte">{n['fonte']}</div>
            <div class="titulo"><a href="{n['link']}" target="_blank">{n['titulo']}</a></div>
            <div class="descricao">{n['descricao']}</div>
        """
        if "resumo_ia" in n and n["resumo_ia"]:
            html += f'<div class="resumo-ia"> <strong>Resumo IA:</strong> {n["resumo_ia"]}</div>'
        html += f'<div class="data"> {n["data"]}</div></div>'

    html += """
            </div>
            <div class="footer">
                Este e-mail foi gerado automaticamente pelo seu Robô de Notícias em Python.
            </div>
        </div>
    </body>
    </html>
    """
    return html


# ================= ENVIO DO E-MAIL =================
def enviar_email(assunto, corpo_html):
    """Envia o e-mail usando SMTP do Gmail."""
    try:
        msg = MIMEMultipart("alternative")
        msg["From"] = EMAIL_ORIGEM
        msg["To"] = EMAIL_DESTINO
        msg["Subject"] = assunto
        msg.attach(MIMEText(corpo_html, "html"))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_ORIGEM, SENHA_APP)
        server.sendmail(EMAIL_ORIGEM, EMAIL_DESTINO, msg.as_string())
        server.quit()
        print(" E-mail enviado com sucesso!")
        return True
    except Exception as e:
        print(f" Erro ao enviar e-mail: {e}")
        return False


# ================= FUNÇÃO PRINCIPAL =================
def main():
    print(" Iniciando coleta de notícias...")
    noticias = buscar_noticias_rss() + buscar_noticias_api()
    print(f" Total de notícias coletadas: {len(noticias)}")

    if not noticias:
        print(" Nenhuma notícia encontrada. Verifique sua conexão.")
        return

    if USAR_IA:
        print(" Gerando resumos com IA...")
        for n in noticias:
            n["resumo_ia"] = resumir_com_ia(n["titulo"], n["descricao"])

    corpo_html = gerar_email_html(noticias)
    assunto = f" Seu Resumo de Tecnologia - {datetime.now().strftime('%d/%m/%Y')}"
    print(" Enviando e-mail...")
    enviar_email(assunto, corpo_html)
    print(" Processo finalizado!")


if __name__ == "__main__":
    main()
