//Check if a string reads the same forwards and backwards.
#include <stdio.h>
#include <string.h>

int main() {
char str[100];
int i, j, isPalin = 1;

printf("Enter a string: ");
scanf("%s", str);

i = 0;
j = strlen(str) - 1;

while (i < j) {
if (str[i] != str[j]) {
isPalin = 0; // mismatch found, not palindrome
break;
}
i++; j--;
}

if (isPalin)
printf("'%s' is a Palindrome\n", str);

else
printf("'%s' is NOT a Palindrome\n", str);

return 0;
}
