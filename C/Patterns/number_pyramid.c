//Print a pyramid of numbers....

#include <stdio.h>

int main() {
int n, i, j;
printf("Enter number of rows: ");
scanf("%d", &n);

for (i = 1; i <= n; i++) {
// print spaces for alignment

for (j = i; j < n; j++) printf(" ");
// print numbers from 1 to i

for (j = 1; j <= i; j++) printf("%d ", j);
printf("\n");
}

return 0;
}