import random
import os

class JogoBagels:
    def __init__(self):
        self.arquivo_usuarios = "usuarios_bagels.txt"
        self.usuarios = {}
        self.usuario_atual = None
        self.carregar_usuarios()
    
    def carregar_usuarios(self):
        """Carrega os dados dos usuários do arquivo"""
        if os.path.exists(self.arquivo_usuarios):
            with open(self.arquivo_usuarios, 'r', encoding='utf-8') as arquivo:
                for linha in arquivo:
                    linha = linha.strip()
                    if linha:
                        partes = linha.split(',')
                        if len(partes) == 3:
                            nome, vitorias, derrotas = partes
                            self.usuarios[nome] = {
                                'vitorias': int(vitorias),
                                'derrotas': int(derrotas)
                            }
    
    def salvar_usuarios(self):
        """Salva os dados dos usuários no arquivo"""
        with open(self.arquivo_usuarios, 'w', encoding='utf-8') as arquivo:
            for nome, dados in self.usuarios.items():
                arquivo.write(f"{nome},{dados['vitorias']},{dados['derrotas']}\n")
    
    def criar_usuario(self, nome):
        """Cria um novo usuário"""
        if nome not in self.usuarios:
            self.usuarios[nome] = {'vitorias': 0, 'derrotas': 0}
            self.salvar_usuarios()
        self.usuario_atual = nome
        return self.usuarios[nome]
    
    def login(self):
        """Realiza o login do usuário"""
        print("\n" + "="*50)
        print("BEM-VINDO AO JOGO BAGELS!")
        print("="*50)
        
        while True:
            nome = input("\nDigite seu nome de usuário: ").strip()
            if nome:
                if nome in self.usuarios:
                    print(f"\nBem-vindo de volta, {nome}!")
                    self.usuario_atual = nome
                    return self.usuarios[nome]
                else:
                    print(f"\nUsuário '{nome}' não encontrado. Vou criar uma nova conta para você!")
                    return self.criar_usuario(nome)
            else:
                print("Nome de usuário inválido. Tente novamente.")
    
    def gerar_numero_secreto(self):
        """Gera um número secreto de 3 dígitos sem repetição"""
        digitos = list('0123456789')
        random.shuffle(digitos)
        # O primeiro dígito não pode ser 0
        if digitos[0] == '0':
            # Troca com outro dígito não-zero
            for i in range(1, len(digitos)):
                if digitos[i] != '0':
                    digitos[0], digitos[i] = digitos[i], digitos[0]
                    break
        return ''.join(digitos[:3])
    
    def validar_palpite(self, palpite):
        """Valida se o palpite é válido"""
        if len(palpite) != 3:
            return False, "O palpite deve ter exatamente 3 dígitos."
        
        if not palpite.isdigit():
            return False, "O palpite deve conter apenas números."
        
        # Verifica se há dígitos repetidos
        if len(set(palpite)) != 3:
            return False, "Os dígitos não podem se repetir."
        
        return True, ""
    
    def dar_dica(self, secreto, palpite):
        """Retorna as dicas Fermi/Pico/Bagels para o palpite"""
        fermi = 0  # Dígito correto na posição certa
        pico = 0   # Dígito correto na posição errada
        
        # Verifica Fermi (posição correta)
        for i in range(3):
            if palpite[i] == secreto[i]:
                fermi += 1
        
        # Verifica Pico (dígito correto, posição errada)
        for i in range(3):
            if palpite[i] != secreto[i] and palpite[i] in secreto:
                pico += 1
        
        # Monta a resposta
        if fermi == 3:
            return "VOCÊ GANHOU!"
        
        if fermi == 0 and pico == 0:
            return "Bagels"
        
        resposta = []
        for _ in range(fermi):
            resposta.append("Fermi")
        for _ in range(pico):
            resposta.append("Pico")
        
        return " ".join(resposta)
    
    def exibir_instrucoes(self):
        """Exibe as instruções do jogo"""
        print("\n" + "="*60)
        print("INSTRUÇÕES DO JOGO BAGELS")
        print("="*60)
        print("""
O jogo gerou um número secreto de 3 dígitos (sem repetição).
Seu objetivo é adivinhar esse número em no máximo 10 tentativas.

A cada palpite, você receberá uma das seguintes dicas:
• FERMI: Um dígito está correto e na posição certa
• PICO: Um dígito está correto, mas na posição errada  
• BAGELS: Nenhum dígito está correto

Exemplo:
Se o número secreto é 427 e você chuta 123:
- O dígito 2 está correto mas na posição errada → "Pico"
- Os dígitos 1 e 3 não estão no número → não geram dicas
- Resultado: "Pico"

Boa sorte!
        """)
        input("Pressione ENTER para continuar...")
    
    def jogar_partida(self):
        """Executa uma partida completa do jogo"""
        secreto = self.gerar_numero_secreto()
        tentativas = 0
        max_tentativas = 10
        
        print("\n" + "="*50)
        print(f"NOVA PARTIDA - Jogador: {self.usuario_atual}")
        print("="*50)
        print(f"Você tem {max_tentativas} tentativas para adivinhar o número de 3 dígitos.")
        print("Os dígitos não se repetem no número secreto.\n")
        
        while tentativas < max_tentativas:
            tentativas_restantes = max_tentativas - tentativas
            print(f"\nTentativa {tentativas + 1}/{max_tentativas} (Restam: {tentativas_restantes})")
            
            while True:
                palpite = input("Digite seu palpite (3 dígitos diferentes): ").strip()
                valido, mensagem = self.validar_palpite(palpite)
                if valido:
                    break
                print(f"Palpite inválido! {mensagem}")
            
            tentativas += 1
            resultado = self.dar_dica(secreto, palpite)
            
            if resultado == "VOCÊ GANHOU!":
                print(f"\n PARABÉNS! Você acertou o número {secreto} em {tentativas} tentativas! ")
                # Atualiza estatísticas
                self.usuarios[self.usuario_atual]['vitorias'] += 1
                self.salvar_usuarios()
                return True
            else:
                print(f"Dica: {resultado}")
        
        # Se chegou aqui, o jogador perdeu
        print(f"\n GAME OVER! O número secreto era {secreto}. 💀")
        self.usuarios[self.usuario_atual]['derrotas'] += 1
        self.salvar_usuarios()
        return False
    
    def exibir_ranking(self):
        """Exibe o ranking dos jogadores"""
        if not self.usuarios:
            print("\nNenhum jogador cadastrado ainda!")
            return
        
        print("\n" + "="*60)
        print(" RANKING DOS JOGADORES ")
        print("="*60)
        
        # Cria lista de tuplas (nome, vitorias, derrotas, total_jogos)
        ranking = []
        for nome, dados in self.usuarios.items():
            total_jogos = dados['vitorias'] + dados['derrotas']
            if total_jogos > 0:
                taxa_vitoria = (dados['vitorias'] / total_jogos) * 100
            else:
                taxa_vitoria = 0
            ranking.append((nome, dados['vitorias'], dados['derrotas'], total_jogos, taxa_vitoria))
        
        # Ordena por vitórias (decrescente)
        ranking.sort(key=lambda x: x[1], reverse=True)
        
        print(f"\n{'Pos':<4} {'Jogador':<15} {'Vitórias':<10} {'Derrotas':<10} {'Total':<8} {'% Vitória':<10}")
        print("-" * 60)
        
        for i, (nome, vitorias, derrotas, total, taxa) in enumerate(ranking, 1):
            print(f"{i:<4} {nome:<15} {vitorias:<10} {derrotas:<10} {total:<8} {taxa:.1f}%")
        
        # Exibe estatísticas do jogador atual se existir
        if self.usuario_atual:
            dados_atual = self.usuarios[self.usuario_atual]
            total_atual = dados_atual['vitorias'] + dados_atual['derrotas']
            if total_atual > 0:
                print(f"\n SUAS ESTATÍSTICAS:")
                print(f"   Vitórias: {dados_atual['vitorias']}")
                print(f"   Derrotas: {dados_atual['derrotas']}")
                print(f"   Total de jogos: {total_atual}")
                print(f"   Taxa de vitória: {(dados_atual['vitorias']/total_atual)*100:.1f}%")
            else:
                print(f"\n Você ainda não jogou nenhuma partida!")
        
        print("\n" + "="*60)
        input("Pressione ENTER para continuar...")
    
    def menu_principal(self):
        """Exibe o menu principal do jogo"""
        # Login do usuário
        self.login()
        
        while True:
            print("\n" + "="*50)
            print(f"MENU PRINCIPAL - Jogador: {self.usuario_atual}")
            print("="*50)
            print("1.  Iniciar nova partida")
            print("2.  Ver ranking")
            print("3.  Ver instruções")
            print("4.  Trocar usuário")
            print("5.  Sair do jogo")
            print("-"*50)
            
            opcao = input("Escolha uma opção (1-5): ").strip()
            
            if opcao == "1":
                self.jogar_partida()
            elif opcao == "2":
                self.exibir_ranking()
            elif opcao == "3":
                self.exibir_instrucoes()
            elif opcao == "4":
                self.login()
            elif opcao == "5":
                print(f"\nAté logo, {self.usuario_atual}! Obrigado por jogar Bagels!")
                break
            else:
                print("\n Opção inválida! Escolha uma opção entre 1 e 5.")

# Execução principal
if __name__ == "__main__":
    jogo = JogoBagels()
    jogo.menu_principal()
