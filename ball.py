import pygame as pg
import sys
from random import randint
from random import randrange
from random import choice


#Es más cómodo crear una función que permita cerrar el juego
def fin_juego():
    pg.quit()
    sys.exit()

ROJO = (255, 0, 0)  #Es bueno declarar los colores para luego usarlos con el nombre, en vez de hacerlo con tuplas
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
NEGRO = (0, 0, 0)
ANCHO = 800
ALTO = 600

pg.init()
pantalla = pg.display.set_mode((ANCHO, ALTO))
reloj = pg.time.Clock()                             #creo la variable reloj para establecer la tasa de fps

class Bola():
    def __init__(self, x, y, vx, vy, color, radio=10):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.radio = radio

    def actualizar(self):
        self.x += self.vx
        self.y += self.vy

        if self.y<=0 or self.y>=ALTO:
            self.vy = -self.vy

        if self.x<=0 or self.x>=ANCHO:
            self.vx = -self.vx
    
    def dibujar(self, lienzo):
        pg.draw.circle(lienzo, self.color, (self.x, self.y), self.radio) #pg.draw.circle necesita los parámetros surface, color, center y radius)



bolas = []

for _ in range(10):
    bola = Bola(randint(0, ANCHO),
                randint(0, ALTO),
                randint(5, 10)*choice([-1, 1]),
                randint(5, 10)*choice([-1, 1]),
                (randint(0, 255), randint(0, 255), randint(0, 255)))
    
    bolas.append(bola)

game_over = False                                       #esto se va a repetir siempre
while not game_over:
    reloj.tick(60)                                      #ralentiza los frames para que la bola no salga tan rápida
    #Gestión de eventos
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True
        
    #Gestión de la pantalla
    pantalla.fill(NEGRO)
    for bola in bolas:                             
        bola.dibujar(pantalla)
    
    #Modificación de la pantalla para que rebote la pelota / Modificación de Estado
    for bola in bolas:
        bola.actualizar()

    pg.display.flip() #¡Muestralo!

fin_juego()