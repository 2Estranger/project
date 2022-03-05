import random

def hangman():
    list_of_words = ['peace','sin', 'cold', 'death', 'angel', 'demon','breath','butterfly','trust','bang','high','ride']
    word = random.choice(list_of_words)
    print(word)
    '''Secret word'''
    
    chances = 10
    guess_made = ''
    '''casually for condition'''
    
    valid_word = set('abcdefghijklmnopqrstuvwxyz')
    # print(valid_word)
    
    while len(word) > 0:
        main_word = ""
        
        for letter in word:
            if letter in guess_made:
                main_word += letter
            else:
                main_word += '_ '
                
        if main_word == word:
            print(main_word)
            print("You won !")
            break
        
        print("guess the word",    main_word)
        guess = input("enter the guess letter")
        
        if guess in valid_word:
            guess_made += guess
            
        else:
            print("Invalid character")
            
        if guess not in word:
            chances -= 1
            
            if chances == 9:
                print("9 chances left")
                print("-----------")
            
            if chances == 8:
                print("8 chances left")
                print("-----------")
                print('     O     ')
                
            if chances == 7:
                print("7 chances left")
                print("-----------")
                print('     O     ')
                print("     |     ")
            
            if chances == 6:
                print("6 chances left")
                print("-----------")
                print('     O     ')
                print("     |     ")
                print('    /      ')
            
            if chances == 5:
                print("5 chances left")
                print("-----------")
                print('     O     ')
                print("     |     ")
                print('    / \    ')
                
            if chances == 4:
                print("4 chances left")
                print("-----------")
                print('    \O     ')
                print("     |     ")
                print('    / \    ')
                
            if chances == 3:
                print("3 chances left")
                print("-----------")
                print('    \O/    ')
                print("     |     ")
                print('    / \    ')
                
            
            if chances == 2:
                print("2 chances left")
                print("-----------")
                print('    \O/   | ')
                print("     |     ")
                print('    / \    ')
                
            if chances == 1:
                print("1 chance left !! Hangmam on his last breath")
                print("-----------")
                print('    \O/__| ')
                print("     |     ")
                print('    / \    ')
                
            if chances == 0:
                print("You loose")
                print("You let a good man die")
                print("-----------")
                print('     O__| ')
                print("    /|\     ")
                print('    / \    ')
                break
                
                
                
name = input("ENTER PLAYER NAME   -->  ")
print("Welcome", name, '!')
print('*****************')
print("You have 10 chances to guess the word")

hangman()

def again():
    while True:
        play_again = input("Do you want to play again enter y if yes or anything if no")
        if play_again == "y":
            hangman()
        else:
            break
again()