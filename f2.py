#2.INTERACTIVE QUIZ

import json

# Define the quiz questions and answers
quiz_data = [
    {"question": "What is the capital of Philippines?", "answer": "Manila"},
    {"question": "Who wrote Noli Me Tangere?", "answer": "Jose Rizal"},
    {"question": "Who is the first woman president of the Philippines?", "answer":"Corazon Aquino"},
    # Add more questions here...
]

# Ensure we have at least 100 questions
# For the sake of example, we'll duplicate the sample questions to reach 100
while len(quiz_data) < 100:
    quiz_data.extend(quiz_data[:100-len(quiz_data)])

def interactive_quiz(quiz_data):
    user_answers = []
    score = 0
    
    print("Welcome to the Interactive Quiz!")
    print(f"There are {len(quiz_data)} questions. Let's get started!\n")
    
    for index, item in enumerate(quiz_data):
        print(f"Question {index + 1}: {item['question']}")
        user_answer = input("Your answer: ").strip()
        user_answers.append({"question": item['question'], "your_answer": user_answer, "correct_answer": item['answer']})
        
        if user_answer.lower() == item['answer'].lower():
            score += 1
            print("Correct!\n")
        else:
            print(f"Wrong! The correct answer is {item['answer']}.\n")
    
    print("Quiz Complete!")
    print(f"Your total score is: {score} out of {len(quiz_data)}\n")
    
    print("Review your answers:")
    for answer in user_answers:
        print(f"Question: {answer['question']}")
        print(f"Your answer: {answer['your_answer']}")
        print(f"Correct answer: {answer['correct_answer']}\n")
    
    with open('quiz_results.json', 'w') as f:
        json.dump(user_answers, f, indent=4)

if __name__ == "__main__":
    interactive_quiz(quiz_data)
