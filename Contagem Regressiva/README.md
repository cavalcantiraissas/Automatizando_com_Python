# Contagem regressiva

**Cadastro de eventos futuros com a contagem de dias que faltam para cada um, em ordem do mais próximo ao mais distante, e limpeza automática dos eventos que já passaram.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Dependências](https://img.shields.io/badge/depend%C3%AAncias-nenhuma-555555)](#como-executar)
[![Coleção](https://img.shields.io/badge/cole%C3%A7%C3%A3o-Automatizando_com_Python-6f42c1)](../)

Para acompanhar prazos, provas, entregas e aniversários num só lugar. Os eventos ficam num arquivo de texto e sobrevivem entre execuções.

---

## Destaques

- **Entradas validadas:** datas no formato `dd/mm/aaaa` e existentes (`31/02/2026` é recusada); títulos sem `;`, o separador do arquivo.
- **Só eventos futuros:** um evento na data de referência ou antes dela não é cadastrado, e o programa informa há quantos dias ele passou.
- **Lista ordenada** pelo número de dias restantes.
- **Limpeza automática:** a cada listagem, os eventos já ocorridos são removidos do arquivo.
- **Sem dependências:** só `os` e `datetime`.

## Como funciona

A data de referência é digitada pelo usuário, tanto no cadastro quanto na listagem. Isso permite simular outra data, por exemplo para conferir como a lista estará daqui a uma semana. Na listagem, o programa:

1. lê `eventos.txt` e descarta os eventos com data igual ou anterior à referência, regravando o arquivo;
2. calcula os dias restantes de cada evento;
3. ordena do menor para o maior prazo e imprime a tabela.

Cada linha de `eventos.txt` segue o formato `titulo;data_de_cadastro;data_do_evento`:

```text
Formatura;10/06/2026;20/12/2026
Prova final;10/06/2026;30/06/2026
```

## Como executar

```bash
cd "Contagem Regressiva"
python3 contagem.py
```

```text
===== SISTEMA DE CONTAGEM REGRESSIVA =====
1. Adicionar novo evento
2. Ver lista de eventos futuros (contagem regressiva ordenada)
3. Sair
```

Exemplo de listagem:

```text
============================================================
Título do Evento               Faltam (dias)   Data do Evento
============================================================
Entrega de projeto             3 dia(s)        15/07/2026
Aniversário da empresa         35 dia(s)       20/08/2026
============================================================
```

## Estrutura do projeto

| Arquivo | Descrição |
|---|---|
| `contagem.py` | Menu, validação de datas, cadastro e listagem |
| `eventos.txt` | Gerado no uso: um evento por linha |

## Limitações

- A data atual é digitada à mão, não lida do relógio do sistema.
- A remoção dos eventos passados é permanente; listar com uma data futura apaga eventos que ainda não aconteceram.
- Títulos com mais de 30 caracteres aparecem truncados na tabela.

---

[← Automatizando com Python](../)
