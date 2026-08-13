# Exercise 6: Student Scores Analysis

student_scores = {
    "Anisha": 78,
    "Ravi": 55,
    "Maya": 92,
    "Sagar": 61,
    "Nima": 48
}

# 1. Print every student and score using a loop
print("--- All Student Scores ---")
for name, score in student_scores.items():
    print(f"Student: {name}, Score: {score}")

# 2. Create a dictionary containing only students who scored at least 60 using dictionary comprehension
for name, score in student_scores.items():
    if score >= 60:
        passing_students={name: score}


# 3. Find the student with the highest score
top_student = max(student_scores, key=student_scores.get)
highest_score = student_scores[top_student]

# 4. Calculate the average score
average_score = sum(student_scores.values()) / len(student_scores)

# Display the results
print("\n--- Summary Analysis ---")
print(f"Passing Students (Score >= 60): {passing_students}")
print(f"Top Student: {top_student} with a score of {highest_score}")
print(f"Average Score: {average_score:.2f}")