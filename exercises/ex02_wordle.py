""""Ultimate Wordle Knockoff"""

__author__: str = "730746714"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def main(secret: str) -> None:
    "The entrypoint of the program and main game loop"
    turnsused: int = 1
    emojifiedreturn: str = ""
    while turnsused <= 6:
        print(f"=== Turn {turnsused}/6 ===")
        emojifiedreturn = emojified(wordle=secret, guess=input_guess(len(secret)))
        print(emojifiedreturn)
        if emojifiedreturn == emojified(wordle=secret, guess=secret):
            print(f"You won in {turnsused}/6 turns!")
            return None
        else:
            turnsused += 1
    print("X/6 - Sorry, try again tomorrow!")
    return None


def contains_char(wordle: str, guess_character: str) -> bool:
    """Determines if a character given is found at any index of the first string"""
    assert len(guess_character) == 1, f"len('{guess_character}') is not 1"
    idx: int = 0
    while idx < len(wordle):
        if wordle[idx] == guess_character:
            return True
        else:
            idx += 1
    return False


def emojified(guess: str, wordle: str) -> str:
    # I made a mistake here when I made the parameter list (wordle: str, guest:str)
    """Yellow, Green, and White for Guesses"""
    assert len(guess) == len(wordle), "Guess must be same length as secret"
    idx: int = 0
    squares: str = ""
    # Took some time to figure out that it would be best to store results in a variable
    while idx < len(guess):
        if wordle[idx] == guess[idx]:
            squares += GREEN_BOX
        elif contains_char(wordle=wordle, guess_character=guess[idx]):
            squares += YELLOW_BOX
        else:
            squares += WHITE_BOX
        idx += 1
    return squares


def input_guess(guess_length: int) -> str:
    """Prompting the User"""
    userinput: str = input(f"Enter a {guess_length} character word")

    while len(userinput) != guess_length:
        userinput = input(f"That wasn't {guess_length} chars! Try again:")

    return userinput


if __name__ == "__main__":
    main(secret="codes")
