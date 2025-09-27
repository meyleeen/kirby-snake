import pygame
import states
from menu import Menu
from game import Game

pygame.init()

#configuración de la ventana
ancho = 800
alto = 600
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("snake")
clock = pygame.time.Clock()

#configuración de la pantalla
menu = Menu(ancho, alto)
game = Game(ancho, alto)

estado = states.MENU
running = True


#bucle principal
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if estado == states.MENU:
            nuevo_estado = menu.handle_event(event)

            if nuevo_estado is None:
                running = False
            
            else: 
                estado = nuevo_estado
        
        elif estado == states.GAME:
            estado = game.handle_event(event)

        
    #lógica del juego
    if estado == states.GAME:
        game.update()


    #dibujar en pantalla
    if estado == states.MENU:
        menu.draw(ventana)
    
    if estado == states.GAME:
        game.draw(ventana)


    pygame.display.update()
    clock.tick(6)