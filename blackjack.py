import random,time,sys,itertools

COLOR_VERDE = '\033[92m'
COLOR_RESET = '\033[0m'
COLOR_ROJO = '\033[91m'


Jugador = True
Casino = True

cartas = ["A","J","Q","K","A","J","Q","K","A","J","Q","K","A","J","Q","K",2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10]

Player_1 = []
Banca = []

#mensaje de bienvenida + animacion de carga

print("\nCreated by JJandula for Codedex Final Project\n\n🃏 Welcome to the BlackJack Game 🃏\n")


def rueda_de_carga(tiempo_espera):
    animacion = itertools.cycle(['♥️', '♦️', '♠️', '♣️'] )
    tiempo_inicio = time.time()

    while time.time() - tiempo_inicio < tiempo_espera:
        sys.stdout.write(f"\r{next(animacion)} {" The Dealer is shuffling the Cards, in a few moments the game will begin "}{next(animacion)}")
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write('\b')

    sys.stdout.write('\n')

rueda_de_carga(5)



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
    print(f"\n🎰 - The Bank has a {cartas_casa()} y 🃏 \n")
    print(f"🃏 - Your Cards are: {Player_1}, For a total of {total(Player_1)}\n")
    if Jugador:
        decision = input("1: Hold\n2: Ask for Card\n\n")
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
    print(f"\n🃏 - Your Cards Are: {Player_1} For a total of {total(Player_1)} \n\n🎰 - The Dealer has: {Banca} For a total of {total(Banca)}\n")
    print(COLOR_VERDE + "BlackJack! You Win! 🍀\n" + COLOR_RESET)
elif total (Banca) == 21:
    print(f"\n🃏 - Your Cards Are: {Player_1} For a total of {total(Player_1)} \n\n🎰 - The Dealer has: {Banca} For a total of {total(Banca)}\n")
    print(COLOR_ROJO + "BlackJack! The Dealer has won 🎰\n" + COLOR_RESET)
elif total(Player_1) > 21:
    print(f"\n🃏 - Your Cards Are: {Player_1} For a total of {total(Player_1)} \n\n🎰 - The Dealer has: {Banca} For a total of {total(Banca)}\n")
    print(COLOR_ROJO + "You're over 21... The Dealer has won 🎰\n" + COLOR_RESET)
elif total(Banca) > 21:
    print(f"\n🃏 - Your Cards Are: {Player_1} For a total of {total(Player_1)} \n\n🎰 - The Dealer has: {Banca} For a total of {total(Banca)}\n")
    print(COLOR_VERDE + "The Dealer has gone beyond 21... You Win! 🍀\n" + COLOR_RESET)
elif 21 - total(Banca) < 21 - total(Player_1):
    print(f"\n🃏 - Your Cards Are: {Player_1} For a total of {total(Player_1)} \n\n🎰 - The Dealer has: {Banca} For a total of {total(Banca)}\n")
    print(COLOR_ROJO + "The Dealer has won 🎰\n" + COLOR_RESET)
elif 21 - total(Banca) > 21 - total(Player_1):
    print(f"\n🃏 - Your Cards Are: {Player_1} For a total of {total(Player_1)} \n\n🎰 - The Dealer has: {Banca} For a total of {total(Banca)}\n")
    print(COLOR_VERDE + "You Win! 🍀\n" + COLOR_RESET)
elif total(Banca) == total(Player_1):
    print(f"\n🃏 - Your Cards Are: {Player_1} For a total of {total(Player_1)} \n\n🎰 - The Dealer has: {Banca} For a total of {total(Banca)}\n")
    print("Same Card Result, Tie\n")




