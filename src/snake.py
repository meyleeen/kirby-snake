import pygame
import config

class Snake:
    def __init__(self):
        #cargar sprite
        self.kirby = pygame.image.load(config.KIRBY).convert_alpha()
        self.kirby = pygame.transform.scale(self.kirby, (config.TAMAÑO_CELDAS, config.TAMAÑO_CELDAS))

        self.estrella = pygame.image.load(config.ESTRELLA).convert_alpha()
        self.estrella = pygame.transform.scale(self.estrella, (config.TAMAÑO_CELDAS, config.TAMAÑO_CELDAS))


        #posición inicial
        self.cuerpo = [(5,5)] #lista de coordenadas de kirby y las estrellas
        self.direccion = (1, 0)

    def get_kirby(self):
        return self.cuerpo[0] #devuelve la posición de kirby 
    
    def move(self,grow = False):
        x, y = self.get_kirby() #posición en la que está kirby en x / y 
        dx, dy = self.direccion #direccion en la que se mueve kirby en x / y 

        nueva_posicion = (x + dx, y + dy) #nueva posición de kirby
        self.cuerpo.insert(0, nueva_posicion)
        
        if not grow:
            self.cuerpo.pop()
    
    def cambiar_direccion(self, nueva_direccion):
        if (nueva_direccion[0] * -1, nueva_direccion[1] * -1) != self.direccion:
            self.direccion = nueva_direccion
    
    def draw (self, surface, offset_x, offset_y):
        for i, (x, y) in enumerate (self.cuerpo):
            px = offset_x + x * config.TAMAÑO_CELDAS
            py = offset_y + y * config.TAMAÑO_CELDAS

            if i == 0:
                surface.blit(self.kirby, (px, py))
            else:
                surface.blit(self.estrella, (px, py))