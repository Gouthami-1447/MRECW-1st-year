if __name__ == '__main__':
    n = int(input())  # Read number of scores
    arr = list(map(int, input().split()))  # Read scores as a list

    # Convert to a set to remove duplicates, then sort in descending order
    unique_scores = sorted(set(arr), reverse=True)

    # Print the second highest score (runner-up)
    print(unique_scores[1])
