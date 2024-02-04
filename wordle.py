import os
import random
import sys
from termcolor import colored
import nltk
nltk.download('words')

from nltk.corpus import words

def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    print("Wordle :")
    print("Type a five letter word and hit Enter!. ",)

def clearLine():
    sys.stdout.write("\033[F")  
    sys.stdout.write("\033[K")  

nltk.data.path.append('/work/words')

wordList = words.words()
wordsFive = [word for word in wordList if (len(word) == 5)]
wordsFiveWP = [word for word in wordList if (len(word) == 5) and word[-1] != 's']


totalGuess = 6
playAgain = ""

while playAgain != 'q':

    attempt = 0
    invalidEntries = 0
    clearTerminal()
    print_menu()
    
    todaysWord = random.choice(wordsFiveWP)

    while attempt< totalGuess + invalidEntries :

        guess = input().casefold()
        attempt += 1

        if(len(guess) != 5)  or guess not in wordsFive:
            print(colored("Invalid guess.",'red'))
            invalidEntries += 1
            continue

        clearLine()

        print(f'{attempt - invalidEntries}. ',end = "")
        for i in range(5):
            if guess[i] == todaysWord[i]:
                print(colored(guess[i], 'green'),end="")
            elif guess[i] in todaysWord:
                print(colored(guess[i], 'yellow'),end="")
            else:
                print(guess[i],end="")
        print()

        if guess == todaysWord:
            print(f'\nCongrats!. You have won wordle in {attempt - invalidEntries} tries.')
            break
        elif attempt == totalGuess + invalidEntries:
           print(f'\nYou lost. The word was {todaysWord}')
        
          
    playAgain = input("\nPress anything to play again or 'q' to quit : ")
clearTerminal()



         


        

        



    