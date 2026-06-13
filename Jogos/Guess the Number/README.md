#  Jogo de Adivinhação de Números em Python

Um jogo de adivinhação desenvolvido em Python onde o jogador deve descobrir um número secreto gerado aleatoriamente pelo sistema. O projeto conta com diferentes níveis de dificuldade, sistema de pontuação, ranking de jogadores e armazenamento permanente das estatísticas em arquivo local.

---

##  Objetivo do Projeto

O objetivo deste projeto é aplicar conceitos fundamentais de programação por meio de um jogo interativo em terminal, explorando:

- Programação estruturada;
- Manipulação de arquivos;
- Geração de números aleatórios;
- Estruturas de dados;
- Controle de fluxo;
- Validação de entradas;
- Sistema de pontuação e classificação de jogadores.

O jogador possui até **10 tentativas** para descobrir o número secreto e acumular pontos de acordo com a dificuldade escolhida.

---

##  Como Funciona o Jogo

Ao iniciar uma partida, o jogador deve:

1. Informar um nome de usuário;
2. Escolher um dos cinco níveis de dificuldade;
3. Tentar descobrir o número secreto dentro do limite de 10 tentativas;
4. Utilizar as dicas fornecidas pelo sistema para se aproximar do número correto.

Durante a partida, o jogo informa se o palpite está:

- Muito perto;
- Perto;
- Razoavelmente perto;
- Longe;
- Muito longe;

Além disso, o sistema informa se o número secreto é maior ou menor que o valor digitado, auxiliando o jogador nas próximas tentativas.

---

##  Sistema de Dificuldade e Pontuação

Cada nível possui um intervalo diferente de números e uma quantidade específica de pontos por vitória:

| Nível | Dificuldade | Intervalo | Pontos por vitória |
|------|-------------|-----------|-------------------|
| 1 | Fácil | 1 a 50 | 100 pontos |
| 2 | Médio | 1 a 100 | 200 pontos |
| 3 | Difícil | 1 a 200 | 400 pontos |
| 4 | Muito Difícil | 1 a 500 | 700 pontos |
| 5 | Insano | 1 a 1000 | 1000 pontos |

Quanto maior a dificuldade, maior será a recompensa pela vitória.

---

##  Funcionalidades

-  Sistema de identificação de jogadores;
-  Salvamento automático das estatísticas em arquivo `.txt`;
-  Ranking ordenado pela pontuação total;
-  Destaque para os três melhores jogadores;
-  Registro de vitórias, derrotas e taxa de aproveitamento;
-  Cinco níveis de dificuldade;
-  Geração aleatória de números secretos;
-  Sistema de dicas de proximidade e direção;
-  Limpeza automática da tela no terminal;
-  Possibilidade de jogar várias partidas em uma mesma execução;
-  Tratamento de entradas inválidas;
-  Compatível com Windows, Linux e macOS.

---

##  Tecnologias Utilizadas

- **Python 3**
- **random** — Utilizado para gerar números aleatórios;
- **os** — Utilizado para manipulação de arquivos e comandos do sistema operacional;
- **datetime** — Importado no projeto para manipulação de data e hora;
- Manipulação de arquivos `.txt`;
- Estruturas de dados com dicionários;
- Programação estruturada.

---

##  Estrutura do Projeto

```text
jogo-adivinhe-o-numero/
│
├── main.py              # Código principal do jogo
├── ranking_jogo.txt     # Arquivo responsável pelo ranking dos jogadores
└── README.md            # Documentação do projeto
```

---

##  Pré-requisitos

Antes de executar o projeto é necessário possuir:

- Python 3 instalado na máquina.

Para verificar a instalação, utilize:

```bash
python --version
```

ou:

```bash
python3 --version
```

---

##  Instalação e Execução

1. Clone o repositório:

2. Acesse a pasta do projeto

O projeto utiliza apenas bibliotecas nativas do Python, portanto não é necessário instalar dependências externas.
