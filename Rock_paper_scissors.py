import random
rock = '''

       _______
    |
___        ___)
        (________)
        (________)
  ___   (______)
      __ (____)

'''


paper = '''


        ________
____|   _______)____
            ________)
            ________)
 ___    __________)
    . __________)

'''

scissors = '''

        ________
     |
____     _______)_____
            __________)
        ________________)
 ___    (_________)
     __ (______)

'''

end_game = "The game is ended"

game_images = [rock,paper,scissors,end_game]
while True:
    user_choice = int(input("Enter your choice : type 0 for rock, 1 for paper, 2 for scissors."))
    if user_choice >=4 or user_choice < 0:
        print("You entered invalid number, You Lose")
    else:
        print(game_images[user_choice])
        computer_choice = random.randint(0,2)
        print("computer choice:")
        print(computer_choice)
        print(game_images[computer_choice])

        if computer_choice == user_choice:
            print("it's a Draw.")

        elif user_choice == 3:
            print("The game is ended")
            break

        elif computer_choice == 0 and user_choice == 2:
            print("You Lose.")

        elif user_choice == 0 and computer_choice == 2:
            print("You Win.")

        elif computer_choice > user_choice:
            print("You Lose.")

        elif user_choice > computer_choice:
            print("You Win.")
        
       
