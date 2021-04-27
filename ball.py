import pygame as pg
import sys

ROJO = (255, 0, 0)  #es bueno declarar los colores para luego usarlos con el nombre, en vez de hacerlo con tuplas
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
NEGRO = (0, 0, 0)
ANCHO = 800
ALTO = 600

pg.init()
pantalla = pg.display.set_mode((ANCHO, ALTO))

game_over = False                       #esto se va a repetir siempre
x = ANCHO // 2                                 # vamos a dejar la bola en el centro
y = ALTO // 2
vx = -5
vy = -5

while not game_over:
    #Gestión de eventos
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True
        
    #Gestión de la pantalla
    pantalla.fill(NEGRO)                            #pinta la pantalla para que la bola se mueva
    pg.draw.circle(pantalla, ROJO, (x, y), 10)      #esto establece las propiedades de la bola
    
    #Modificación de la pantalla
    x += vx
    y += vy

    if y == 0:
        #En vez de menos, quiero un más, para que rebote la bola
        vy = 5
    if y == ALTO:
        vy = -5
    if x == 0:
        vx = 5
    if x == ANCHO:
        vx = -5


    pg.display.flip()

pg.quit()
sys.exit()