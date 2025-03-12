#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);  // Read the integer input

    // Array of words for numbers 1 to 9
    char *words[] = { "one", "two", "three", "four", "five", 
                      "six", "seven", "eight", "nine" };

    if (n >= 1 && n <= 9) {
        printf("%s\n", words[n - 1]);  // Print corresponding word
    } else {
        printf("Greater than 9\n");  // Print if n > 9
    }

    return 0;
}
