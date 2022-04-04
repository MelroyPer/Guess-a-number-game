#guess the number

for x in range(0,5):
    choice = 4 - x
    inp = int(input("Guess a number:\n"))
    if inp>62:
        print("Guess lesser number",)
        print("You have only", choice, "choice")

    if inp==62:
        print("congratulation!!! you won")
        break
    if inp<62:
        print("Guess greater number")
        print("You have only",choice,"choice")
    if choice==0:
        print("game over")