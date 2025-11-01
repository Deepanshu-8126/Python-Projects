name = input("Enter student name: ")
marks = float(input("Enter marks (out of 100): "))

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 40:
    grade = "D"
else:
    grade = "Fail"

print(f"{name} got {marks} marks and grade {grade}")
