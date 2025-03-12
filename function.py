def is_leap(year):
    leap = False  # Default to False
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
        else:
            leap = True  # Fixed typo: should be 'True', not 'true'
    
    return leap

year = int(input())