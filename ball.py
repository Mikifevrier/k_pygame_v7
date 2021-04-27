import pygame as pg
import sys

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

game_over = False                                   #esto se va a repetir siempre
x = ANCHO // 2                                      #vamos a dejar la bola en el centro
y = ALTO // 2
vx = -5
vy = -5
reloj = pg.time.Clock()                             #creo la variable reloj para establecer la tasa de fps

while not game_over:
    reloj.tick(60)                                  #ralentiza los frames para que la bola no salga tan rápida
    #Gestión de eventos
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True
        
    #Gestión de la pantalla
    pantalla.fill(NEGRO)                            #pinta la pantalla para que la bola se mueva
    pg.draw.circle(pantalla, ROJO, (x, y), 10)      #esto establece las propiedades de la bola
    
    
    #Modificación de la pantalla para que rebote la pelota
    x += vx
    y += vy

    if y <= 0 or y >= ALTO:                                   #ponemos <= o >= 0 porque si usamos un número impar, se va
    #En vez de menos, quiero un más, para que rebote la bola
        vy = -vy
    
    if x <= 0 or x>= ANCHO:                         #EN LAS LINEAS 42 a 50, hemos puesto lo mismo, pero de otra manera (usando or)
        vx = -vx

    pg.display.flip() #¡Muestralo!

fin_juego()