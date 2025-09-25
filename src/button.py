import pygame

#constructor de botones 
class Button:
    def __init__(self, image, pos, scale = 1):

        self.original_image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))

        self.image = self.original_image

        #versión más pequeña para el click
        self.pressed_image = pygame.transform.scale(self.original_image, (int(self.original_image.get_width() * 0.9), int(self.original_image.get_height() * 0.9)))

        self.rect = self.image.get_rect(center = pos)

        self.pressed = False

    #dibujar botón
    def draw(self, surface):
        surface.blit(self.image, self.rect) 
    
    def is_hovered(self):
        return self.rect.collidepoint(pygame.mouse.get_pos()) #devuelve True si el mouse está sobre el botón
    
    #manejo de los eventos del mouse 
    def event_mouse(self, event):


        #cuando se presiona el botón del mouse
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.is_hovered():
                self.pressed = True

                #animación botón
                self.image = self.pressed_image
                self.rect = self.image.get_rect(center = self.rect.center)


        #cuando se suelta el botón del mouse
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.pressed:
                self.pressed = False

                #animación botón
                self.image = self.original_image 
                self.rect = self.image.get_rect(center = self.rect.center)

            if self.is_hovered():
                return True
        
        return False