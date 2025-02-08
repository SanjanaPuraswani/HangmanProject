import random
import time
import sys
from hangman_pics import hangman_pics  # Importing hangman pictures from the external file



# Celebration with dynamic hand movements at the same place
def celebration_animation():
    print("\nYAY! You Won!\n")  # Print the message once

    frames = [
        '''
             \o/  
              |   
             / \  
        ''',
        '''
              o   
             /|\\  
             / \  
        '''
    ]

    for _ in range(5):  # Repeat the celebration animation a few times
        for frame in frames:
            sys.stdout.write("\033[F" * 4)  # Move cursor up to overwrite previous frame
            sys.stdout.write("\033[2K\033[2K\033[2K\033[2K")  # Clear the previous lines
            print(frame, end="\r")  # Print the frame without adding extra newlines
            sys.stdout.flush()
            time.sleep(0.5)  # Pause for animation effect

    print("\n")  # Move cursor down after the animation ends for normal output




def choose_word():
    words = ['python', 'hangman', 'developer', 'coding', 'computer', 'algorithm']
    return random.choice(words)

# Hints for each word
hints = {
    'python': 'A popular programming language.',
    'hangman': 'A game where you guess letters to form a word.',
    'developer': 'A person who builds software.',
    'coding': 'The process of writing programs.',
    'computer': 'A device for processing data.',
    'algorithm': 'A step-by-step procedure for solving a problem.'
}

def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    while True:
        word = choose_word()
        guessed_letters = []
        attempts = 6  # Number of allowed wrong attempts

        print("Welcome to Hangman!")
        print(display_word(word, guessed_letters))
        print("\n")
        # Show the hint for the chosen word
        print(f"Hint: {hints[word]}\n")

        while attempts > 0:
            guess = input("Enter a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a valid letter.\n")
                continue

            if guess in guessed_letters:
                print("You've already guessed that letter.\n")
                continue

            guessed_letters.append(guess)

            if guess in word:
                print(f"Good guess! The word now looks like: {display_word(word, guessed_letters)}\n")
            else:
                attempts -= 1
                print(f"Wrong guess! You have {attempts} attempts remaining.")
                print(hangman_pics[6 - attempts])  # Display hangman figure from imported list
                print("\n")

            if '_' not in display_word(word, guessed_letters):
                print(f"Congratulations! You've guessed the word: {word}")
                celebration_animation()  # Show moving hands celebration when the word is guessed correctly
                break
        else:
            print(f"You've run out of attempts! The word was: {word}")
        
        # Ask user if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

hangman()
