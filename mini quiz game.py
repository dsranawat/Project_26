questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A) New Delhi", "B) Mumbai", "C) Kolkata", "D) Chennai"],
        "answer": "A"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A) Earth", "B) Jupiter", "C) Saturn", "D) Mars"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["A) Harper Lee", "B) Mark Twain", "C) F. Scott Fitzgerald", "D) Ernest Hemingway"],
        "answer": "A"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["A) Au", "B) Ag", "C) Pb", "D) Fe"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "B"
    }
]

def run_quiz():
    score = 0
    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}.")
    print(f"\nYour final score is {score}/{len(questions)}.")
    if score == len(questions):
        print("Congratulations! You got a perfect score!")
    elif score >= len(questions) // 2:
        print("Good job! You passed the quiz.")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    print("Welcome to the Mini Quiz Game!")
    print("Answer the following questions:")
    run_quiz()
    print("Thank you for playing!")