import pygame
import states
from menu import Menu
from game import Game
import config
from gameover import GameOver

pygame.init()

#Configuración de la ventana.
ventana = pygame.display.set_mode((config.ANCHO, config.ALTO))
pygame.display.set_caption("Kirby Snake")
clock = pygame.time.Clock()

#Configuración de la pantalla.
menu = Menu(config.ANCHO, config.ALTO)
game = Game(config.ANCHO, config.ALTO)
game_over = GameOver(config.ANCHO, config.ALTO)

estado = states.MENU
running = True

#Bucle principal.
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

        elif estado == states.GAME_OVER:
            estado = game_over.handle_event(event)
            if estado == states.GAME:
                #Reiniciar la partida si se elige reiniciar.
                game = Game(config.ANCHO, config.ALTO)


        
    #Lógica del juego.
    if estado == states.GAME:
        game.update()

    #Dibujar en pantalla.
    if estado == states.MENU:
        menu.draw(ventana)
    
    if estado == states.GAME:
        game.draw(ventana)

    if estado == states.GAME_OVER:
        game_over.draw(ventana, game.score)


    pygame.display.update()
    clock.tick(config.VELOCIDAD)

pygame.quit()