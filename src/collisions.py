"""Funciones puras para comprobar colisiones lógicas en el juego (no dibujo).
check_self_collision(snake): True si la cabeza coincide con cualquier segmento del cuerpo.
check_wall_collision(snake): True si la cabeza sale del área jugable (en coordenadas de celdas).
check_food_collision(snake, food): True si la cabeza está en la misma celda que la comida.
"""

import config

def check_self_collision(snake):
    #Devuelve True si kirby toca cualquier parte del cuerpo.
    head = snake.get_kirby()
    return head in snake.cuerpo[1:]

def check_wall_collision(snake):
    #Devuelve True si la cabeza está fuera de los límites de la zona jugable.
    x, y = snake.get_kirby()
    max_celda = config.ZONA_DE_JUEGO//config.TAMAÑO_CELDAS # número de celdas en la zona jugable
    return x < 0 or y < 0 or x >= max_celda or y >= max_celda

def check_food_collision(snake, food):
    #Devuelve True si la cabeza está en la misma posición que la comida.
    return snake.get_kirby() == food.posicion