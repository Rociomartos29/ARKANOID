import pygame as pg
from arkanoid.entidades import Pelota, Raqueta
raqueta = Raqueta
pelota = Pelota


pantalla = pg.display.set_mode((1000, 1000))
salir = False
raqueta.rect.left = 70
pelota.rect.left = 0
raqueta.rect.y = 50
pelota.rect.y = 50
while not salir: 
    for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    salir = True
    pantalla.fill((0, 99, 0))
    teclas = pg.key.get_pressed()
    if teclas[pg.K_LEFT]:
        raqueta.rect.x -= 5
    if teclas[pg.K_RIGHT]:
        raqueta.rect.x += 5
        pantalla.blit(raqueta.image, raqueta.rect)
        pelota.blit(pelota.image, pelota.rect)
    pg.display.flip()