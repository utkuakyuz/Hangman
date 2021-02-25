import random
from HangmanSim_data import words,man

def Hangman (manimage,words):

    seperated = []
    seperated2 = []
    
    word = random.randint(0,len(words))
    random_word = words[word]
    
    #print("Your word is:", random_word)
    
    for i in random_word:
        seperated.append(i)
    for i in random_word:
        seperated2.append(i)
   
    for i in range(len(seperated)):
        seperated[i] = "_"
 
    false_choice = len(manimage)-1
    
    current = ""
    for i in seperated:
        current += str(i)
        
    oldletters = []
    current = list(current)
    hangman_index = 0
    print(man[0])
    
    str_c = ""
    for i in current:
        str_c += i + " "
    print(str_c)
    
    while false_choice != 0:
        guess = input("Enter Your Guess Here:").lower()
        oldletters.append(guess)

        if guess == "q":
            break
        if len(guess) !=1:
            print("Enter just a letter please")
        if len(guess) == 1:
            oldletters.append(guess)
            str1 = ""
            str2 = ""

            for i in range(len(random_word)):

                if random_word[i] == guess:
                    current[i] = guess

            for i in current:
                str1 += i + " "
            for i in random_word:
                str2 += i + " " 
            
            if not guess in random_word:
                
                hangman_index += 1
                false_choice -= 1
                
            print(str1)          
        print(man[hangman_index])
        print("You Have", false_choice, "choices left")
        
        if str2 == str1:
            print("You guessed the word, Great!")
            try_again = input("Play Again ? Y/N: ").upper()
            if try_again == "Y":
                Hangman(man,words)
            if try_again =="N":
                print("Thanks For Playing :)")
                
            break
        
        if false_choice == 0:
            try_again = input("YOU HAVE FAILED, TRY AGAIN ? Y/N :").upper()
            if try_again == "Y":
                Hangman(man,words)
            if try_again =="N":
                print("Thanks For Playing :)")
                break
                
                
Hangman(man,words)