// c program of linear search..
#include <stdio.h>

int main() {

    int n, i, key;

    // Input array size
    printf("Enter number of elements: ");
    scanf("%d", &n);

    int a[n];

    // Input array elements
    printf("Enter elements:\n");

    for(i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }

    // Search element..
    printf("Enter element to search: ");
    scanf("%d", &key);

    for(i = 0; i < n; i++) {

        if(a[i] == key) {
            printf("Element found at position %d", i + 1);
            return 0;
        }
    }

    printf("Element not found");

    return 0;
}