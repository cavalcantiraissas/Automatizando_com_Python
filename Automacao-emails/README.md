# Ferramenta de Automação de E-mails

Aplicação Python em linha de comando que automatiza o envio de e-mails, rastreia o histórico de envios e simplifica a seleção de contatos com base na frequência de uso. Ideal para usuários que enviam conteúdos repetitivos para múltiplos destinatários.

## Propósito

Esta ferramenta elimina a necessidade de digitar manualmente os endereços de e-mail a cada envio. Ela memoriza os endereços já utilizados, conta quantas vezes cada um foi usado e oferece um menu de seleção rápida.

Além disso, registra cada e-mail enviado com data e hora e permite reenviar a última mensagem para novos destinatários sem redigitar o assunto e o corpo.

## Tecnologias e Ferramentas

* **Python 3** - Linguagem de programação principal
* **smtplib** - Envio de e-mails via SMTP
* **email.mime** - Construção de mensagens compatíveis com MIME
* **python-dotenv** - Carregamento seguro de credenciais a partir de um arquivo `.env`
* **datetime** - Registro de data e hora dos envios
* **Arquivos de texto** - Persistência da frequência de contatos e do histórico de envios

## Funcionalidades

* **Gerenciamento seguro de credenciais** - E-mail e senha armazenados em arquivo `.env` (utilize uma Senha de App do Gmail)
* **Registro de frequência de contatos** - Cada destinatário é salvo em `email_counts.txt` com sua contagem de uso
* **Seleção inteligente de destinatários** - Contatos mais usados são exibidos com a quantidade de envios para seleção rápida
* **Múltiplos destinatários** - Envie o mesmo e-mail para vários endereços de uma só vez, digitando ou selecionando da lista
* **Entrada flexível da mensagem**

  * Digite o corpo do e-mail interativamente (finalize com `FIM` em uma nova linha)
  * Ou carregue o conteúdo a partir de um arquivo de texto
* **Histórico de envios** - Cada e-mail enviado é registrado em `historico_envios.txt` com data, destinatário(s) e assunto
* **Reenvio do último e-mail** - Reutilize o assunto e o corpo do e-mail mais recente para novos destinatários sem redigitar
* **Menu interativo** –-Escolha entre enviar novo e-mail, listar histórico, reenviar o último e-mail ou sair

## Como Executar

### Pré-requisitos

* Python 3.6 ou superior instalado
* Uma conta de e-mail com suporte a SMTP (Gmail, Outlook, etc.)
* Para Gmail:

  * Ative a Verificação em Duas Etapas
  * Crie uma Senha de App

### Instalação

1. Clone ou baixe os arquivos do projeto para um diretório:

   * `main.py` – Programa principal
   * `.env` – Arquivo de configuração (criar manualmente)
   * `email_counts.txt` – Criado automaticamente na primeira execução
   * `historico_envios.txt` – Criado automaticamente na primeira execução

2. Instale a dependência necessária:

```bash
pip install python-dotenv
```

3. Crie um arquivo `.env` no mesmo diretório com o seguinte conteúdo:

```env
EMAIL=seuemail@gmail.com
PASSWORD=sua_senha_de_app
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

Substitua:

* `seuemail@gmail.com` pelo seu endereço de e-mail
* `sua_senha_de_app` pela Senha de App gerada pelo Gmail

Caso utilize outro provedor, ajuste `SMTP_SERVER` e `SMTP_PORT` conforme necessário.

### Execução

No terminal, navegue até o diretório do projeto e execute:

```bash
python main.py
```

Ou, em sistemas Linux/macOS:

```bash
python3 main.py
```

## Guia de Uso

1. O programa exibe o e-mail remetente configurado.
2. Se não houver contatos registrados, será solicitado um destinatário manualmente.
3. Após o primeiro envio, o endereço é armazenado e sua contagem de uso é incrementada.
4. Nas execuções seguintes, os contatos mais frequentes aparecem numerados.

### Seleção de Destinatários

Você pode:

* Digitar o número correspondente para selecionar um contato
* Digitar `0` para informar um novo e-mail
* Digitar `99` para enviar para múltiplos destinatários:

  * Informando e-mails separados por vírgula
  * Ou selecionando vários índices

### Composição da Mensagem

1. Informe o assunto do e-mail.
2. Escolha como fornecer o corpo da mensagem:

#### Opção 1 – Digitação Interativa

Digite o texto linha por linha e finalize com:

```text
FIM
```

em uma linha separada.

#### Opção 2 – Carregar de Arquivo

Informe o caminho completo de um arquivo `.txt` contendo o conteúdo do e-mail.

### Após o Envio

O programa:

* Envia a mensagem
* Atualiza a frequência dos contatos
* Registra o envio no histórico

### Menu Principal

Após cada operação, será exibido o menu:

| Opção | Descrição                  |
| ----- | -------------------------- |
| 1     | Enviar novo e-mail         |
| 2     | Listar histórico de envios |
| 3     | Reenviar último e-mail     |
| 4     | Sair do programa           |

## Estrutura dos Arquivos

| Arquivo                | Finalidade                                                          |
| ---------------------- | ------------------------------------------------------------------- |
| `.env`                 | Armazena credenciais e configurações SMTP (não deve ser versionado) |
| `email_counts.txt`     | Armazena contatos e quantidade de utilização (`email\|quantidade`)  |
| `historico_envios.txt` | Registra data, hora, destinatários e assunto dos envios             |
| `main.py`              | Script principal da aplicação                                       |

## Solução de Problemas

### Erros de Autenticação

Se estiver utilizando Gmail:

* Verifique se a Verificação em Duas Etapas está ativada
* Utilize uma Senha de App

Desde 2022, o Gmail não aceita login SMTP com senha comum.

### E-mail Não Enviado

Verifique:

* Sua conexão com a internet
* O servidor SMTP configurado
* A porta SMTP utilizada

### O Comando `FIM` Não Encerra a Digitação

Certifique-se de que:

* `FIM` está sozinho em uma linha
* Não há espaços antes ou depois do texto

### Histórico Não Registrado

Verifique se o programa possui permissão de escrita no diretório do projeto.

## Licença

Este projeto é open source e está disponível sob a licença MIT.
