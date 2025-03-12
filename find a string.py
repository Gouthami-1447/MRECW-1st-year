def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):  # Iterate through the main string
        if string[i:i + len(sub_string)] == sub_string:  # Check if substring matches
            count += 1
    return count  # Return the total count


if __name__ == '__main__':