import random

name = input("Enter player name")
print("Welcome", name , "to Cow-Bull guessing game")

def game():
    number = list(range(10))
    '''we made a list of number (e.g; [0,1,2,3,4,5,6,7,8,9])'''
    # print(number) --> '''use to check only'''
    random.shuffle(number)
    '''now everytime you print a new shuffled list will exececute'''
    return number
# print(game()) --> '''use to check only'''

def player_number():
    number1 = game()
    secret_num = []
    for i in range(4):
        secret_num.append(number1[i])
    return secret_num

def check_number():
    cow = []
    bull = []
    '''here I took two list of cow-bull to append the number which is cow-bull'''
    number2 = player_number()
    
    # print(number2)
    '''|||SECRET NUMBER|||'''
    max_guess = 10
    while max_guess > 0:
        guess = int(input("Enter one guessing number:"))
        position = int(input("Enter the position:(e.g;[0,1,2,3])"))
        print("~~~~")
        
        if guess in number2:
            index = number2.index(guess)
            '''index() --> it will give o/p in indexing'''
            if index == position:
                if guess not in bull:
                    bull.insert(index,guess)
                    '''insert() --> it will insert the number in indexing position'''
                    print("Bull", bull)
                else:
                    ("You already found",bull,"try other digit")
            else:
                cow.append(guess)
                print("Cow, you can reuse this digit in different position", cow )
        if bull == number2:
            print(name,"Congartulation !!! You won")
            break
        
        max_guess -= 1
        print(max_guess,"chances left")
    else:
        print("You lose")
        return bull
check_number()


def play_again():
    while True:
        try_again = input("Enter y to play again or n to exit")
        if try_again == "y":
            check_number()
        else:
            break
play_again()