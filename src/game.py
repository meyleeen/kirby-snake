import pygame 
import states

class Game:
    def __init__(self, alto, ancho):
        
        self.rosa = (255, 192, 203)

    def handle_event(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return states.MENU
            
        return states.GAME
    
    def update(self):
        pass

    def draw(self, surface):
        surface.fill(self.rosa)