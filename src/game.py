"""
Clase Game que encapsula el estado y lógica de una partida:
Inicializa Snake y Food.
Mantiene score (puntos).
Calcula offsets para centrar la ZONA_DE_JUEGO en la ventana.
handle_event: procesa teclas (direcciones, ESC -> menú).
update: lógica por frame (comer, mover, comprobar colisiones).
draw: dibuja fondo, borde del área jugable, comida, serpiente y marcador.
"""

import pygame 
import states
import config
from snake import Snake
from food import Food
import collisions

class Game:
    def __init__(self, ancho, alto):
        #Crear kirby y estrella.
        self.snake = Snake()
        self.food = Food()
        self.score = 0 #Puntos del jugador.

        #Margenes para calcular la zona jugable.
        self.offset_x = (ancho - config.ZONA_DE_JUEGO)// 2
        self.offset_y = (alto - config.ZONA_DE_JUEGO)// 2


    def handle_event(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.snake.cambiar_direccion((0, -1))

            elif event.key == pygame.K_DOWN:
                self.snake.cambiar_direccion((0, 1))

            elif event.key == pygame.K_LEFT:
                self.snake.cambiar_direccion((-1, 0))

            elif event.key == pygame.K_RIGHT:
                self.snake.cambiar_direccion((1, 0))        

            elif event.key == pygame.K_ESCAPE:
                return states.MENU
              
        return states.GAME
    
    def update(self):
        #Actualiza la lógica del juego.
        grow = False

        #Si kirby come una estrella, crece y suma puntos, se añade nueva estrella en el mapa.
        if collisions.check_food_collision(self.snake, self.food):
            grow = True 
            self.score += 1
            self.food.randomize()
        
        #Mover kirby. 
        self.snake.move(grow)

        #Comprobar colisiones.
        if collisions.check_self_collision(self.snake) or collisions.check_wall_collision(self.snake):
            return states.GAME_OVER
        
        return states.GAME

    def draw(self, surface):
        surface.fill(config.ROSA)

        #Dibujar el borde del área jugable.
        pygame.draw.rect(surface, config.NEGRO, (self.offset_x, self.offset_y, config.ZONA_DE_JUEGO, config.ZONA_DE_JUEGO), 3)

        #Dibujar comida kirby.
        self.food.draw(surface, self.offset_x, self.offset_y)
        self.snake.draw(surface, self.offset_x, self.offset_y)

        #Dibujar el marcador.
        font = pygame.font.SysFont(None, 40)
        text = font.render(f"Score: {self.score}", True, config.NEGRO)
        surface.blit(text,(10, 10))
