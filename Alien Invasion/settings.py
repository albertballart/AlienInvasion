class Settings:
    """Una clase para almacenar todos los ajustes de Alien Invasion."""

    def __init__(self):
        """Inicializar la configuración del juego."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Configuración de la nave
        self.ship_speed = 4.5

        # Configuración de las balas
        self.bullet_speed = 4.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 5

        # Configuraciones del alien
        self.alien_speed = 3.0
        self.fleet_drop_speed = 10
        # fleet_direction de 1 representa derecha; -1 representa izquierda
        self.fleet_direction = 1

