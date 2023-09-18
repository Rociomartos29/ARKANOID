import os
import random
from typing import Any
import pygame as pg
from . import Ancho, Alto, VEL_MAX, VEL_MIN_Y

margen = 25
velocidad = 5


class Raqueta(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.imagenes = []
        margen = 25
        velocidad = 5
        for i in range(3):
            ruta_image = os.path.join('resources', 'images', f'electric0{i}.png')
            self.imagenes.append(pg.image.load(ruta_image))
        self.contador = 0
        self.image = self.imagenes[self.contador]

        self.rect = self.image.get_rect(
            midbottom=(Ancho/2, Alto - margen))

    def update(self):
        self.contador += 1
        if self.contador > 2:
            self.contador = 0
        self.comprobar_teclas()
        self.image = self.imagenes[self.contador]

    def mover(self):
        pass

    def pintar(self):
        pass

    def reset(self):
        pass

    def comprobar_teclas(self):
        teclas = pg.key.get_pressed()
        if teclas[pg.K_LEFT]:
            self.rect.x -= velocidad
        if teclas[pg.K_RIGHT]:
            self.rect.x += velocidad

class Ladrillo(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()
        ruta_verde = os.path.join('resources', 'images', 'greenTile.png')
        self.image = pg.image.load(ruta_verde)
        self.rect = self.image.get_rect()

    def update():
        pass
    
class Pelota(pg.sprite.Sprite):

    vel_x = -10
    vel_y = -13

    def __init__(self, raqueta):
        super().__init__()
        self.image = pg.image.load(os.path.join('resources', 'images', 'ball1.png'))
        self.rect = self.image.get_rect(midbottom=raqueta.rect.midtop)
        self.raqueta = raqueta

    def inicializar_velocidades(self):
        self.vel_x = random.randint(-VEL_MAX, VEL_MAX)
        self.vel_y = random.randint(-VEL_MAX, VEL_MIN_Y)
    def update(self, partida_empezada):
        if not partida_empezada:
            self.rect = self.image.get_rect(midbottom=self.raqueta.rect.midtop)
        else:
            self.rect.x += self.vel_x
            if self.rect.left <= 0 or self.rect.right > Ancho:
                self.vel_x = -self.vel_x

            self.rect.y += self.vel_y
            if self.rect.top <= 0:
                self.vel_y = -self.vel_y

            if self.rect.top >= Alto:
                self.pierdes()
                self.reset()
            if pg.sprite.collide_mask(self, self.raqueta):
                self.inicializar_velocidades()
            

    def pierdes(self):
        print('Has perdido un punto')

    


    def reset(self):
        print('Hay que poner la pelota de nuevo en el centro de la raqueta y esperar a que se pulse el espacio para iniciar de nuevo el juego')