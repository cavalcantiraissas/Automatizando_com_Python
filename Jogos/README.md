# Jogos

**Três jogos de terminal em Python, só com a biblioteca padrão: Bagels, BlackJack e Adivinhe o Número, todos com contas de jogador e ranking que persistem entre execuções.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Dependências](https://img.shields.io/badge/depend%C3%AAncias-nenhuma-555555)](#como-executar)
[![Coleção](https://img.shields.io/badge/cole%C3%A7%C3%A3o-Automatizando_com_Python-6f42c1)](../)

Os jogos exercitam geração de números aleatórios, validação de entrada, controle de fluxo e persistência em arquivos de texto. Cada um guarda as estatísticas dos jogadores num `.txt` próprio, criado na primeira execução.

---

## Jogos

| Jogo | Descrição | Persistência |
|---|---|---|
| [Bagels](./Bagels) | Dedução lógica: descobrir um número de 3 dígitos distintos com as dicas Fermi, Pico e Bagels | `usuarios_bagels.txt` |
| [BlackJack](./BlackJack) | Vinte e um contra o dealer, com saldo virtual e três níveis de aposta | `blackjack_users.txt` |
| [Adivinhe o Número](./Guess%20the%20Number) | Cinco níveis de dificuldade, dicas de proximidade e pontuação acumulada | `ranking_jogo.txt` |

## Como executar

```bash
cd Bagels            # ou BlackJack, ou "Guess the Number"
python3 main.py
```

---

[← Automatizando com Python](../)
