import os
from datetime import datetime

ARQUIVO = "eventos.txt"

def validar_data(data_str):
    """Verifica se a string está no formato dd/mm/aaaa e se é uma data válida."""
    try:
        datetime.strptime(data_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def adicionar_evento():
    """Solicita os dados do evento e os salva no arquivo, exceto se já tiver passado ou for hoje."""
    print("\n--- Adicionar novo evento ---")
    titulo = input("Título do evento: ").strip()
    if not titulo:
        print("Título não pode ficar vazio.")
        return

    data_atual = input("Data atual (dd/mm/aaaa): ").strip()
    if not validar_data(data_atual):
        print("Data atual inválida! Use o formato dd/mm/aaaa.")
        return

    data_evento = input("Data do evento (dd/mm/aaaa): ").strip()
    if not validar_data(data_evento):
        print("Data do evento inválida! Use o formato dd/mm/aaaa.")
        return

    dt_atual = datetime.strptime(data_atual, "%d/%m/%Y")
    dt_evento = datetime.strptime(data_evento, "%d/%m/%Y")

    # Bloqueia evento com data <= data atual
    if dt_evento <= dt_atual:
        if dt_evento == dt_atual:
            print(" O evento ocorre hoje! Não é necessário contagem regressiva. Não foi adicionado.")
        else:
            dias_passados = (dt_atual - dt_evento).days
            print(f" Evento já passou! Há {dias_passados} dia(s) desde a data do evento. Não foi adicionado.")
        return

    with open(ARQUIVO, "a", encoding="utf-8") as f:
        f.write(f"{titulo};{data_atual};{data_evento}\n")
    print(f" Evento '{titulo}' adicionado com sucesso!")

def calcular_diferenca(data_evento_str, data_hoje_str):
    """Retorna o número de dias entre a data do evento e a data de hoje."""
    data_evento = datetime.strptime(data_evento_str, "%d/%m/%Y")
    data_hoje = datetime.strptime(data_hoje_str, "%d/%m/%Y")
    return (data_evento - data_hoje).days

def remover_eventos_passados(data_hoje_str):
    """
    Remove do arquivo todos os eventos cuja data do evento seja <= data_hoje.
    Retorna a lista de eventos restantes (futuros).
    """
    if not os.path.exists(ARQUIVO):
        return []

    with open(ARQUIVO, "r", encoding="utf-8") as f:
        linhas = f.readlines()

    eventos_restantes = []
    for linha in linhas:
        linha = linha.strip()
        if not linha:
            continue
        partes = linha.split(";")
        if len(partes) != 3:
            continue
        titulo, data_inicial, data_evento = partes
        dias = calcular_diferenca(data_evento, data_hoje_str)
        # Mantém apenas eventos futuros (dias > 0)
        if dias > 0:
            eventos_restantes.append(linha)

    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for evento in eventos_restantes:
            f.write(evento + "\n")

    return eventos_restantes

def listar_eventos():
    """Exibe todos os eventos futuros ordenados pelos que faltam menos dias primeiro.
       Antes de exibir, remove os eventos que já ocorreram (data do evento <= data atual)."""
    if not os.path.exists(ARQUIVO):
        print("\nNenhum evento cadastrado ainda.")
        return

    print("\n--- Contagem Regressiva ---")
    hoje = input("Digite a data atual para o cálculo (dd/mm/aaaa): ").strip()
    if not validar_data(hoje):
        print("Data atual inválida! Operação cancelada.")
        return

    eventos_restantes = remover_eventos_passados(hoje)

    if not eventos_restantes:
        print("\n📭 Nenhum evento futuro encontrado. Todos os eventos já ocorreram ou foram removidos.")
        return

    lista_eventos = []
    for linha in eventos_restantes:
        partes = linha.split(";")
        if len(partes) != 3:
            continue
        titulo, data_inicial, data_evento = partes
        dias = calcular_diferenca(data_evento, hoje)
        lista_eventos.append((titulo, data_evento, dias))

    lista_eventos.sort(key=lambda x: x[2])

    print("\n" + "=" * 60)
    print(f"{'Título do Evento':<30} {'Faltam (dias)':<15} {'Data do Evento':<15}")
    print("=" * 60)

    for titulo, data_evento, dias in lista_eventos:
        status = f"{dias} dia(s)"
        print(f"{titulo[:30]:<30} {status:<15} {data_evento:<15}")

    print("=" * 60)

def main():
    while True:
        print("\n===== SISTEMA DE CONTAGEM REGRESSIVA =====")
        print("1. Adicionar novo evento")
        print("2. Ver lista de eventos futuros (contagem regressiva ordenada)")
        print("3. Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            adicionar_evento()
        elif opcao == "2":
            listar_eventos()
        elif opcao == "3":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
