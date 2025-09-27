import pygame
import random
import config

class Food:
    def __init__(self):
        #sprite de la estrella
        self.image = pygame.image.load(config.ESTRELLA).convert_alpha()
        self.image = pygame.transform.scale(self.image, (config.TAMAÑO_CELDAS, config.TAMAÑO_CELDAS))

        #estrella incial
        self.posicion = (0, 0)
        self.randomize()
    
    def randomize(self):
        max_celda = config.ZONA_DE_JUEGO//config.TAMAÑO_CELDAS
        x = random.randint(0, max_celda -1)
        y = random.randint(0, max_celda -1)
        self.posicion = (x, y)

    def draw(self, surface, offset_x, offset_y):
        x, y = self.posicion
        px = offset_x + x * config.TAMAÑO_CELDAS
        py = offset_y + y * config.TAMAÑO_CELDAS
        surface.blit(self.image, (px, py))