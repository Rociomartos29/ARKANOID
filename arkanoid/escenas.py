import os
import pygame as pg
from . import Alto, Ancho, FPS, VIDAS, ALTO_MARCADOR
from .entidades import Raqueta, Ladrillo, Pelota, ContadorVidas, Marcador


class Escena:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.reloj = pg.time.Clock()

    def bucle_principal(self):
        '''
        Este metodo debe ser implementado por todas y cada una de las escenas, 
        en funcion de lo que esten esperando hasta la condicion de salida.
        '''
        print('Esto es un metodo vacio')


class Portada(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        ruta = os.path.join('resources',
                            'images', 'arkanoid_name.png')
        self.logo = pg.image.load(ruta)

        ruta_font = os.path.join('resources',
                                 'fonts', 'CabinSketch-Bold.ttf')
        self.tipo = pg.font.Font(ruta_font, 35)

    def bucle_principal(self):
        super().bucle_principal()
        salir = False
        while not salir:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    salir = True
                if evento.type == pg.KEYDOWN and evento.key == pg.K_SPACE:
                    salir = True

            self.pantalla.fill((99, 0, 0))
            self.pintar_logo()
            self.pintar_mensaje()

            # self.comprobar_teclas()
            pg.display.flip()

    def pintar_logo(self):
        ancho, alto = self.logo.get_size()
        pos_x = (Ancho - ancho) / 2
        pos_y = (Alto - alto)/2
        self.pantalla.blit(self.logo, (pos_x, pos_y))

    def pintar_mensaje(self):
        mensaje = 'Pulsa <Espacio> para comenzar'
        texto = self.tipo.render(mensaje, True, (255, 255, 255))
        pos_x = (Ancho - texto.get_width())/2
        pos_y = Alto / 4 * 3
        self.pantalla.blit(texto, (pos_x, pos_y))


class Partida(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        ruta_fondo = os.path.join('resources', 'images', 'background.jpg')
        self.fondo = pg.image.load(ruta_fondo)
        self.jugador = Raqueta()
        self.muro = pg.sprite.Group()
        self.pelota = Pelota(self.jugador)
        self.contador_vidas = ContadorVidas(VIDAS)
        self.marcador= Marcador()

    def bucle_principal(self):
        super().bucle_principal()
        self.crear_muro()
        salir = False
        juego_iniciado = False
        while not salir:
            self.reloj.tick(FPS)
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    return  True
                if evento.type == pg.KEYDOWN and evento.key == pg.K_SPACE:
                    juego_iniciado = True
            

            self.pintar_fondo()
            self.jugador.update()
            self.pantalla.blit(self.jugador.image, self.jugador.rect)
            

            self.muro.draw(self.pantalla)
            juego_iniciado = self.pelota.update(juego_iniciado)

            self.pelota.update(juego_iniciado)
            self.pantalla.blit(self.pelota.image, self.pelota.rect)

            golpeadas = pg.sprite.spritecollide(self.pelota, self.muro, True)
            if len(golpeadas)>0 :
                
                for ladrillo in golpeadas:
                        anterior = len(self.muro)
                        ladrillo.update(self.muro)
                        if len(self.muro) < anterior:
                            self.marcador.aumentar(ladrillo.puntos)
                
                self.pelota.vel_y = -self.pelota.vel_y
            self.marcador.pintar(self.pantalla)
            pg.display.flip()
            if self.pelota.he_perdido:
                # acciones cada vez que pierdo una vida
                salir = self.contador_vidas.perder_vida()
                self.pelota.he_perdido = False
                juego_iniciado = False
    
    def pintar_fondo(self):
        self.pantalla.fill((0, 0, 99))

        self.pantalla.blit(self.fondo, (0, 0))
        self.pantalla.blit(self.fondo, (600, 0))
        self.pantalla.blit(self.fondo, (0, 800))
        self.pantalla.blit(self.fondo, (600, 800))


    def crear_muro(self):
        filas = 6
        columnas = 9
        margen_superior = 60
        tipo = Ladrillo.verde

        for fila in range(filas):   # 0-3
            if tipo == Ladrillo.rojo:
                tipo = Ladrillo.verde
            else:
                tipo = Ladrillo.rojo

            for col in range(columnas):
                # por aquí voy a pasar filas*columnas = 24 veces
                puntos = (tipo-1) * (fila+1)
                ladrillo = Ladrillo(puntos, tipo)
                margen_izquierdo = (Ancho - columnas * ladrillo.rect.width) / 2
                # x = ancho_lad * col
                # y = alto_lad * fila
                ladrillo.rect.x = ladrillo.rect.width * col + margen_izquierdo
                ladrillo.rect.y = ladrillo.rect.height * fila + margen_superior
                self.muro.add(ladrillo)
                print(ladrillo.rect)


class Mejore_Jugadores(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)

    def bucle_principal(self):
        super().bucle_principal()
        salir = False
        while not salir:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    salir = True
            self.pantalla.fill((0, 99, 0))
            pg.display.flip()
