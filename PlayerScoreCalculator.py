#Write a program It should be realized as a ‘Player’class, where each of the player is a separate object. Inside it stores the score of the player and has 
#method for calculating the score of a given word. Make a simple text UI to enhance the program's 
#accessibility for players


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def calculate_score(self, word):
        score = sum(ord(char) - ord('a') + 1 for char in word.lower())
        self.score += score
        return score

# Simple text UI for demonstration
def main():
    print("Word Scoring Game")

    # Get player names
    player1_name = input("Enter Player 1 name: ")
    player2_name = input("Enter Player 2 name: ")

    # Create player objects
    player1 = Player(player1_name)
    player2 = Player(player2_name)

    while True:
        print("\nOptions:")
        print("1. Enter a word for Player 1")
        print("2. Enter a word for Player 2")
        print("3. View scores")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            word = input(f"{player1.name}, enter a word: ")
            score = player1.calculate_score(word)
            print(f"Score for '{word}': {score}")

        elif choice == "2":
            word = input(f"{player2.name}, enter a word: ")
            score = player2.calculate_score(word)
            print(f"Score for '{word}': {score}")

        elif choice == "3":
            print(f"\nScores:")
            print(f"{player1.name}: {player1.score}")
            print(f"{player2.name}: {player2.score}")

        elif choice == "4":
            print("Exiting the game. Final scores:")
            print(f"{player1.name}: {player1.score}")
            print(f"{player2.name}: {player2.score}")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
