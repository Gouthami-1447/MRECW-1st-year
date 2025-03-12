def swap_case(s):
    return s.swapcase()  # Swap uppercase to lowercase and vice vers
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)