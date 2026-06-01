#include <stdio.h>

int power(int a, int b) {

    if(b == 0)
        return 1;

    return a * power(a, b - 1);
}

int main() {

    int base, exponent;

    printf("Enter base and exponent: ");
    scanf("%d %d", &base, &exponent);

    printf("Result = %d", power(base, exponent));

    return 0;
}