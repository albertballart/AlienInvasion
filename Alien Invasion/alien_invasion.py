import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import  Alien

class AlienInvasion:
    """Clase general para administrar los activos y el comportamiento del juego."""
    def __init__(self):
        """Inicialice el juego y cree recursos."""
        self.exp = None
        self.all_sprites = None
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Inicie el ciclo principal del juego."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()

    def _check_events(self):
        """Responde a pulsaciones de teclads y eventos de ratón"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Responde a las pulsaciones de teclas"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Responde a liberaciones de teclas"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Crea una bala nueva y la añade al grupo de balas"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Actualiza la posición de las balas y se deshace de las viejas"""
        # Actuliza las posiciones de las balas
        self.bullets.update()
        self.explosions = pygame.sprite.Group()

        # Se deshace de las balas que han desaparecido
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        print(len(self.bullets))

        # Busca balas que hayan dado a liens
        # Si hay, se deshace de la bala y del alien
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        for alien in collisions.values():
            center = alien[0].rect.center

        if not self.aliens:
            # Destruye las balas existentes y crea una flota nueva
            self.bullets.empty()
            self._create_fleet()


    def _update_aliens(self):
        """Comprueba si la flota está en un borde,
        después actualiza las posiciones de todos los aliens de la flota"""
        self._check_fleet_edges()
        self.aliens.update()

    def _create_fleet(self):
        """Crea la flota de aliens"""
        # Crea un alien y halla el número de aliens en una fila
        # El espacio entre aliens es igual a la anchura de un alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Determina el número de filas de aliens que caben en la pantalla
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Crea la flota completa de aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _check_fleet_edges(self):
        """Responde adecuadamente si algún alien ha llegado a un borde"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Baja toda la flota y cambia su dirección"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _create_alien(self, alien_number, row_number):
        # Crea un alien y lo coloca en la fila
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)


    def _update_screen(self):
        """Actualiza las imágenes en la pantalla y cambia a la pantalla nueva"""
        # Vuelva a dibujar la pantalla durante cada pasada por el bucle.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        # Haga visible la pantalla dibujada más recientemente.
        pygame.display.flip()


if __name__ == '__main__':
    # Cree una instancia de juego y ejecútelo.
    ai = AlienInvasion()
    ai.run_game()
