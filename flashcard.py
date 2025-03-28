import json
import random

class Teacher:
    def __init__(self, phrase, answer, image=None):
        self.phrase = phrase
        self.answer = answer
        self.image = image
    
    def input_phrase(self):
        return f"{self.phrase} {self.answer} {self.model}"
    
    def to_dict(self):
        return {"phrase": self.phrase, "answer": self.answer, "image": self.image}

def main():
    mode = input("Choose your mode: Teacher (T) or Student (S): ").strip().lower()

    if mode == 'T':
        print("Teacher Mode:")
        t()  
    elif mode == 'S':
        print("Student Mode:")
        s() 
    else:
        print("Invalid input. Please choose 'T' for Teacher or 'S' for Student.")

# 1
def t():
    while True:
     a = input("What phrase would you like to input?")

     b = input("What is the correct answer?")

     c = input("Link of image reference?")

new_flashcard = Teacher("a","b","c")

try:
    with open("f.json", "r") as file:
        fc_data = json.load(file)
except FileNotFoundError:
        fc_data = []

fc_data.append(new_flashcard.to_dict())

with open("fc.json", "w") as file:
    json.dump(fc_data, file, indent=4)
  
print("Flashcard added successfully!")

continue_input = input("Would you like to add another flashcard? (y/n): ")
if continue_input == 'n':
    break


def s():
    try:
        with open("fc.json", "r") as file:
            fc_data = json.load(file)
    except FileNotFoundError:
        print("No flashcards found. Please add some flashcards in Teacher Mode.")
        return
score = 0
streak = 0
total_questions = 0

while True:
    flashcard = random.choice(fc_data)
    question = flashcard['phrase']
    correct_answer = flashcard['answer']

    print(f"Question: {question})")
    user_answer = input("Your answer:")

    if user_answer == correct_answer:
        print("Correct!")
        score = score + 1
        streak = streak + 1
        total_questions = total_questions + 1
    else:
        print(f"Incorrect. The correct answer was: {correct_answer}")
        streak = 0
        total_questions = total_questions + 1
    
    continue_game = input("Do you want to continue? (y/n): ")
    if continue_game == "n":
     break
    print(f"Final Score: {score} / {total_questions}")
    print("Thank you for playing!")
