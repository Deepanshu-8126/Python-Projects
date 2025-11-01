
print("Welcome to the Python Quiz Game! 🐍")
print("Answer the questions and test your Python knowledge!\n")

questions = {
    "1️⃣ What is the correct file extension for Python files? ": ".py",
    "2️⃣ Which keyword is used to define a function in Python? ": "def",
    "3️⃣ What is the output of: print(type([]))? ": "<class 'list'>",
    "4️⃣ Which data type is immutable in Python? (list / tuple / dict) ": "tuple",
    "5️⃣ What does the len() function do? ": "returns length",
    "6️⃣ What keyword is used to start a loop in Python? ": "for",
    "7️⃣ Which operator is used for exponent (power) in Python? ": "**",
    "8️⃣ What will this code print? print(10//3) ": "3",
    "9️⃣ Which library is mostly used for data analysis in Python? ": "pandas",
    "🔟 Python was created by which developer? ": "guido van rossum"
}

score = 0

for q, a in questions.items():
    ans = input(q).lower().strip()
    if a.lower() in ans:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! Correct answer is: {a}\n")

print("🎯 Quiz Completed!")
print(f"Your Final Score: {score}/{len(questions)}")

if score == len(questions):
    print(" Excellent! You’re a Python Proooo!")
elif score >= 7:
    print("Great Job! You know Python well.")
elif score >= 4:
    print(" Not bad, keep learning!")
else:
    print("Keep practicing Python daily! Noobbb")
