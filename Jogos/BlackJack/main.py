import random
import os
from datetime import datetime

class BlackJackGame:
    def __init__(self):
        self.users_file = "blackjack_users.txt"
        self.initialize_file()
        self.current_user = None
        
    def initialize_file(self):
        """Inicializa o arquivo de usuários se não existir"""
        if not os.path.exists(self.users_file):
            with open(self.users_file, 'w', encoding='utf-8') as f:
                f.write("NOME|VITORIAS|DERROTAS|DINHEIRO|DATA_CRIACAO\n")
    
    def load_users(self):
        """Carrega todos os usuários do arquivo"""
        users = {}
        try:
            with open(self.users_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for line in lines[1:]:  # Pular cabeçalho
                    if line.strip():
                        data = line.strip().split('|')
                        if len(data) == 5:
                            nome, vitorias, derrotas, dinheiro, data_criacao = data
                            users[nome] = {
                                'vitorias': int(vitorias),
                                'derrotas': int(derrotas),
                                'dinheiro': float(dinheiro),
                                'data_criacao': data_criacao
                            }
        except Exception as e:
            print(f"Erro ao carregar usuários: {e}")
        return users
    
    def save_user(self, user_data):
        """Salva todos os usuários no arquivo"""
        try:
            with open(self.users_file, 'w', encoding='utf-8') as f:
                f.write("NOME|VITORIAS|DERROTAS|DINHEIRO|DATA_CRIACAO\n")
                for nome, dados in user_data.items():
                    f.write(f"{nome}|{dados['vitorias']}|{dados['derrotas']}|{dados['dinheiro']}|{dados['data_criacao']}\n")
        except Exception as e:
            print(f"Erro ao salvar usuários: {e}")
    
    def get_or_create_user(self, nome):
        """Obtém usuário existente ou cria novo"""
        users = self.load_users()
        
        if nome in users:
            self.current_user = users[nome]
            self.current_user['nome'] = nome
            print(f"\n Bem-vindo de volta, {nome}!")
            print(f" Dinheiro disponível: R$ {self.current_user['dinheiro']:.2f}")
            print(f" Estatísticas: {self.current_user['vitorias']} vitórias, {self.current_user['derrotas']} derrotas")
        else:
            # Criar novo usuário com dinheiro inicial
            dinheiro_inicial = 1000.00
            data_criacao = datetime.now().strftime("%d/%m/%Y %H:%M")
            self.current_user = {
                'nome': nome,
                'vitorias': 0,
                'derrotas': 0,
                'dinheiro': dinheiro_inicial,
                'data_criacao': data_criacao
            }
            users[nome] = self.current_user.copy()
            self.save_user(users)
            print(f"\n Novo jogador criado: {nome}!")
            print(f" Você recebeu R$ {dinheiro_inicial:.2f} para começar!")
        
        return self.current_user
    
    def update_user_stats(self, venceu, aposta):
        """Atualiza estatísticas do usuário"""
        users = self.load_users()
        
        if self.current_user['nome'] in users:
            if venceu:
                users[self.current_user['nome']]['vitorias'] += 1
                users[self.current_user['nome']]['dinheiro'] += aposta
                self.current_user['dinheiro'] += aposta
            else:
                users[self.current_user['nome']]['derrotas'] += 1
                users[self.current_user['nome']]['dinheiro'] -= aposta
                self.current_user['dinheiro'] -= aposta
            
            self.save_user(users)
    
    def calcular_valor_mao(self, mao):
        """Calcula o valor total da mão considerando As como 1 ou 11"""
        valor = sum(mao)
        num_as = mao.count(11)
        
        while valor > 21 and num_as > 0:
            valor -= 10
            num_as -= 1
        
        return valor
    
    def mostrar_mao(self, mao, nome_jogador, esconder_primeira=False):
        """Mostra a mão do jogador de forma formatada"""
        print(f"\n {nome_jogador}:")
        if esconder_primeira:
            print(f"   [??] {', '.join(str(carta) for carta in mao[1:])}")
            print(f"   Valor: ?")
        else:
            print(f"   {', '.join(str(carta) for carta in mao)}")
            valor = self.calcular_valor_mao(mao)
            print(f"   Valor: {valor}")
    
    def sortear_carta(self):
        """Sorteia uma carta (2-10, J=10, Q=10, K=10, A=11)"""
        cartas = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  # 11 é Ás
        return random.choice(cartas)
    
    def realizar_aposta(self, dificuldade):
        """Realiza a aposta do jogador baseado na dificuldade"""
        aposta_maxima = min(500, self.current_user['dinheiro'])
        aposta_minima = 10
        
        if dificuldade == 1:  # Fácil
            aposta_minima = 10
            aposta_maxima = min(100, self.current_user['dinheiro'])
        elif dificuldade == 2:  # Médio
            aposta_minima = 50
            aposta_maxima = min(300, self.current_user['dinheiro'])
        else:  # Difícil
            aposta_minima = 100
            aposta_maxima = min(500, self.current_user['dinheiro'])
        
        while True:
            try:
                print(f"\n Dinheiro disponível: R$ {self.current_user['dinheiro']:.2f}")
                print(f" Limites de aposta: R$ {aposta_minima:.2f} - R$ {aposta_maxima:.2f}")
                aposta = float(input("Digite o valor da sua aposta: R$ "))
                
                if aposta < aposta_minima:
                    print(f" Aposta mínima é R$ {aposta_minima:.2f}!")
                elif aposta > aposta_maxima:
                    print(f" Aposta máxima para esta dificuldade é R$ {aposta_maxima:.2f}!")
                elif aposta > self.current_user['dinheiro']:
                    print(" Você não tem dinheiro suficiente!")
                else:
                    return aposta
            except ValueError:
                print(" Por favor, digite um valor válido!")
    
    def jogar_blackjack(self):
        """Executa uma partida de BlackJack"""
        if not self.current_user or self.current_user['dinheiro'] <= 0:
            print("\n Você não tem dinheiro para jogar!")
            return False
        
        # Mostrar menu de dificuldade
        print("\n" + "="*50)
        print(" NÍVEL DE DIFICULDADE")
        print("="*50)
        print("1️  FÁCIL    - Apostas menores (R$10-R$100)")
        print("2️  MÉDIO    - Apostas médias (R$50-R$300)")
        print("3️  DIFÍCIL  - Apostas altas (R$100-R$500)")
        print("-"*50)
        
        while True:
            try:
                dificuldade = int(input("Escolha a dificuldade (1-3): "))
                if dificuldade in [1, 2, 3]:
                    break
                else:
                    print(" Opção inválida! Escolha 1, 2 ou 3.")
            except ValueError:
                print(" Digite um número válido!")
        
        # Realizar aposta
        aposta = self.realizar_aposta(dificuldade)
        
        print(f"\n Iniciando partida com aposta de R$ {aposta:.2f}!")
        print("-"*50)
        
        # Inicializar mãos
        jogador_mao = []
        dealer_mao = []
        
        # Distribuir cartas iniciais
        jogador_mao.append(self.sortear_carta())
        jogador_mao.append(self.sortear_carta())
        dealer_mao.append(self.sortear_carta())
        dealer_mao.append(self.sortear_carta())
        
        # Mostrar mãos iniciais
        self.mostrar_mao(jogador_mao, "JOGADOR")
        self.mostrar_mao(dealer_mao, "DEALER", esconder_primeira=True)
        
        # Turno do jogador
        while True:
            valor_jogador = self.calcular_valor_mao(jogador_mao)
            
            if valor_jogador > 21:
                print(f"\n JOGADOR estourou com {valor_jogador} pontos!")
                return False, aposta
            
            print(f"\n Pontuação atual: {valor_jogador}")
            acao = input(" [C]omprar carta ou [P]arar? ").upper()
            
            if acao == 'C':
                nova_carta = self.sortear_carta()
                jogador_mao.append(nova_carta)
                print(f"\n Você comprou um {nova_carta}!")
                self.mostrar_mao(jogador_mao, "JOGADOR")
                self.mostrar_mao(dealer_mao, "DEALER", esconder_primeira=True)
            elif acao == 'P':
                break
            else:
                print(" Opção inválida! Digite C para comprar ou P para parar.")
        
        # Verificar se jogador não estourou
        valor_jogador = self.calcular_valor_mao(jogador_mao)
        if valor_jogador > 21:
            return False, aposta
        
        # Turno do dealer (só compra se tiver menos que 17)
        print("\n" + "="*30)
        print(" TURNO DO DEALER")
        print("="*30)
        self.mostrar_mao(dealer_mao, "DEALER")
        
        while self.calcular_valor_mao(dealer_mao) < 17:
            nova_carta = self.sortear_carta()
            dealer_mao.append(nova_carta)
            print(f"\n Dealer comprou um {nova_carta}!")
            self.mostrar_mao(dealer_mao, "DEALER")
        
        # Calcular pontuações finais
        valor_dealer = self.calcular_valor_mao(dealer_mao)
        valor_jogador = self.calcular_valor_mao(jogador_mao)
        
        print("\n" + "="*50)
        print(" RESULTADO FINAL")
        print("="*50)
        print(f" JOGADOR: {valor_jogador} pontos")
        print(f" DEALER: {valor_dealer} pontos")
        print("-"*50)
        
        # Determinar vencedor
        if valor_dealer > 21:
            print(" DEALER ESTOUROU! VOCÊ GANHOU! ")
            return True, aposta
        elif valor_jogador > valor_dealer:
            print(" PARABÉNS! VOCÊ GANHOU! ")
            return True, aposta
        elif valor_jogador < valor_dealer:
            print(" QUE PENA! VOCÊ PERDEU! ")
            return False, aposta
        else:
            print(" EMPATE! SEU DINHEIRO FOI DEVOLVIDO! ")
            return None, aposta
    
    def mostrar_ranking(self):
        """Mostra ranking dos jogadores"""
        users = self.load_users()
        
        if not users:
            print("\n Nenhum jogador cadastrado ainda!")
            return
        
        # Criar ranking baseado em vitórias
        ranking = sorted(users.items(), key=lambda x: x[1]['vitorias'], reverse=True)
        
        print("\n" + "="*60)
        print(" RANKING DOS JOGADORES ")
        print("="*60)
        print(f"{'Pos.':<5} {'Nome':<20} {'Vitórias':<10} {'Derrotas':<10} {'Dinheiro':<12}")
        print("-"*60)
        
        for i, (nome, dados) in enumerate(ranking[:10], 1):
            print(f"{i:<5} {nome[:20]:<20} {dados['vitorias']:<10} {dados['derrotas']:<10} R$ {dados['dinheiro']:<10.2f}")
        
        print("-"*60)
        
        # Mostrar estatísticas gerais
        total_vitorias = sum(dados['vitorias'] for dados in users.values())
        total_derrotas = sum(dados['derrotas'] for dados in users.values())
        total_partidas = total_vitorias + total_derrotas
        
        if total_partidas > 0:
            taxa_vitoria = (total_vitorias / total_partidas) * 100
            print(f"\n Estatísticas Globais:")
            print(f"   • Total de partidas: {total_partidas}")
            print(f"   • Taxa de vitória geral: {taxa_vitoria:.1f}%")
            print(f"   • Total de jogadores: {len(users)}")
    
    def main_menu(self):
        """Menu principal do jogo"""
        while True:
            print("\n" + "="*50)
            print(" BLACKJACK - O JOGO DE CARTAS ")
            print("="*50)
            print("1️   INICIAR PARTIDA")
            print("2️   VER RANKING")
            print("3️   SAIR DO JOGO")
            print("-"*50)
            
            opcao = input("Escolha uma opção (1-3): ").strip()
            
            if opcao == '1':
                if not self.current_user or self.current_user['dinheiro'] <= 0:
                    nome = input("\n Digite seu nome de usuário: ").strip()
                    if nome:
                        self.get_or_create_user(nome)
                
                if self.current_user and self.current_user['dinheiro'] > 0:
                    venceu, aposta = self.jogar_blackjack()
                    
                    if venceu is not None:
                        self.update_user_stats(venceu, aposta)
                        
                        # Verificar se jogador ainda tem dinheiro
                        if self.current_user['dinheiro'] <= 0:
                            print("\n GAME OVER! Você ficou sem dinheiro!")
                            print("Crie um novo usuário para jogar novamente!")
                            self.current_user = None
                        else:
                            print(f"\n Seu novo saldo: R$ {self.current_user['dinheiro']:.2f}")
                elif self.current_user and self.current_user['dinheiro'] <= 0:
                    print("\n Você não tem dinheiro para jogar!")
                    print("Por favor, crie um novo usuário!")
                    self.current_user = None
                    
            elif opcao == '2':
                self.mostrar_ranking()
                
            elif opcao == '3':
                if self.current_user:
                    print(f"\n Até logo, {self.current_user['nome']}!")
                print(" Obrigado por jogar BlackJack! Volte sempre! ")
                break
            else:
                print(" Opção inválida! Escolha 1, 2 ou 3.")

# Função para mostrar introdução do jogo
def mostrar_introducao():
    print("\n" + "="*60)
    print(" BEM-VINDO AO BLACKJACK!")
    print("="*60)
    print(" REGRAS DO JOGO:")
    print("-"*40)
    print("• O objetivo é fazer 21 pontos ou chegar o mais perto possível")
    print("• Cartas de 2 a 10 valem seu valor nominal")
    print("• J, Q, K valem 10 pontos")
    print("• Ás vale 11 ou 1 ponto (o que for melhor para sua mão)")
    print("• Você joga contra o dealer (computador)")
    print("• Quanto maior a dificuldade, maior o valor mínimo da aposta")
    print("• Seu dinheiro é atualizado conforme você ganha ou perde")
    print("-"*40)
    print(" COMO JOGAR:")
    print("• Digite seu nome para começar")
    print("• Escolha a dificuldade (1-Fácil, 2-Médio, 3-Difícil)")
    print("• Faça sua aposta dentro dos limites da dificuldade")
    print("• Decida se quer comprar mais cartas ou parar")
    print("• Quem tiver mais pontos sem passar de 21 vence!")
    print("="*60)
    
    input("\nPressione ENTER para continuar...")

# Função principal
def main():
    # Limpar tela
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Mostrar introdução
    mostrar_introducao()
    
    # Iniciar jogo
    game = BlackJackGame()
    game.main_menu()

if __name__ == "__main__":
    main()
