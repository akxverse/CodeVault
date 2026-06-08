// GCD (Greatest Common Divisor) using Euclid's algorithm recursively.
#include <stdio.h>

int gcd(int a, int b)
{
    if (b == 0)
        return a;         
    return gcd(b, a % b); // Euclid's algorithm
}

int main()
{
    int a, b;
    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);
    printf("GCD of %d and %d = %d\n", a, b, gcd(a, b));
    return 0;
}