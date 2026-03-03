import random
import json
import os

class FlashCard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

class FlashCardApp:
    """A CLI-based flash card application for studying."""
    def __init__(self, data_file="flashcards.json"):
        self.data_file = data_file
        self.cards = self.load_cards()

    def load_cards(self):
        """Loads cards from JSON."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except:
                return []
        return []

    def save_cards(self):
        """Saves current cards to JSON."""
        with open(self.data_file, 'w') as f:
            json.dump(self.cards, f, indent=4)

    def add_card(self):
        q = input("Enter the question/term: ")
        a = input("Enter the answer/definition: ")
        self.cards.append({"question": q, "answer": a})
        self.save_cards()
        print("Card added!")

    def start_quiz(self):
        if not self.cards:
            print("No cards available. Add some first!")
            return

        print("\n--- Starting Quiz (Press Enter to see answer, 'q' to stop) ---")
        temp_cards = list(self.cards)
        random.shuffle(temp_cards)

        score = 0
        for card in temp_cards:
            print(f"\nQuestion: {card['question']}")
            user_input = input("Your answer (or press Enter to reveal): ")
            
            if user_input.lower() == 'q':
                break
            
            print(f"Correct Answer: {card['answer']}")
            check = input("Did you get it right? (y/n): ")
            if check.lower() == 'y':
                score += 1

        print(f"\nQuiz Finished! You got {score}/{len(temp_cards)} correct.")

def main():
    app = FlashCardApp()
    while True:
        print("\n--- Flash Card Study Tool ---")
        print("1. Add New Card")
        print("2. Start Quiz")
        print("3. Exit")
        choice = input("Choice: ")

        if choice == '1':
            app.add_card()
        elif choice == '2':
            app.start_quiz()
        elif choice == '3':
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()