//Print a right-angled triangle using nested loops...

#include <stdio.h>

int main() {
int n, i, j;
printf("Enter number of rows: ");
scanf("%d", &n);

// outer loop = rows, inner loop = stars in each row
for (i = 1; i <= n; i++) {
for (j = 1; j <= i; j++) {
printf("* ");
}

printf("\n"); // move to next line after each row
}

return 0;
}
