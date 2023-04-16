import pygame
 
class Ship:
    """Una clase para manejar la nave."""

    def __init__(self, ai_game):
        """Inicializa la nave y establece su posición inicial."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Cargue la imagen del barco y obtenga su rect.
        self.image = pygame.image.load('images/nave_yes.png')
        self.rect = self.image.get_rect()

        # Inicia cada nave nueva en el centro de la parte inferior de la pantalla.
        self.rect.midbottom = self.screen_rect.midbottom

        # Guarda un valor decimal para cada posición horizontal de la nave
        self.x = float(self.rect.x)

        # Bandera de movimiento.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Actualiza la posición de la nave en función de la bandera de movimiento"""
        # Actualiza el valor de x de la nave, no el rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Actualiza el objeto rect de self.x.
        self.rect.x = self.x

    def blitme(self):
        """Dibuja el barco en su ubicación actual."""
        self.screen.blit(self.image, self.rect)
