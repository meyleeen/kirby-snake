"""
Pantalla de menú principal:
Muestra botones Start y Close (salir).
Al pulsar Start devuelve states.GAME (el main debe crear la nueva Game).
Al pulsar Close devuelve None para indicar que se debe cerrar la aplicación.
"""


import pygame
from button import Button
import states
import config


class Menu:
    def __init__(self, ancho, alto):

        #Creación de botones.
        self.start_button = Button(pygame.image.load("Assets/button/start_button.png").convert_alpha(),pos = (400, 300), scale = 0.1)
        self.close_button = Button(pygame.image.load("Assets/button/close_button.png").convert_alpha(),pos = (400, 400), scale = 0.1) 


    def handle_event(self, event):

        if self.start_button.event_mouse(event):
            return states.GAME
        
        if self.close_button.event_mouse(event):
            return None
        
        return states.MENU
    
    def draw(self, surface):

        surface.fill(config.CELESTE)
        self.start_button.draw(surface)
        self.close_button.draw(surface)

        font = pygame.font.SysFont(None, 20)
        text = font.render("by meyleeen", True, (0, 0, 0))
        surface.blit(text, (50, 550))