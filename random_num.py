import random

def wellcome():
    '''
    This function gets no parametres and just print a welcome text and help user how to play game.
    '''
    return "Wellcome to our game.\nIn this game I choose a random number between 1 to 20 and you have to find it by guess numbers."

def goodbye():
    '''
    Thi function gets no parametres and print a text to say goodbye.
    '''
    return "Have a nice day and goodbye."

def get_a_guess():
    '''
    This function gets no parametres and just return the values of input it get.
    '''
    res = int(input("Enter guess : "))
    return res

def win(computer_number, guess):
    '''
    This funcion get two parametres:
    first = int => random num gets from random madule
    second = int => guess from the user
    resualt ==> check and return first == second
    '''
    return computer_number == guess

def answer(computer_number, guess):
    '''
    This function gets two parametres:
    first = int => random num gets from random madule
    second = int => guess from the user
    resualt ==> return some clues to user to find a random number faster and better
    '''
    if guess < computer_number:
        return "You should guess a bigger number."
    if guess > computer_number:
        return "You should guess a smaller number."
    return "Wow... . You win."

def finish(computer_number, count):
    '''
    THis function gets two parametres:
    first = int => random num gets from random madule
    second = int => a count of number user guesses
    resault ==> check count of user guesses and if count is lower than best player count replace that.
                and if count of user guesses higher than best player tell user best player count and say user is not on leaderboard.
    '''
    if check_best_player(count):
        if count == 1:
            print("My number is {} and you find it in {} guess and you are on leaderboard.".format(computer_number, count))
            save_best_player(count)
        else:
            print("My number is {} and you find it in {} guesses and you are on leaderboard.".format(computer_number, count))
            save_best_player(count)
    elif not check_best_player(count):
        if count == 1:
            if tell_best_player_count() == 1:
                print("My number is {} and you find it in {} guess but you are not in the leader board.\nThe leader board player find my number in {} guess.".format(computer_number, count, tell_best_player_count()))
            else:
                print("My number is {} and you find it in {} guess but you are not in the leader board.\nThe leader board player find my number in {} guesses.".format(computer_number, count, tell_best_player_count()))
        else:
            if tell_best_player_count() == 1:
                print("My number is {} and you find it in {} guesses but you are not in the leader board.\nThe leader board player find my number in {} guess.".format(computer_number, count, tell_best_player_count()))
            else:
                print("My number is {} and you find it in {} guess but you are not in the leader board.\nThe leader board player find my number in {} guesses.".format(computer_number, count, tell_best_player_count()))
def play_again_function():
    '''
    get a input to a user and say do you want play again and if user say in uppercase in list of possitive words return True and else return False.
    '''
    user_choice = input("Do you want to play again? Y/N : ")
    p_list = ["YES", "Y", "BALE", "ARE"]
    if user_choice.upper() in p_list:
        return True
    else:
        return False

def check_best_player(count):
    '''
    This function gets one parametres:
    first = int => count of user guesses
    resualt ==> check if user count is lower than best player record save in records.txt return True and else return False.
    '''
    with open("record.txt", "r") as record_file:
        lines = record_file.readlines()
        if int(lines[0]) > int(count):
            return True
        else:
            return False

def tell_best_player_count():
    '''
    This function gets no parametres and returns the count of guesses of best player.
    '''
    with open("record.txt", "r") as record_file:
        lines = record_file.readlines()
        return int(lines[0])

def save_best_player(count):
    '''
    This function gets one parametres:
    first = int => count of user guesses
    resualt ==> save count to a records.txt as a best player record.
    '''
    with open("record.txt", "w") as record_file:
        count = str(count)
        record_file.write(count)

print(wellcome())
play_again = True
while play_again:
    computer_number = random.randint(1, 20)
    guess = 0
    count = 0
    while not win(computer_number, guess):
        guess = get_a_guess()
        count += 1
        print(answer(computer_number, guess))
    finish(computer_number, count)
    play_again = play_again_function()
print(goodbye())