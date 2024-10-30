import pygame
import random

pygame.init()

largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Forca")

branco = (255, 255, 255)
preto = (0, 0, 0)

palavras = [
    'abacaxi', 'abacate', 'amarelo', 'amor', 'aviao', 'artista', 'alface', 'avó', 'água', 'ato',
    'bola', 'batata', 'barco', 'banco', 'bicho', 'banda', 'bater', 'bico', 'bela',
    'cachorro', 'carro', 'cama', 'carta', 'cachoeira', 'caneta', 'cabelo', 'cesta', 'casa', 'coração',
    'dado', 'dólar', 'dente', 'doce', 'dó', 'dificil', 'dama', 'dona', 'desenho', 'divertido',
    'elefante', 'estrela', 'escola', 'eleição', 'esmalte', 'estrada', 'extensão', 'espinho', 'esquilo', 'escova',
    'fogo', 'faca', 'festa', 'fruta', 'futebol', 'foto', 'feliz', 'fumaça', 'filme', 'férias',
    'gato', 'galo', 'guitarra', 'gol', 'grande', 'girafa', 'galinha', 'guerra', 'garagem',
    'horario', 'hotel', 'harpa', 'hospedeiro', 'hipopótamo', 'humor', 'hiena', 'historia', 'hobby',
    'jacare', 'janela', 'jogo', 'jardim', 'jato', 'joia', 'japonês', 'joão',
    'kiwi', 'ketchup', 'karate', 'kilo', 'kit', 'kiosk', 'krypton',
    'leão', 'lago', 'luz', 'lápis', 'livro', 'lobo', 'lata', 'limão', 'lanterna', 'lavabo',
    'macaco', 'mesa', 'maçã', 'manga', 'música', 'moeda', 'motor', 'mole', 'mãe', 'mão',
    'navio', 'noite', 'nuvem', 'nariz', 'ninho', 'noiva', 'nome', 'número', 'natureza', 'notícia',
    'ocelo', 'outono', 'olho', 'ouro', 'obra', 'orégano', 'ocidente', 'oasis', 'oficina', 'ombro',
    'pato', 'piano', 'paz', 'peixe', 'papel', 'pão', 'patinha', 'pimenta', 'palco', 'palavra',
    'quadro', 'queijo', 'quente', 'quarto', 'qualidade', 'quimica', 'quimono', 'queimar', 'quero', 'quasar',
    'rato', 'rosa', 'roda', 'rua', 'raiz', 'roxo', 'rapaz', 'relógio', 'ratoeira',
    'sapo', 'sorvete', 'sorriso', 'salada', 'sal', 'sonho', 'sombra', 'semente', 'serpente',
    'tigre', 'taco', 'tinta', 'tela', 'tambor', 'tampa', 'torrada', 'torta', 'trevo', 'túnel',
    'urso', 'uva', 'unha', 'umbigo', 'urgente', 'uniforme', 'utilidade', 'universo', 'utopia',
    'vaca', 'você', 'viagem', 'ventilador', 'voo', 'vinho', 'vulcão', 'voto', 'verão', 'velho',
    'zebra', 'zangado', 'zumbido', 'zangão', 'zoo', 'zap', 'zine', 'zodíaco', 'zorro', 'zeus'
]

def desenhar_boneco(tentativas):
    if tentativas <= 5:
        pygame.draw.circle(tela, preto, (400, 200), 20)
    if tentativas <= 4:
        pygame.draw.line(tela, preto, (400, 220), (400, 320), 5)
    if tentativas <= 3:
        pygame.draw.line(tela, preto, (400, 240), (360, 280), 5)
    if tentativas <= 2:
        pygame.draw.line(tela, preto, (400, 240), (440, 280), 5)
    if tentativas <= 1:
        pygame.draw.line(tela, preto, (400, 320), (360, 360), 5)
    if tentativas <= 0:
        pygame.draw.line(tela, preto, (400, 320), (440, 360), 5) 

def mostrar_palavra(palavra, letras_adivinhadas):
    exibicao = ''
    for letra in palavra:
        if letra in letras_adivinhadas:
            exibicao += letra + ' '
        else:
            exibicao += '_ '
    return exibicao.strip()

fonte = pygame.font.SysFont(None, 30)

executando = True
while executando:
    palavra = random.choice(palavras)
    letras_adivinhadas = []
    tentativas = 6
    pontos = 0

    tela.fill(branco)
    mensagens_intro = [
        "Olá, jogador! Você está em um mundo antigo.",
        "Você é um escravo grego capturado por persas.",
        "Participe do jogo da forca e não deixe que descubram seu sotaque."
    ]
    for i, mensagem in enumerate(mensagens_intro):
        texto_intro = fonte.render(mensagem, True, preto)
        tela.blit(texto_intro, (50, altura // 2 - 100 + i * 50))
    pygame.display.flip()
    pygame.time.wait(10000)

    while True:
        tela.fill(branco)
        desenhar_boneco(tentativas)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False
                break
            elif evento.type == pygame.KEYDOWN:
                if evento.unicode.isalpha() and len(evento.unicode) == 1:
                    letra = evento.unicode.lower()
                    if letra not in letras_adivinhadas:
                        letras_adivinhadas.append(letra)
                        if letra not in palavra:
                            tentativas -= 1
                            if pontos >= 100:
                                tentativas -= 1
                        else:
                            pontos += 1

        if set(palavra) <= set(letras_adivinhadas):
            pontos += 5
            mensagem = f"Você ganhou! Pontuação: {pontos}"
            break
        elif tentativas <= 0:
            mensagem = f"Você perdeu! A palavra era: {palavra}. Pontuação: {pontos}"
            break


        if pontos >= 100 and tentativas == 6:
            mensagem_aviso = "Os persas perceberam você..."
            tentativas = 3
        elif pontos >= 75:
            mensagem_aviso = "Eles estão desconfiados..."
        elif pontos >= 50:
            mensagem_aviso = "Eles ainda não confiam em você."
        elif pontos >= 25:
            mensagem_aviso = "Eles acham você estranho..."

        if 'mensagem_aviso' in locals():
            texto_aviso = fonte.render(mensagem_aviso, True, preto)
            tela.blit(texto_aviso, (50, altura // 2 - 50))

        texto_palavra = fonte.render(mostrar_palavra(palavra, letras_adivinhadas), True, preto)
        tela.blit(texto_palavra, (50, altura // 2))

        pygame.display.flip()
        pygame.time.delay(100)

    tela.fill(branco)
    texto_final = fonte.render(mensagem, True, preto)
    tela.blit(texto_final, (50, altura // 2))
    pygame.display.flip()
    pygame.time.wait(3000)


    if pontos >= 150:
        executando = False

pygame.quit()
