# BlackJack em Python

## Sobre o projeto

Este projeto consiste na implementação de um jogo de BlackJack desenvolvido em Python para execução via terminal. O sistema permite que jogadores criem contas, realizem apostas com saldo virtual, disputem partidas contra o dealer e acompanhem seu desempenho por meio de estatísticas e ranking.

O projeto foi desenvolvido utilizando conceitos de Programação Orientada a Objetos (POO), manipulação de arquivos, controle de fluxo, validação de dados e geração de números aleatórios.

---

## Objetivos

O projeto tem como finalidade aplicar conceitos fundamentais de desenvolvimento de software, incluindo:

- Programação Orientada a Objetos;
- Manipulação de arquivos para persistência de dados;
- Controle de estados do jogo;
- Validação de entradas do usuário;
- Estruturas de dados nativas do Python;
- Implementação da lógica do jogo BlackJack.

---

## Funcionalidades

- Cadastro automático de novos jogadores;
- Sistema de login com carregamento de dados existentes;
- Saldo inicial virtual para novos usuários;
- Sistema de apostas baseado em níveis de dificuldade;
- Controle de vitórias e derrotas;
- Atualização automática do saldo do jogador;
- Ranking de jogadores;
- Armazenamento permanente dos dados em arquivo local;
- Cálculo automático do valor das cartas, incluindo a regra especial do Ás;
- Interface interativa por linha de comando.

---

## Regras do jogo

O objetivo do BlackJack é alcançar uma pontuação igual ou mais próxima de 21 pontos sem ultrapassar esse valor.

Valores das cartas:

| Carta | Valor |
| :--- | :--- |
| 2 a 10 | Valor numérico |
| J, Q e K | 10 pontos |
| Ás | 1 ou 11 pontos, conforme a melhor jogada |

O jogador pode realizar duas ações durante sua rodada:

- Comprar uma nova carta;
- Encerrar sua jogada e manter sua pontuação atual.

Após o turno do jogador, o dealer realiza suas jogadas automaticamente seguindo as regras definidas pelo sistema.

---

## Níveis de dificuldade

O jogo possui três níveis de dificuldade que definem os limites das apostas:

| Dificuldade | Valor mínimo | Valor máximo |
| :--- | :---: | :---: |
| Fácil | R$ 10,00 | R$ 100,00 |
| Médio | R$ 50,00 | R$ 300,00 |
| Difícil | R$ 100,00 | R$ 500,00 |

---

## Tecnologias utilizadas

- Python 3;
- Biblioteca `random` para sorteio das cartas;
- Biblioteca `os` para manipulação de arquivos e comandos do sistema operacional;
- Biblioteca `datetime` para registro da data de criação dos usuários.

---

## Estrutura do projeto

```text
blackjack/
│
├── main.py
├── blackjack_users.txt
└── README.md
```

Descrição dos arquivos:

- `main.py`: contém toda a lógica do jogo, regras, menus e gerenciamento dos jogadores;
- `blackjack_users.txt`: arquivo utilizado para armazenar as informações dos usuários;
- `README.md`: documentação do projeto.

---

## Pré-requisitos

Para executar o projeto é necessário possuir:

- Python 3 instalado na máquina.

Verifique a instalação utilizando:

```bash
python --version
```

ou:

```bash
python3 --version
```

---

## Instalação

1. Clone o repositório:

2. Acesse a pasta do projeto:


Não é necessário instalar dependências externas, pois o projeto utiliza apenas módulos nativos da biblioteca padrão do Python.

---

## Execução

### Windows

Execute o comando no Prompt de Comando ou PowerShell:

```powershell
python main.py
```

### Linux

Execute o comando no terminal:

```bash
python3 main.py
```

### macOS

Execute o comando no Terminal:

```bash
python3 main.py
```

---

## Persistência dos dados

As informações dos jogadores são armazenadas no arquivo `blackjack_users.txt`.

Cada registro contém:

- Nome do usuário;
- Quantidade de vitórias;
- Quantidade de derrotas;
- Saldo disponível;
- Data de criação da conta.

Os dados são carregados automaticamente ao iniciar o programa e atualizados ao final de cada partida.

---

## Fluxo de funcionamento

1. O usuário inicia o programa;
2. Um novo jogador pode ser criado ou um usuário existente pode ser carregado;
3. O jogador escolhe a dificuldade da partida;
4. Uma aposta é realizada dentro dos limites permitidos;
5. As cartas são distribuídas para o jogador e para o dealer;
6. O jogador decide comprar novas cartas ou encerrar sua rodada;
7. O dealer executa sua estratégia automaticamente;
8. O sistema determina o vencedor;
9. O saldo e as estatísticas são atualizados;
10. O ranking pode ser consultado a qualquer momento.

---
