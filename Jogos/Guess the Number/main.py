import random
import os
from datetime import datetime

ARQUIVO_RANKING = "ranking_jogo.txt"

# Dicionário com pontuações por nível
PONTUACOES_NIVEL = {
    1: 100,   # Fácil (1-50)
    2: 200,   # Médio (1-100)
    3: 400,   # Difícil (1-200)
    4: 700,   # Muito Difícil (1-500)
    5: 1000   # Insano (1-1000)
}

def normalizar_nome(user):
    """Normaliza o nome do usuário para comparação (case insensitive)"""
    return user.strip().lower()

def carregar_ranking():
    """Carrega o ranking do arquivo TXT"""
    ranking = {}
    if os.path.exists(ARQUIVO_RANKING):
        with open(ARQUIVO_RANKING, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                try:
                    # Formato: user|vitorias|derrotas|taxa|pontuacao
                    partes = linha.strip().split('|')
                    if len(partes) == 5:
                        user, vitorias, derrotas, taxa, pontuacao = partes
                        ranking[user] = {
                            'vitorias': int(vitorias),
                            'derrotas': int(derrotas),
                            'taxa': float(taxa),
                            'pontuacao': int(pontuacao)
                        }
                except:
                    continue
    return ranking

def salvar_ranking(ranking):
    """Salva o ranking no arquivo TXT"""
    with open(ARQUIVO_RANKING, 'w', encoding='utf-8') as arquivo:
        for user, dados in ranking.items():
            arquivo.write(f"{user}|{dados['vitorias']}|{dados['derrotas']}|{dados['taxa']:.2f}|{dados['pontuacao']}\n")

def atualizar_ranking(user, venceu, pontuacao_nivel=0):
    """Atualiza as estatísticas do usuário no ranking"""
    user_norm = normalizar_nome(user)
    ranking = carregar_ranking()
    
    if user_norm not in ranking:
        ranking[user_norm] = {
            'vitorias': 0, 
            'derrotas': 0, 
            'taxa': 0.0,
            'pontuacao': 0
        }
    
    if venceu:
        ranking[user_norm]['vitorias'] += 1
        ranking[user_norm]['pontuacao'] += pontuacao_nivel
    else:
        ranking[user_norm]['derrotas'] += 1
    
    # Calcula taxa de vitórias
    total_jogos = ranking[user_norm]['vitorias'] + ranking[user_norm]['derrotas']
    if total_jogos > 0:
        ranking[user_norm]['taxa'] = (ranking[user_norm]['vitorias'] / total_jogos) * 100
    else:
        ranking[user_norm]['taxa'] = 0.0
    
    salvar_ranking(ranking)
    return ranking[user_norm]

def exibir_ranking():
    """Exibe o ranking ordenado por pontuação total"""
    ranking = carregar_ranking()
    
    if not ranking:
        print("\n" + "="*60)
        print(" RANKING".center(60))
        print("="*60)
        print("Nenhum jogador registrado ainda!")
        return
    
    # Ordena por pontuação (decrescente)
    ranking_ordenado = sorted(ranking.items(), key=lambda x: x[1]['pontuacao'], reverse=True)
    
    print("\n" + "="*70)
    print(" RANKING DOS JOGADORES (POR PONTUAÇÃO) ".center(70))
    print("="*70)
    print(f"{'Posição':<8} {'Usuário':<15} {'Vitórias':<10} {'Derrotas':<10} {'Taxa %':<8} {'Pontuação':<10}")
    print("-"*70)
    
    for pos, (user, dados) in enumerate(ranking_ordenado, 1):
        # Destaca o top 3 com medalhas
        medalha = ""
        if pos == 1:
            medalha = "🥇 "
        elif pos == 2:
            medalha = "🥈 "
        elif pos == 3:
            medalha = "🥉 "
        
        print(f"{medalha}{pos:<5} {user:<15} {dados['vitorias']:<10} {dados['derrotas']:<10} {dados['taxa']:.2f}%{' '*3} {dados['pontuacao']:<10}")
    print("="*70)
    
    # Exibe informações sobre pontuação
    print("\n SISTEMA DE PONTUAÇÃO:")
    print(f"{'Nível':<12} {'Intervalo':<15} {'Pontos por vitória':<20}")
    print("-"*50)
    print(f"{'1 - Fácil':<12} {'1-50':<15} {PONTUACOES_NIVEL[1]:<20}")
    print(f"{'2 - Médio':<12} {'1-100':<15} {PONTUACOES_NIVEL[2]:<20}")
    print(f"{'3 - Difícil':<12} {'1-200':<15} {PONTUACOES_NIVEL[3]:<20}")
    print(f"{'4 - Muito Difícil':<12} {'1-500':<15} {PONTUACOES_NIVEL[4]:<20}")
    print(f"{'5 - Insano':<12} {'1-1000':<15} {PONTUACOES_NIVEL[5]:<20}")

def jogar():
    """Função principal do jogo"""
    print("\n" + " NOVA PARTIDA ".center(50))
    print("="*50)
    
    # Solicitar nome do usuário
    user = input("Digite seu nome de usuário: ").strip()
    if not user:
        print("Nome inválido! Usando 'Anônimo'.")
        user = "Anônimo"
    
    # Solicitar nível de dificuldade
    while True:
        try:
            print("\n NÍVEIS DE DIFICULDADE E PONTUAÇÃO:")
            print(f"{'1 - Fácil':<20} {'(1-50)':<10} {' +' + str(PONTUACOES_NIVEL[1]) + ' pontos':<15}")
            print(f"{'2 - Médio':<20} {'(1-100)':<10} {' +' + str(PONTUACOES_NIVEL[2]) + ' pontos':<15}")
            print(f"{'3 - Difícil':<20} {'(1-200)':<10} {' +' + str(PONTUACOES_NIVEL[3]) + ' pontos':<15}")
            print(f"{'4 - Muito Difícil':<20} {'(1-500)':<10} {' +' + str(PONTUACOES_NIVEL[4]) + ' pontos':<15}")
            print(f"{'5 - Insano':<20} {'(1-1000)':<10} {' +' + str(PONTUACOES_NIVEL[5]) + ' pontos':<15}")
            
            nivel = int(input("\nEscolha o nível (1-5): "))
            if nivel in [1, 2, 3, 4, 5]:
                max_num = {
                    1: 50,
                    2: 100,
                    3: 200,
                    4: 500,
                    5: 1000
                }[nivel]
                pontuacao_vitoria = PONTUACOES_NIVEL[nivel]
                break
            else:
                print("Opção inválida! Escolha um número entre 1 e 5.")
        except ValueError:
            print("Entrada inválida! Digite um número.")
    
    # Sortear número
    numero_secreto = random.randint(1, max_num)
    tentativas_restantes = 10
    acertou = False
    
    print(f"\n Jogo iniciado! Você tem 10 tentativas para acertar o número (1-{max_num})")
    print(f" Pontuação em jogo: {pontuacao_vitoria} pontos se vencer!")
    print(" Dica: O sistema dirá se seu palpite está PERTO ou LONGE do número secreto!\n")
    
    for tentativa in range(1, 11):
        print(f" Tentativa {tentativa}/10 - Tentativas restantes: {10 - tentativa + 1}")
        
        # Solicitar palpite
        while True:
            try:
                palpite = int(input("Digite seu palpite: "))
                if 1 <= palpite <= max_num:
                    break
                else:
                    print(f" Palpite deve estar entre 1 e {max_num}!")
            except ValueError:
                print(" Entrada inválida! Digite um número inteiro.")
        
        # Verificar palpite
        if palpite == numero_secreto:
            print(f"\n PARABÉNS! Você acertou o número {numero_secreto} em {tentativa} tentativas! ")
            print(f" Você ganhou {pontuacao_vitoria} pontos!")
            acertou = True
            break
        
        # Dar dicas
        diferenca = abs(palpite - numero_secreto)
        percentual_distancia = (diferenca / max_num) * 100
        
        if percentual_distancia <= 10:
            print(" MUITO PERTO! Você está quase lá!")
        elif percentual_distancia <= 20:
            print(" PERTO! Continue assim!")
        elif percentual_distancia <= 30:
            print(" RAZOAVELMENTE PERTO")
        elif percentual_distancia <= 50:
            print(" LONGE")
        else:
            print(" MUITO LONGE!")
        
        # Dica extra para ajudar
        if palpite < numero_secreto:
            print(f" Dica: O número é MAIOR que {palpite}")
        else:
            print(f" Dica: O número é MENOR que {palpite}")
        
        print("-" * 40)
    
    if not acertou:
        print(f"\n FIM DE JOGO! O número secreto era {numero_secreto} ")
        print(f" Você perdeu a oportunidade de ganhar {pontuacao_vitoria} pontos!")
    
    # Atualizar ranking
    estatisticas = atualizar_ranking(user, acertou, pontuacao_vitoria if acertou else 0)
    
    # Mostrar estatísticas atuais do usuário
    print("\n" + "="*50)
    print(" SUAS ESTATÍSTICAS ATUALIZADAS")
    print("="*50)
    print(f"Usuário: {user}")
    print(f"Vitórias: {estatisticas['vitorias']}")
    print(f"Derrotas: {estatisticas['derrotas']}")
    print(f"Taxa de vitórias: {estatisticas['taxa']:.2f}%")
    print(f"Pontuação total: {estatisticas['pontuacao']} pontos")
    
    # Se venceu, mostra pontuação desta partida
    if acertou:
        print(f"Pontos nesta partida: +{pontuacao_vitoria}")
    
    print("="*50)
    
    input("\nPressione ENTER para continuar...")

def main():
    """Menu principal do jogo"""
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpa tela
        print("="*60)
        print(" ADIVINHE O NÚMERO - SISTEMA DE PONTUAÇÃO ".center(60))
        print("="*60)
        print("1️  Iniciar novo jogo")
        print("2️  Ver ranking")
        print("3️  Sair")
        print("="*60)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            jogar()
        elif opcao == "2":
            exibir_ranking()
            input("\nPressione ENTER para continuar...")
        elif opcao == "3":
            print("\n Obrigado por jogar! Até mais!")
            break
        else:
            print("\n Opção inválida! Tente novamente.")
            input("Pressione ENTER para continuar...")

if __name__ == "__main__":
    main()
