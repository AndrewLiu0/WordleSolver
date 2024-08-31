from solver import *
from wordlist import WordList

if __name__ == "__main__":

    # Get 10 random words to test
    # wordBank = 
    wordBank = ["audio", "stain", "vicar", "swath", "prank"]
    randomNumGuesses = []
    mattParkerNumGuesses = []
                # , "knife", "ivory", "gravy", "north"]
    wl = WordList()
    mattParker = MattParker()
    random = RandomSolver()
    print(wordBank)

    for word in wordBank:
        
        mattParker = MattParker()
        mattParkerNumGuesses.append(GameManager(mattParker, word).play_game())
        random = RandomSolver()
        randomNumGuesses.append(GameManager(random, word).play_game())


print(f'Guesses: \n\t Matt Parker: {mattParkerNumGuesses} \n\t Random: {randomNumGuesses}')


        


