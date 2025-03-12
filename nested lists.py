if __name__ == '__main__':
    students = []  # List to store student names and grades

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])  # Append student data to list

    # Get unique sorted grades
    unique_grades = sorted(set(score for name, score in students))

    # Find the second lowest grade
    second_lowest_grade = unique_grades[1]

    # Get students with the second lowest grade, sorted alphabetically
    second_lowest_students = sorted([name for name, score in students if score == second_lowest_grade])

    # Print each name on a new line
    for student in second_lowest_students:
        print(student)
   
