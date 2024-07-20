import random

words = [
    "star", 
    "rain", 
    "book", 
    "moon", 
    "wind", 
    "ocean",
    "river",
    "earth",
    "cloud",
    "plane",
]

ascii_art = r'''
██╗░░██╗░█████╗░███╗░░██╗░██████╗░  ███╗░░░███╗░█████╗░███╗░░██╗
██║░░██║██╔══██╗████╗░██║██╔════╝░  ████╗░████║██╔══██╗████╗░██║
███████║███████║██╔██╗██║██║░░██╗░  ██╔████╔██║███████║██╔██╗██║
██╔══██║██╔══██║██║╚████║██║░░╚██╗  ██║╚██╔╝██║██╔══██║██║╚████║
██║░░██║██║░░██║██║░╚███║╚██████╔╝  ██║░╚═╝░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░  ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
'''

print(ascii_art)

BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
YELLOW = "\033[33m"
RESET = "\033[0m"
freddyboi = [r'''
  O   
 /|\  
 / \   ''']
print(freddyboi[0], end=" ")
print(f"{BOLD}{GREEN}<--- This is Freddy Boi{RESET}\n")
print()
print(f"{YELLOW}Freddy Boi’s about to hang because he sent a ‘love letter’ to his boss instead of his crush {RESET}\n")
print(f"{BOLD}===={RED} Guess the Word or Freddy Boi's Hangin' Around!{RESET} ====")


stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
wins=["Freddy Boi is still around! Maybe you’re not as hopeless as you look.",
      "Freddy Boi is safe! Who knew you had it in you?",
      "Freddy Boi lives to spell another day, thanks to your genius!",
      "Freddy Boi lives to guess another letter!"
]
loses=[
    "Freddy Boi is history! Brush up on your vocabulary.",
    "Congratulations! You’ve turned Freddy Boi into a permanent decoration.",
    "Freddy Boi is gone! Looks like spelling isn’t your strong suit.",
    "Freddy Boi’s now guessing words in heaven—thanks to your ‘help’!",
    "Looks like Freddy Boi’s taking a permanent nap. Your guessing skills really nailed it!"
]
random_word = random.choice(words)

count=0
storage = []
for brack in random_word:
    storage.append("_")

game_over = False
lives = 6
print(stages[-1])
print(f"{GREEN}Number of lives left = {lives}{RESET}")
print()
print(f"{BLUE}You can guess the letters in the word, if the letter is present it gets added to the word,else you will lose a life{RESET}")
print()
stageLevels = -2
while not game_over:
    guess = input("Enter your letter : \n").lower()
    for pos in range(len(random_word)):
        curr = random_word[pos]
        if(curr==guess):
            storage[pos] = curr
    if guess not in random_word:
        lives= lives-1
        print(stages[stageLevels])
        print(f"{RED}Number of lives left = {lives}{RESET}")
        stageLevels=stageLevels-1
        if lives==0:
            game_over=True
            print()
            print(f"{YELLOW}The correct word was {random_word}{RESET}")
            print()
            print(f"{RED}{BOLD}{random.choice(loses)}{RESET}")
    if not game_over:
        for char in storage:
            print(char+" ",end='')
        print()
        print()
    if "_" not in storage:
        game_over=True
        print(f"{GREEN}{BOLD}{random.choice(wins)}{RESET}")

