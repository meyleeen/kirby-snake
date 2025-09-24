import pygame
from button import button

pygame.init()

#configuración de la ventana
ancho = 800
alto = 600
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("snake")
clock = pygame.time.Clock()

#colores
celeste = (135, 206, 235)

#creación de botones
start_button = button(pygame.image.load("Assets/button/start_button.png").convert_alpha(),pos = (400, 300), scale = 0.1)
close_button = button(pygame.image.load("Assets/button/close_button.png").convert_alpha(),pos = (400, 400), scale = 0.1) 

#bucle principal
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if start_button.event_mouse(event):
            print("botón presionado")
        if close_button.event_mouse(event):
            pygame.quit()

    #lógica del juego

    #dibujar en pantalla
    ventana.fill(celeste)
    start_button.draw(ventana)
    close_button.draw(ventana)

    pygame.display.update()
    clock.tick(60)