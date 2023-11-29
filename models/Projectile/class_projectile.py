import pygame
from models.constantes import ANCHO_VENTANA
from models.Items.class_item import Item

class Projectile(Item):
    def __init__(self, surface: pygame.Surface, initial_position: tuple, actions: dict, rect_diference: int, size: tuple):
        super().__init__(surface, initial_position, actions, 0, size)
        self.speed = 0

    def check_collide_platform(self,platform_list,projectile_list,enemy_list):
        rect_list = []
        for platform in platform_list:
            rect_list.append(platform.colliders["main"])

        for enemy in enemy_list:
            rect_list.append(enemy.colliders["main"])

        for rect in rect_list:
            if self.colliders["main"].colliderect(rect):
                self.kill(projectile_list)

    def update(self, screen,platform_list,projectile_list,enemy_list):
        self.rect.x += self.speed
        self.check_collide_platform(platform_list,projectile_list,enemy_list)

        if self.rect.x > ANCHO_VENTANA or self.rect.x < 0:
            self.set_colition(True)
        super().update(screen)

