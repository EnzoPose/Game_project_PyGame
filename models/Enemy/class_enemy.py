import pygame as pg
from models.charapter.charapter import Charapter
from models.platform.class_patform import Platform
from models.constantes import ANCHO_VENTANA

class Enemy(Charapter):
    def __init__(self, surface: pg.surface, initial_position: tuple, animations: dict, rect_diference: int, size: int):
        super().__init__(surface, initial_position, animations, rect_diference, size)
        
        self.is_doing = "walk"
        self.my_floor = None
        self.is_jumping = True


    def check_collition_platform(self,platform_list:list[Platform]):
        self.gravity_fall()
        for platform in platform_list:
            if self.colliders["right"].colliderect(platform.colliders["left"]) or self.colliders["main"].right >= ANCHO_VENTANA \
            or self.colliders["right"].colliderect(platform.rect_for_collide_enemy_r):
                
                self.is_doing = "walk_l"
            elif self.colliders["left"].colliderect(platform.colliders["right"]) or self.colliders["main"].left <= 0 \
                or self.colliders["left"].colliderect(platform.rect_for_collide_enemy_l):
                self.is_doing = "walk"


    def obtain_floor(self,platform_list:list[Platform]):
        if self.my_floor == None:
            for platform in platform_list:
                if self.colliders["bottom"].colliderect(platform.colliders["top"]):
                    self.my_floor = platform
                    break

    def check_limit_platform(self):
        if self.colliders["main"].right >= self.my_floor["main"].right:
            self.is_doing = "walk_l"
        elif self.colliders["main"].left <= self.my_floor["main"].left:
            self.is_doing = "walk"

    def event_management(self):
        match self.is_doing:
            case "walk":
                self.speed_x = 5
                self.move_x()
                self.animate(self.animations["walk"])
            case "walk_l":
                self.speed_x = -5
                self.move_x()
                self.animate(self.animations["walk_l"])


    def verify_pathing(self,platform_list):
        pass

    
    def update(self,screen,platform_list,enemy_list):
        self.gravity_fall()
        self.event_management()
        self.check_collition_platform(platform_list)
        super().verify_colission_platforms(platform_list)
        super().update(screen,platform_list,enemy_list)