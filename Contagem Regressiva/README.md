# Sistema de Contagem Regressiva

Sistema simples e funcional em Python para gerenciar eventos futuros com contagem regressiva de dias. Ideal para acompanhar prazos importantes, aniversários, Ano Novo, provas, entregas de projetos e muito mais.

---

##  O que o programa resolve

Muitas vezes precisamos saber quantos dias faltam para um evento importante, mas manter isso organizado para vários eventos pode ser confuso.

Este programa resolve:

*  Cadastro de eventos com data atual e data do evento
*  Exibição ordenada dos eventos (do mais próximo ao mais distante)
*  Bloqueio automático de eventos passados ou do dia atual no cadastro
*  Remoção automática de eventos que já ocorreram (ao listar)
*  Persistência dos dados em arquivo `.txt` – os eventos não se perdem ao fechar o programa
*  Interface simples por terminal, fácil de usar e adaptar

---

##  Como foi feito

###  Linguagem e ferramentas

* **Python 3.10+** – Linguagem principal
* **Bibliotecas padrão** – `os` e `datetime` (nenhuma dependência externa)
* **Armazenamento** – Arquivo `eventos.txt` no mesmo diretório do script

###  Lógica principal

#### Validação de datas

* Formato `dd/mm/aaaa`
* Verificação de existência da data (ex.: `31/02` é inválido)

#### Adição de evento

Compara a data atual com a data do evento:

* Se `evento <= data_atual` → mensagem de erro e não salva
* Caso contrário → salva no arquivo `eventos.txt` no formato:

```text
titulo;data_atual;data_evento
```

#### Listagem

O usuário informa uma data de referência (pode ser hoje ou qualquer outra):

* Remove automaticamente do arquivo todos os eventos com `data_evento <= data_referencia`
* Calcula a diferença em dias para os eventos restantes
* Ordena do menor número de dias restantes para o maior
* Exibe em formato de tabela organizada

---

##  Como usar

###  Requisitos

* Python 3 instalado
* Terminal (Linux, macOS, Windows com PowerShell ou CMD)

###  Execução

1. Salve o código em um arquivo, por exemplo:

```text
contagem.py
```

2. Abra o terminal na pasta do arquivo.

3. Execute:

```bash
python contagem.py
```

---

##  Menu principal

```text
===== SISTEMA DE CONTAGEM REGRESSIVA =====
1. Adicionar novo evento
2. Ver lista de eventos futuros (contagem regressiva ordenada)
3. Sair
```

---

## ➕ Adicionar evento

Informe:

* O título do evento (ex.: "Aniversário da empresa")
* A data atual (referência)
* A data do evento (sempre no futuro em relação à data atual)

Se tentar cadastrar um evento com data igual ou anterior à data atual, o programa exibirá uma mensagem de erro e não salvará o registro.

---

##  Ver eventos futuros

Informe a data atual (pode ser a data real ou qualquer outra para simular).

O programa:

* Remove automaticamente eventos que já aconteceram ou ocorrem nesta data
* Exibe os eventos restantes ordenados do que falta menos dias para o que falta mais dias

### Exemplo de saída

```text
============================================================
Título do Evento                Faltam (dias)   Data do Evento
============================================================
Entrega de projeto             3 dia(s)        15/07/2026
Aniversário da empresa         35 dia(s)       20/08/2026
============================================================
```

---

##  Persistência e limpeza

* Os eventos ficam salvos em `eventos.txt` mesmo após fechar o programa.
* A cada listagem, eventos passados são excluídos permanentemente do arquivo.
* Isso mantém o sistema sempre contendo apenas eventos futuros.

---

##  Estrutura do arquivo de dados

Arquivo `eventos.txt`:

```text
Formatura;10/06/2026;20/12/2026
Prova final;10/06/2026;30/06/2026
```

Cada linha segue o formato:

```text
titulo;data_atual_informada;data_do_evento
```

>  Não edite manualmente o arquivo, a menos que conheça o formato. Alterações incorretas podem causar erros na leitura.


---

##  Contribuições

Este é um projeto simples, de código aberto, desenvolvido para fins didáticos e utilitários.

Contribuições são bem-vindas. Sinta-se à vontade para:

* Corrigir bugs
* Melhorar a interface
* Adicionar novas funcionalidades
* Refatorar o código

---

##  Licença

Este projeto está licenciado sob a **Licença MIT**.

Você pode usar, modificar e distribuir livremente.

---

##  Contato

Desenvolvido como uma solução simples para contagem regressiva de eventos.

Para sugestões, melhorias ou relato de problemas, abra uma *Issue* no repositório deste projeto.
