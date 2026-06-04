//Reverse a string by swapping characters from both ends moving toward the center.
#include <stdio.h>
#include <string.h>

int main() {
char str[100];
int i, j;
char temp;

printf("Enter a string: ");
scanf("%s", str);

i = 0;
j = strlen(str) - 1; // start from last character

// swap characters from both ends
while (i < j) {
temp = str[i];
str[i] = str[j];
str[j] = temp;
i++;
j--;
}

printf("Reversed: %s\n", str);

return 0;
}