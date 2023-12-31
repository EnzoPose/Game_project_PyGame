from models.object_game.Class_object import Object
from models.Projectile.class_projectile import Projectile
from models.platform.class_patform import Platform
from auxiliar.configuraciones import resize_images
import pygame as pg

class Charapter(Object):

    def __init__(self, surface:pg.surface, initial_position: list ,animations:dict,rect_diference:int,size:list,life:int,damage:int):
        super().__init__(surface,initial_position,animations,rect_diference, size)
        
        self.life = life
        self.damage = damage
        ##Movement 
        self.speed_x = 0

        self.gravity = 1
        self.jump_power = -20
        self.drop_speed_limit = 20
        self.displacement_y = 0
        self.is_jumping = False

        ##Attack
        self.is_shooting = False
        self.projectile_list:list[Projectile] = []
        self.cadence = 200


        self.is_loking_right = True
        self.right_limit = False
        self.left_limit = False
        self.animations = animations
        self.resize_animations()

        self.colliders_thickness = rect_diference

        self.projectile_collide_sound = pg.mixer.Sound("assets\img\Sounds\lasser_collide.mp3")

    
    def resize_animations(self):
        for key in self.animations: ## por cada key en el diccionario de animations del objeto
            resize_images(self.animations[key],self.width,self.height)## llamo a la función de reescalar imagen


    def gravity_fall(self):
        if self.is_jumping:
            self.jump()
            if self.displacement_y + self.gravity < self.drop_speed_limit:
                self.displacement_y += self.gravity

    def jump(self):
        for side in self.colliders:
            self.colliders[side].y += self.displacement_y



    def move_x(self):
        super().move_x(self.speed_x)



    def create_projectile(self,image_path,size):
        surface = pg.transform.scale(pg.image.load(image_path),size)
        if self.is_loking_right:
            projectile = Projectile(surface,(self.rect.right, self.rect.centery - 20),None,0,size,self.damage)
            projectile.speed = 20
        else:
            surface = pg.transform.flip(surface,True,False)
            projectile = Projectile(surface,(self.rect.left, self.rect.centery - 20),None,0,size,self.damage)
            projectile.speed = -20
        self.projectile_list.append(projectile)


    def update_projectiles(self,screen,platform_list,enemy_list):
        for projectile in self.projectile_list:
            projectile.update(screen,platform_list,self.projectile_list,enemy_list)
            if projectile.colition:
                self.projectile_collide_sound.play()
                projectile.kill(self.projectile_list)



    def update(self,screen,platform_list,enemy_list):
        super().update(screen)
        self.update_projectiles(screen,platform_list,enemy_list)


