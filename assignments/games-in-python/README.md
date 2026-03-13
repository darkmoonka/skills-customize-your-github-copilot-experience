# 📘 Assignment: Hangman Game

## 🎯 Objective

Build an interactive Hangman word‑guessing game in Python to practice working with strings, loops, conditionals, and user input.

## 📝 Tasks

### 🛠️ Build the core Hangman game loop

#### Description
Implement the main game loop that repeatedly prompts the player to guess letters, updates game state, and displays progress until the game ends.

#### Requirements
Completed program should:

- Randomly select a secret word from a predefined list.
- Display the word as underscores (e.g., `_ _ _ _ _`) for unguessed letters.
- Prompt the player to guess a letter each turn.
- Reveal letters in the word when guessed correctly.
- Track incorrect guesses and remaining attempts.
- End the game when the word is fully guessed or the player runs out of attempts.
- Print a win message if guessed correctly or a lose message showing the secret word.

Example output:
```
Word: _ _ _ _ _
Guess a letter: a
Incorrect guesses left: 5
```

### 🛠️ Handle input validation and repeated guesses

#### Description
Improve the game by validating user input and preventing repeated guesses from counting against the player.

#### Requirements
Completed program should:

- Only accept a single alphabetical character as a guess.
- Ignore (and optionally warn about) invalid input (e.g., numbers, multiple characters).
- Keep track of letters already guessed and do not deduct attempts when a letter is guessed twice.
- Display the list of guessed letters or incorrect guesses each turn (optional but helpful).

