# grade_calculator.py

def calculate_grade():
    print("--- Academic Grade Portal ---")
    
    try:
        # 2. Take marks input
        raw_input =int(input("Enter the student's marks (0-100): ") )
        marks = float(raw_input)

        # 5. Handle invalid marks using conditions
        if marks < 0 or marks > 100:
            print("Error: Invalid input. Marks must be between 0 and 100.")
            return

        # 7. Nested conditions for business rules (e.g., Attendance check)
        # Simulating a rule: If marks are near a boundary, check "Participation"
        has_good_attendance = True # This could be another input()

        # 3 & 4. Determine grade using if-elif-else and logical operators
        if marks >= 90:
            grade = "A+"
            message = "Excellence achieved! Keep it up."
        
        elif marks >= 80 and marks < 90:
            grade = "A"
            message = "Great job! You have a solid understanding."
            
        elif marks >= 70 or (marks >= 65 and has_good_attendance):
            # 7. Business Rule: A 'B' can be earned with 65+ if attendance is good
            grade = "B"
            message = "Good work. You've cleared the requirements comfortably."
            
        elif marks >= 50 and marks < 70:
            grade = "C"
            message = "Passed. Consider reviewing the advanced modules."
            
        elif marks >= 40:
            grade = "D"
            message = "Marginal Pass. You are eligible for a retake to improve."
            
        else:
            grade = "F"
            message = "Fail. Please schedule a meeting with your counselor."

        # 6. Display proper messages
        print(f"\nResults: \nGrade: {grade} \nStatus: {message}")

    except ValueError:
        print("Invalid input: Please enter a numeric value.")

# 9. Execute and test
if __name__ == "__main__":
    calculate_grade()