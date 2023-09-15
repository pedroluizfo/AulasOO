import pygame
import sys
pygame.init()


largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Universo Interativo")

branco = (255, 255, 255)
preto = (0, 0, 0)

class Retangulo:
    def __init__(self, x, y, largura, altura):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura

    def desenhar(self):
        pygame.draw.rect(tela, preto, (self.x, self.y, self.largura, self.altura))

    def calcular_area(self):
        return self.largura * self.altura

class Circulo:
    def __init__(self, x, y, raio):
        self.x = x
        self.y = y
        self.raio = raio

    def desenhar(self):
        pygame.draw.circle(tela, preto, (self.x, self.y), self.raio)

    def calcular_area(self):
        return 3.14 * self.raio * self.raio

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    tela.fill(branco)

    retangulo = Retangulo(100, 100, 200, 100)
    retangulo.desenhar()

    circulo = Circulo(400, 300, 50)
    circulo.desenhar()

    pygame.display.update()
