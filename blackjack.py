import random
import time
import sys
import itertools

COLOR_VERDE = '\033[92m'
COLOR_RESET = '\033[0m'
COLOR_ROJO = '\033[91m'


Jugador = True
Casino = True

A = 1

J, Q , K = 10, 10, 10

cartas = ["A","J","Q","K","A","J","Q","K","A","J","Q","K","A","J","Q","K",2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10]

Player_1 = []
Banca = []

#mensaje de bienvenida + animacion de carga

print("\nCreated by JJandula\n\n🃏 Bienvenidos a la Mesa de BlackJack 🃏\n")


def rueda_de_carga(tiempo_espera):
    animacion = itertools.cycle(['♥️', '♦️', '♠️', '♣️'] )
    tiempo_inicio = time.time()

    while time.time() - tiempo_inicio < tiempo_espera:
        sys.stdout.write(f"\r{next(animacion)} {"El Crupier esta barajando las Cartas, en breves momentos comenzara la partida "}{next(animacion)}")
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write('\b')

    sys.stdout.write('\n')

rueda_de_carga(5)


#Espacio en blanco

print("")


#funcion de crupier

def crupier(turno):
    carta = random.choice(cartas)
    turno.append(carta)
    cartas.remove(carta)
    

#Calcula las manos jugadas

def total (turno):
    total = 0
    especiales = ["J","Q","K"]
    for carta in turno:
        if carta in range(1,11):
            total += carta
        elif carta in especiales:
            total += 10
        else:
            if total > 11:
                total +=1
            else:
                total += 11
    return total


# Comprobar ganador

def cartas_casa():
    if len(Banca) == 2:
        return Banca [0]
    elif len(Banca) > 2:
        return Banca[0],Banca[1]


# Bucles y fases del juego

for _ in range (2):
    crupier(Banca)
    crupier(Player_1)

    
while Jugador or Casino:
    print(f"🎰 - La Banca tiene un {cartas_casa()} y 🃏 \n")
    print(f"🃏 - Tus cartas son: {Player_1}, para un total de {total(Player_1)}\n")
    if Jugador:
        decision = input("1: Mantenerse\n2: Pedir Carta\n\n")
    if total(Banca) > 16:
        Casino = False
    else:
        crupier(Banca)
    if decision == "1":
        Jugador = False
    else:
        crupier(Player_1)
    if total(Player_1) >= 21:
        break
    elif total(Banca) >= 21:
        break

if total(Player_1) == 21:
    print(f"\n🃏 - Tus cartas son: {Player_1} Para un total de {total(Player_1)} \n\n🎰 - la Banca tiene: {Banca} para un total de {total(Banca)}\n")
    print(COLOR_VERDE + "BlackJack! Has Ganado! 🍀\n" + COLOR_RESET)
elif total (Banca) == 21:
    print(f"\n🃏 - Tus cartas son: {Player_1} Para un total de {total(Player_1)} \n\n🎰 - la Banca tiene: {Banca} para un total de {total(Banca)}\n")
    print(COLOR_ROJO + "BlackJack! La Banca ha ganado 🎰\n" + COLOR_RESET)
elif total(Player_1) > 21:
    print(f"\n🃏 - Tus cartas son: {Player_1} Para un total de {total(Player_1)} \n\n🎰 - la Banca tiene: {Banca} para un total de {total(Banca)}\n")
    print(COLOR_ROJO + "Te has pasado de 21.. la Banca Gana 🎰\n" + COLOR_RESET)
elif total(Banca) > 21:
    print(f"\n🃏 - Tus cartas son: {Player_1} Para un total de {total(Player_1)} \n\n🎰 - la Banca tiene: {Banca} para un total de {total(Banca)}\n")
    print(COLOR_VERDE + "La Banca se ha pasado de 21.. Has Ganado! 🍀\n" + COLOR_RESET)
elif 21 - total(Banca) < 21 - total(Player_1):
    print(f"\n🃏 - Tus cartas son: {Player_1} Para un total de {total(Player_1)} \n\n🎰 - la Banca tiene: {Banca} para un total de {total(Banca)}\n")
    print(COLOR_ROJO + "La Banca Gana! 🎰\n" + COLOR_RESET)
elif 21 - total(Banca) > 21 - total(Player_1):
    print(f"\n🃏 - Tus cartas son: {Player_1} Para un total de {total(Player_1)} \n\n🎰 - la Banca tiene: {Banca} para un total de {total(Banca)}\n")
    print(COLOR_VERDE + "Has Ganado! 🍀\n" + COLOR_RESET)




