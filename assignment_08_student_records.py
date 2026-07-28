# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def verification(student_id, students) :
    for i, data in enumerate(students) :
        if data["id"] == student_id :
            return True, i
    return False, -1


def add_student(students) :
    student_name = input("Student name: ")
    student_id = input("Student ID: ")
    num_score = int(input("How many scores? "))
    list_score = []
    for i in range(1,num_score+1) :
        score = int(input(f"Enter score {i}: "))
        list_score.append(score)
    student_data = {
        "name" : student_name ,
        "id" : student_id ,
        "scores" : list_score
    }
    students.append(student_data)
    print(f"Student \"{student_name}\" added successfully.")


def average_score(index, students) :
    scores = students[index]["scores"]
    if len(scores) == 0 :
        return 0.0
    total = 0
    for x in scores :
        total += x
    return total / len(scores)
           

def view_all_student(students) :
    if len(students) == 0 :
        print("No students have been added yet.")
        return

    print("""
    --------------------------------------------------
    Name           ID          Scores         Average
    --------------------------------------------------
    """) 
    for i, data in enumerate(students) :
        scores_text = ", ".join(str(score) for score in data["scores"])
        average = average_score(i, students)
        print(f"{data['name']}   {data['id']}    {scores_text}     {average:.2f}")
    print("--------------------------------------------------")


def main() :
    students = []

    print("""
    ================================
    STUDENT RECORD SYSTEM MENU
    ================================
    1. Add student
    2. Display all student
    3. Calculate average
    4. Quit
    """)

    n = int(input("Enter your choice (1-4): "))
    if n == 4 :
        print("Goodbye")
    while n != 4 :
        if n == 1 :
            add_student(students)
        elif n == 2 :
            view_all_student(students)
        elif n == 3 :
            student_id = input("Enter student ID: ")
            found, index = verification(student_id, students)
            if found :
                average = average_score(index, students)
                print(f"{students[index]['name']}'s average score: {average:.2f}")
            else :
                print("Student not found")
        else :
            print("Error : invalid input .Choose a number from 1 to 4")

        n = int(input("Enter your choice (1-4): "))


if __name__ == "__main__" :
    main()

