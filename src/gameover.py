import pygame
import states
from button import Button
import config

class GameOver:
    def __init__(self, ancho, alto):
        # Cargar sprites de botones
        retry_img = pygame.image.load("Assets/button/retry_button.png").convert_alpha()
        menu_img = pygame.image.load("Assets/button/menu_button.png").convert_alpha()

        # Crear botones centrados
        self.retry_button = Button(retry_img, pos=(ancho // 2, alto // 2 + 100), scale=0.15)
        self.menu_button = Button(menu_img, pos=(ancho // 2, alto // 2 + 200), scale=0.15)

    def handle_event(self, event):
        #Maneja los clics en los botones.
        if self.retry_button.event_mouse(event):
            return states.GAME  # volver al juego (nueva partida)
        if self.menu_button.event_mouse(event):
            return states.MENU  # volver al menú principal
        return states.GAME_OVER

    def draw(self, surface, score):
        #Dibuja la pantalla de Game Over con la puntuación.
        surface.fill(config.CELESTE)

        # Título.
        font_big = pygame.font.SysFont(None, 80)
        text = font_big.render("GAME OVER", True, config.NEGRO)
        surface.blit(text, (surface.get_width() // 2 - text.get_width() // 2, 150))

        # Mostrar puntuación final.
        font_small = pygame.font.SysFont(None, 50)
        score_text = font_small.render(f"Puntos: {score}", True, config.NEGRO)
        surface.blit(score_text, (surface.get_width() // 2 - score_text.get_width() // 2, 250))

        # Dibujar botones.
        self.retry_button.draw(surface)
        self.menu_button.draw(surface)