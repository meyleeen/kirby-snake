"""
food.py
-------
Clase Food que representa la "comida" (estrella) en el juego.

-Cargar el sprite de la estrella y escalarlo al tamaño de celda.
-Mantener posicion en coordenadas de grilla (x,y) de 0..max_celda-1.
-Generar una nueva posición aleatoria con randomize().
-Dibujar la estrella en pantalla con la conversión de
coordenadas de grilla -> pixeles (usando offset_x/offset_y).
"""


import pygame
import random
import config

class Food:
    def __init__(self):
        #Sprite de la estrella.
        self.image = pygame.image.load(config.ESTRELLA).convert_alpha()
        self.image = pygame.transform.scale(self.image, (config.TAMAÑO_CELDAS, config.TAMAÑO_CELDAS))

        #Estrella incial.
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