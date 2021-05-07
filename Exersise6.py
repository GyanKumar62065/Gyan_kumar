# Game
# Snake Water Gun

import random , playsound

def winning_music():
    """
    Plays the winning music
    """
    win_music = ["animal wow.mp3", "bruhh.mp3"]
    try:
        playsound.playsound(random.choice(win_music))
    except Exception as e:
        print(e)

def losing_music():
    """
    Plays the losing music
    :return:
    """
    lose_music = ["Nope.mp3","Fart.mp3"]
    try:
        playsound.playsound(random.choice(lose_music))

    except Exception as e:
        print(e)

def tie_music():
    """
        Plays the losing music

    """
    try:
        playsound.playsound("Awkward Cricket .mp3")

    except Exception as e:
        print(e)
if __name__ == '__main__':
    print('\n Welcome to Snake Water Gun game! \n\n')

    print("No of guesses = 10 ")

    attempts = 1
    your_point =0
    computer_point = 0

    while (attempts<=10):

        lst = ['s','w','g']
        ran =random.choice(lst)

        print('s for Snake \t w for Water \t g for Gun')

        inp = input('Enter your choice { s or w or g}: \n')
        inp = inp.lower()

        if inp == "s" and ran == "s":
            print('Tie')
            print(f"\n You chose Sanke and Computer also chose Snake!")
            print('No body gets point \n')
            tie_music()


        elif inp == "w" and ran == "w":
            print('Tie')
            print(f"\n You chose Water and Computer also chose Water!")
            print('No body gets point \n')
            tie_music()

        elif inp == "g" and ran == "g":
            print('Tie')
            print(f"\n You chose Gun and Computer also chose Gun!")
            print('No body gets point \n')
            tie_music()

        elif inp == "s" and ran == "w":
            print(f"\n You chosesd Snake and Computer chose Water!")
            print('The Sanke Drank Water')
            print('You won this round')
            print('You get 1 point \n')
            winning_music()


        elif inp == "w" and ran == "s":
            print(f"\n You chosesd Water and Computer chose Snake!")
            print('The Sanke to drown in Water')
            print('You loss this round')
            print('Computer get 1 point \n')
            losing_music()

        elif inp == "w" and ran == "g":
            print(f"\n You chosesd Water and Computer chose Gun!")
            your_point = your_point + 1
            print('The Gun sank in Water')
            print('You won this round')
            print('You get 1 point \n')
            winning_music()


        elif inp == "g" and ran == "w":
            print(f"\n You chosesd Gun and Computer chose Water!")
            computer_point = computer_point + 1
            print('The Gun sank in Water')
            print('You loss this round')
            print('Computer get 1 point \n')
            losing_music()



        elif inp == "g" and ran == "s":
            print(f"\n You chosesd Gun and Computer chose Snake!")
            your_point = your_point + 1
            print('The Snake was shot and he died \n')
            print('You win this round')
            print('You get 1 point \n')
            winning_music()


        elif inp == "s" and ran == "g":
            print(f"\n You chosesd Snake and Computer chose Gun!")
            computer_point = computer_point + 1
            print('The Snake was shot and he died \n')
            print('You loss this round')
            print('Computer get 1 point \n')
            losing_music()

        else:
            print('Invailid input! \n')
            continue

        print("\n No. of guesses left: {}".format(10-attempts))
        attempts = attempts+1

        if attempts>10:
            print("\n GAME OVER! \n")

    print(f"Your Score: {your_point} \n Computer's Score: {computer_point}")

    if computer_point > your_point:
        print("\n Computer won and You lost! \n")

    elif computer_point < your_point:
        print("\n You won and Computer lost! \n")
    else:
        print("It was a tie!")
        print("Invailid")

    print(11 - attempts ," No. of guesses left")
    attempts = attempts + 1

    if attempts>10:
        print("\n GAME OVER! \n")

    if computer_point > your_point:
        print("\n Computer wins and You lose! \n")

    elif computer_point < your_point:
        print("\n You win and Computer lose! \n")

    print(f"Your point are {your_point} \n Computer's points are {computer_point}")


