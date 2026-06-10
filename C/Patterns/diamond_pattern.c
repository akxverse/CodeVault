// Print a diamond....
#include <stdio.h>

int main()
{
    int n, i, j;
    printf("Enter half-size of diamond: ");
    scanf("%d", &n);

    // upper half (including middle).
    for (i = 1; i <= n; i++)
    {
        for (j = i; j < n; j++)
            printf(" "); // spaces
        for (j = 1; j <= (2 * i - 1); j++)
            printf("*"); // stars
        printf("\n");
    }

    // lower half.
    for (i = n - 1; i >= 1; i--)
    {
        for (j = n; j > i; j--)
            printf(" "); // spaces
        for (j = 1; j <= (2 * i - 1); j++)
            printf("*"); // stars
        printf("\n");
    }

    return 0;
}