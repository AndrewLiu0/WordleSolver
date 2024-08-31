#!/usr/bin/env python3

from wordle import Player, GameManager
from scipy.stats import entropy
from wordlist import WordList
from information import patterns
import math

class BetterEntropySolver(Player):
    def __init__(self):
        super().__init__()
        self.wordlist = WordList()


    def make_guess(self):
        """
        the make_guess function makes a guess.

        Currently, it always guesses "salty". Write code here to improve your solver.
        """
        def calculateEntropy(self, word):
            allPatterns = patterns()
            entropySum = 0
            for pattern in allPatterns:
                matches = self.wordlist.matching(pattern, word)
                probability = len(matches)/len(self.wordlist)
                if probability > 0:
                    entropySum += probability * math.log(1/probability, 2)
            return entropySum
        
        if(self.num_guesses == 0):
            self.num_guesses += 1
            return "salet"

        currMax = 0
        highEntropyWord = ''
        for word in self.wordlist:
            entropy = calculateEntropy(self,word)
            if(entropy >= currMax):
                currMax = entropy
                highEntropyWord = word
        self.num_guesses += 1
        return highEntropyWord
    
    def update_knowledge(self, info):
        self.wordlist.refine(info)
        """
        update_knowledge updates the solver's knowledge with an `info`
        info is an element of the `Information` class. See `information.py`
        """
        print(info)
    

class EntropySolver(Player):
    def __init__(self):
        super().__init__()
        self.wordlist = WordList()
    
    def make_guess(self):
        """
        the make_guess function makes a guess.

        Currently, it always guesses "salty". Write code here to improve your solver.
        """
        def calculateEntropy(self, word):
            allPatterns = patterns()
            entropySum = 0
            for pattern in allPatterns:
                matches = self.wordlist.matching(pattern, word)
                probability = len(matches)/len(self.wordlist)
                if probability > 0:
                    entropySum += probability * math.log(1/probability, 2)
            return entropySum
        currMax = 0
        highEntropyWord = ''
        
        
        
        
        for word in self.wordlist:
            entropy = calculateEntropy(self,word)
            if(entropy >= currMax):
                currMax = entropy
                highEntropyWord = word
        self.num_guesses += 1
        return highEntropyWord
    
    def update_knowledge(self, info):
        self.wordlist.refine(info)
        print(self.wordlist)
        """
        update_knowledge updates the solver's knowledge with an `info`
        info is an element of the `Information` class. See `information.py`
        """
        print(info)

    


class MattParker(Player):
    '''
    The MattParker words are:
       fjord
       gucks
       nymph
       vibex
       waltz

       Good order:
       waltz
       vibex
       fjord
       nymph
       gucks
    '''
    def __init__(self):
        super().__init__()
        self.allInfo = []
        self.wordlist = WordList()

    def make_guess(self):
        """
        the make_guess function makes a guess.

        Currently, it always guesses "salty". Write code here to improve your solver.
        """
        if(self.num_guesses == 0):
            self.num_guesses += 1
            return "waltz"
        elif(self.num_guesses == 1):
            self.num_guesses += 1
            return "vibes"
        elif(self.num_guesses == 2):
            self.num_guesses += 1
            return "swill"
        
        self.num_guesses += 1
        return self.wordlist.get_random_word()

    def update_knowledge(self, info):
        self.wordlist.refine(info)
        """
        update_knowledge updates the solver's knowledge with an `info`
        info is an element of the `Information` class. See `information.py`
        """
        print(info)

class RandomSolver(Player):
    def __init__(self):
        self.num_guesses = 0
        self.wordList = WordList()

    def make_guess(self):
        """
        the make_guess function makes a guess.

        Currently, it always guesses "salty". Write code here to improve your solver.
        """
        
        self.num_guesses += 1
        return self.wordList.get_random_word()

    def update_knowledge(self, info):
        """
        update_knowledge updates the solver's knowledge with an `info`
        info is an element of the `Information` class. See `information.py`
        """
        print(info)

class Solver(Player):
    """
    "Solving" Wordle

    Your task is to fill in this class to automatically play the game.
    Feel free to modify any of the starter code.

    You Should write at least three subclasses of Player.
    1. A Random Player -- guess a random word each time!
    2. A Player that uses Matt Parker's 5 Words. 
       2a. How do you leveage the info gained from these 5 words?
       2b. Do always you have to guess all of these words?
       2c. What order should you guess these words in?
    3. Entropy Player (You are welcome to use the scipy above)
    4. Better and Better Players!

    Your goal is not just to Write the BEST SOLVER YOU CAN, but scientifically
    show that your solver is better than the others. 

    Note that the GameManager class returns the number of guesses a player makes.
    Compute 3 statistics:
    (1) the average number of guesses
    (2) the max number of guesses
    (3) the minimum number of guesses
    Feel free to add more statistics if you'd like.

    Think deeply about how you should design this experiments. How should you select the
    experimental inputs? Is it better for the two algorithms youre comparing to have the
    same or different test sets between experiments? 
    
    Please use objects and inheritance to structure your experiments.

    Here's an outline of the rest of the code in this project.
    - wordle.py.
      Hit play when VSCode is focused on this file to play
      a game of wordle against the computer! There are 3 classes
      of interest to the Solver:
      +  `Wordle` manages the world game state itself
      +  `Player` Provides a Human interface at the CLI to play the game
          Your Solver exposes the same interface as this class       
      +  `Game Manager` runs the main control loop for Wordle

    - information.py
      This file defines how information is propagated to the player. The relevant
      classes are `Information` and `Pattern`.
      + Pattern records a list `pattern` that represents the outcomes. 
        For instance
            [hit, miss, miss, mem, hit]
        Means the first and last letters of a guess are correct, the second two
        are not in the word, and the penultimate is in the word but not
        in the right spot. These codes are defined in `Code`.

      + Pattern provides a useful method `pattern.matches(guess, word)` which
        checks that the current pattern is consistent with guessing `guess` when
        `word` is the goal word

      + Information is constructed by passing it a player-provided `guess` and
        the `goal` word. 
        
      + Information provides an important method `info.matches(word)` which 
        returns true if `info.pattern == Information(info.guess, word)`

      + IMPORTANT. The `patterns()` function returns a list of all 3^5 patterns.

    - `wordlist.py`
       This file defines the `WordList` class, which is not actually a `list`,
       but wraps a list, defining some helpful wordle-specific features.
       + wordlist.get_random_word() gets a random word from the wordlist
       + wordlist.refine(info) keeps only those words consistent with `info`
       + wordlist.matching(pattern, guess) produces a literal `list`
         of words that such that if they had been the goal word, would have 
         produced pattern in responds to a player guessing `guess.

    
    IN GENERAL. FEEL FREE TO MAKE ANY MODIFICATIONS/ADDITIONS TO THIS CODE.
    You shouldn't neeeed to but of course please do if it makes your solution
    more elegant
    """

    def __init__(self):
        """
        Initialize the solver.
        """
        self.num_guesses = 0

    def make_guess(self):
        """
        the make_guess function makes a guess.

        Currently, it always guesses "salty". Write code here to improve your solver.
        """
        return "salty"

    def update_knowledge(self, info):
        """
        update_knowledge updates the solver's knowledge with an `info`
        info is an element of the `Information` class. See `information.py`
        """
        print(info)


def main():
    solver= BetterEntropySolver()
    # solver  = EntropySolver()
    manager = GameManager(solver)
    n_guess = manager.play_game()
    print("you found the word in", n_guess, "guesses")

if __name__ == "__main__": main()
