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

palavra = random.choice(palavras)
letras_adivinhadas = []
tentativas = 6
pontos = 0

fonte = pygame.font.SysFont(None, 30)

mensagens_intro = [
    "Olá, jogador! Você está em um mundo antigo.",
    "Você é um escravo grego capturado por persas.",
    "Participe do jogo da forca e não deixe que descubram seu sotaque."
]

tela.fill(branco)
for i, mensagem in enumerate(mensagens_intro):
    texto_intro = fonte.render(mensagem, True, preto)
    tela.blit(texto_intro, (50, altura // 2 - 100 + i * 50))  # Espaçamento ajustado
pygame.display.flip()

pygame.time.wait(10000)

def mostrar_palavra():
    exibicao = ''
    for letra in palavra:
        if letra in letras_adivinhadas:
            exibicao += letra + ' '
        else:
            exibicao += '_ '
    return exibicao.strip()

executando = True
while executando:
    tela.fill(branco)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
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
        executando = False
    elif tentativas <= 0:
        mensagem = f"Você perdeu! A palavra era: {palavra}. Pontuação: {pontos}"
        executando = False

    if pontos >= 100 and tentativas == 6:
        mensagem_aviso = "Os persas perceberam você..."
        texto_aviso = fonte.render(mensagem_aviso, True, preto)
        tela.blit(texto_aviso, (50, altura // 2 - 50))
        tentativas = 3
    elif pontos >= 75:
        mensagem_aviso = "Eles estão desconfiados..."
        texto_aviso = fonte.render(mensagem_aviso, True, preto)
        tela.blit(texto_aviso, (50, altura // 2 - 50))
    elif pontos >= 50:
        mensagem_aviso = "Eles ainda não confiam em você."
        texto_aviso = fonte.render(mensagem_aviso, True, preto)
        tela.blit(texto_aviso, (50, altura // 2 - 50))
    elif pontos >= 25:
        mensagem_aviso = "Eles acham você estranho..."
        texto_aviso = fonte.render(mensagem_aviso, True, preto)
        tela.blit(texto_aviso, (50, altura // 2 - 50))

    texto_palavra = fonte.render(mostrar_palavra(), True, preto)
    tela.blit(texto_palavra, (50, altura // 2))

    pygame.display.flip()
    pygame.time.delay(100)

if 'mensagem' in locals():
    texto_final = fonte.render(mensagem, True, preto)
    tela.fill(branco)
    tela.blit(texto_final, (50, altura // 2))
    pygame.display.flip()
    pygame.time.wait(3000)

pygame.quit()