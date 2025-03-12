#include <stdio.h>
#include <ctype.h>  // To check if a character is a digit

int main() {
    char str[1000];  // Array to store the input string
    int freq[10] = {0};  // Array to store the frequency of digits from 0 to 9

    // Read the input string
    fgets(str, sizeof(str), stdin);

    // Loop through the string
    for (int i = 0; str[i] != '\0'; i++) {
        if (isdigit(str[i])) {  // Check if the character is a digit
            freq[str[i] - '0']++;  // Increment the frequency for the respective digit
        }
    }

    // Print the frequencies of digits from 0 to 9
    for (int i = 0; i < 10; i++) {
        printf("%d ", freq[i]);
    }

    return 0;
}
