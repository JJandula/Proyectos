

import time

def welcome():
    print("\nWelcome to Space Odissey! 🚀")
    time.sleep(1)
    print("\nIn the year 2150, the Earth was on the brink of collapse. Natural resources were rapidly depleting, and attempts to reverse climate change had proven insufficient. Humanity was facing extinction, and the only hope lay in finding a new home in the vast universe.")
    time.sleep(1)

def make_choice(options):
    print("\n")
    print("Select one option:\n")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    
    while True:
        try:
            choice = int(input("\nEnter the number of your choice: "))
            if choice == 1 or 2:
                return choice
            else:
                print("\nInvalid Answer..")
        except ValueError:
            print("Invalid input. Please enter a number.")

def game():
    print("\nWe have just left Earth's orbit, what is your main decision?")
    time.sleep(1)

    options = ["Explore the nearby star system to ensure a shorter journey and quick arrival to possible habitable planets. 🪐\n", "Opt for the most distant star system in the hope of finding a more favorable planet, even if this involves a longer trip and greater risks. 👽\n"]
    choice = make_choice(options)

    if choice == 1:
        print("\nYou chose the 1.\n")
        time.sleep(1)
        print("\nFinds a system made up of 5 planets, of which 2 are habitable.")
        time.sleep(1)
        
    elif choice == 2:
        print("\nYou chose the 2.\n")
        time.sleep(1)
        print("\nThe crew continues traveling to the next system.")
        time.sleep(1)
        print("\nCrew supplies will now be reduced by 50%")
    else:
        print("Respuesta incorecta")

    if choice == 1:

        print("\nWe have found a decision point..\n")

        time.sleep(1)

        print("What decision do you want to make now capital?\n")
    
        options = ["Farthest planet ➕ ⏰", "Close planet ➖ ⏰"]

        choice = make_choice(options)

        if choice == 1:
            print("\nYou select Farthest planet.")
            time.sleep(1)
            print("\nThe most distant planet has optimal conditions for the life of the human race!\n")
            print("YOU WIN! 🏠\n")
        elif choice == 2:
            print("\nYou choose Close planet")
            time.sleep(1)
            print("\nThe planet is 60% similar to Earth, it is not the best home but it will serve us well!\n")
            print("YOU CAN DO BETTER.. 🪐\n")

    elif choice == 2:


        print("\nAfter 5 years traveling, one day they find an extraterrestrial civilization around an unexplored planet.\n")

        time.sleep(1)

        print("What decision do you want to make now capital?")
    
        options = ["Contact aliens 🤝\n", "Pass and not be detected 🥷\n"]

        choice = make_choice(options)

        if choice == 1:
            print("\nYou select Contact aliens.")
            time.sleep(1)
            print("\nThe aliens care about human civilization and decide to donate a technology that will solve the problem on Earth! From this moment we already have new allies in the solar system!\n")
            print("YOU SAVE THE HUMANITY! 🌏\n")
        elif choice == 2:
            print("\nYou choose Pass and not be detected")
            time.sleep(1)
            print("\nThis was the last planet before supplies ran out. Humanity had not been able to find a new home.\n")
            print("GAME OVER... ❌\n")



def main():
    welcome()
    game()

if __name__ == "__main__":
    main()