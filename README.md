# Wordle Solver: An Algorithmic Approach to Winning Wordle in Less Than 4 Guesses

Welcome to the Wordle Solver! This project implements an algorithm based on principles from information theory to strategically guess Wordle words in fewer than four guesses. The algorithm leverages concepts from Claude Shannon's foundational work in information theory to maximize the information gained from each guess, ensuring efficient and effective Wordle solutions.

## Overview

Wordle is a popular word-guessing game where players have six attempts to guess a secret five-letter word. After each guess, the game provides feedback indicating which letters are correct and in the correct position (green), correct but in the wrong position (yellow), or incorrect (gray). This solver uses these clues to narrow down the possible secret words.

### How It Works

1. **Initial Guess**: The algorithm starts with an initial guess, selected to maximize potential information gain.
  
2. **Information Theory**: After receiving feedback from the game, the algorithm calculates the information content of the guess using Shannon's formula:
   \[
   I = \log_2 \frac{1}{p}
   \]
   where \( I \) is the information in bits, and \( p \) is the probability of the event.

3. **Strategic Guessing**: Instead of simply guessing the word that might be the answer, the algorithm strategically chooses words that will provide the most information about possible solutions. This approach reduces the number of potential solutions more effectively.

4. **Guaranteed Solution**: By iterating this process, the algorithm ensures that it will arrive at the correct word in less than four guesses.

### Example

Suppose the secret word ends in "ATCH" and you have narrowed it down to words like MATCH, CATCH, PATCH, and HATCH. Instead of guessing MATCH directly, the algorithm might choose "CHIMP" to maximize information gain. This ensures that the next guess will correctly identify the word.

## Why This Works

The algorithm leverages two key principles of information theory:

- **Inversely Related Predictability**: The less predictable an event, the more information it contains.
- **Additivity of Information**: Information from independent events adds up, enabling the algorithm to make more informed decisions with each guess.

### Key Concepts in Code

- **Entropy Calculation**: The core of the algorithm is calculating the entropy (uncertainty) of potential words and selecting guesses that minimize this entropy.
- **Word Elimination**: Based on the feedback after each guess, the algorithm eliminates words that no longer fit the criteria, quickly zeroing in on the correct word.

## Usage

Clone the repository and run the Wordle Solver:

```bash
git clone https://github.com/yourusername/wordle-solver.git
cd wordle-solver
python solver.py
