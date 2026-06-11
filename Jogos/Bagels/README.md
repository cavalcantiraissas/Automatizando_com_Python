#  Jogo Bagels em Python

Um jogo de adivinhação baseado em lógica, desenvolvido em Python utilizando programação orientada a objetos (POO). O jogador deve descobrir um número secreto de 3 dígitos sem repetição, utilizando dicas fornecidas pelo sistema a cada tentativa.

Além da mecânica tradicional do Bagels, o projeto possui sistema de usuários, armazenamento de estatísticas e ranking de jogadores.

---

##  Objetivo do Projeto

O objetivo deste projeto é implementar o clássico jogo **Bagels** utilizando conceitos fundamentais da programação, como:

- Programação Orientada a Objetos (POO);
- Manipulação de arquivos;
- Estruturas de dados;
- Controle de fluxo;
- Validação de entradas;
- Persistência de dados em arquivos locais.

O jogador tem até **10 tentativas** para descobrir o número secreto gerado aleatoriamente pelo sistema.

---

#  Como Funciona o Jogo

O programa gera um número secreto composto por **3 dígitos diferentes**.

A cada tentativa, o jogador recebe dicas de acordo com o seu palpite:

| Dica | Significado |
|------|-------------|
| **Fermi** | Um dígito está correto e está na posição correta |
| **Pico** | Um dígito está correto, mas está na posição errada |
| **Bagels** | Nenhum dígito do palpite existe no número secreto |

### Exemplo

Número secreto:

```text
427
```

Palpite do jogador:

```text
123
```

Resultado:

```text
Pico
```

Isso significa que o número **2** existe no número secreto, mas está na posição incorreta.

---

##  Funcionalidades

-  Sistema de login e cadastro automático de jogadores;
-  Salvamento permanente de usuários em arquivo `.txt`;
-  Registro de vitórias e derrotas;
-  Sistema de ranking de jogadores;
-  Cálculo de taxa de vitória;
-  Geração aleatória de números secretos sem repetição;
-  Validação dos palpites inseridos;
-  Menu interativo com múltiplas opções;
-  Possibilidade de jogar diversas partidas em uma mesma execução;
-  Compatível com Windows, Linux e macOS.

---

##  Tecnologias Utilizadas

- **Python 3**
- **random** - Geração aleatória do número secreto;
- **os** - Manipulação de arquivos e verificação de existência de dados;
- **Programação Orientada a Objetos (POO)**

---

##  Estrutura do Projeto

```text
jogo-bagels/
│
├── main.py                  # Código principal do jogo
└── README.md                # Documentação do projeto
```

---

##  Pré-requisitos

Antes de executar o projeto, é necessário possuir:

- Python 3 instalado na máquina.

Verifique a instalação com:

```bash
python --version
```

ou:

```bash
python3 --version
```

---

##  Como Executar o Projeto

1. Clone o repositório

2. Entre na pasta do projeto

---

###  Windows

Abra o Prompt de Comando (CMD) ou PowerShell e execute:

```powershell
python main.py
```

---

###  Linux

Abra o terminal e execute:

```bash
python3 main.py
```

---

###  macOS

Abra o Terminal e execute:

```bash
python3 main.py
```

---

##  Menu Principal

Ao iniciar o programa, o jogador terá acesso ao seguinte menu:

```text
1. Iniciar nova partida
2. Ver ranking
3. Ver instruções
4. Trocar usuário
5. Sair do jogo
```

---

##  Sistema de Dados

As informações dos jogadores são armazenadas no arquivo:

```text
usuarios_bagels.txt
```

Cada registro contém:

- Nome do jogador;
- Quantidade de vitórias;
- Quantidade de derrotas.

Esses dados são carregados automaticamente sempre que o jogo é iniciado, permitindo que o progresso dos usuários seja mantido entre diferentes execuções.

---

##  Fluxo de Funcionamento

1. O jogador realiza o login informando seu nome;
2. Caso o usuário não exista, uma nova conta é criada automaticamente;
3. O sistema exibe o menu principal;
4. Uma nova partida pode ser iniciada;
5. O número secreto é gerado aleatoriamente;
6. O jogador possui até 10 tentativas para acertar;
7. As dicas Fermi, Pico ou Bagels são exibidas após cada palpite;
8. O sistema atualiza as estatísticas de vitória ou derrota;
9. O ranking dos jogadores pode ser consultado a qualquer momento.

