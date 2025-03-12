if __name__ == '__main__':
    n = int(input())  # Number of students
    student_marks = {}  # Dictionary to store student names and scores

    for _ in range(n):
        # Read input and split into name and scores
        name, *line = input().split()
        scores = list(map(float, line))  # Convert scores to float
        student_marks[name] = scores  # Store in dictionary

    query_name = input()  # Student name to query

    # Calculate average and print with 2 decimal places
    avg_marks = sum(student_marks[query_name]) / len(student_marks[query_name])
    print(f"{avg_marks:.2f}")
