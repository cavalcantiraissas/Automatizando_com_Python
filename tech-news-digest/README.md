#  Tech News Digest – Robô Diário de Notícias para Programadores

Receba todos os dias, diretamente no seu e‑mail, um resumo curado das principais notícias de tecnologia, programação e boas práticas. Ideal para quem quer se manter atualizado sem perder tempo navegando em dezenas de sites.

##  Por que este projeto?

Profissionais de tecnologia precisam acompanhar inovações, novas ferramentas e tendências diariamente. Porém, buscar ativamente por essas informações consome tempo e pode levar à procrastinação.

**Tech News Digest** resolve isso:
-  Agrega notícias de fontes confiáveis (Hacker News, Dev.to, NewsAPI).
-  Opcionalmente resume artigos com IA (Google Gemini).
-  Entrega tudo no seu e‑mail, num formato limpo e fácil de ler.
-  Pode ser agendado para rodar automaticamente todos os dias.

##  Como usar

### Pré‑requisitos
- Python 3.8 ou superior
- Uma conta Gmail (para enviar os e‑mails)
- (Opcional) Chaves gratuitas da NewsAPI e/ou Google Gemini

### 1. Clone ou baixe os arquivos

### 2. Crie e ative um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows
```
### 3. Instale as idependências
```bash
pip install requests beautifulsoup4 lxml feedparser python-dotenv google-generativeai
```

### 4. Configure suas credenciais
Edite o arquivo .env (copie de .env.example se existir) e preencha:

- EMAIL_ORIGEM e EMAIL_DESTINO (seu e‑mail Gmail)
- GMAIL_APP_PASSWORD – senha de aplicativo do Gmail
- NEWS_API_KEY (opcional) – obtenha em https://newsapi.org

### 5. Teste o Script
```bash
python3 news_digest.py
```
