# Number of test cases
t = int(input())

for _ in range(t):
    try:
        # Read input values
        a, b = input().split()
        print(int(a) // int(b))  # Integer division
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)
