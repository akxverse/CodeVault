#include <stdio.h>
void insertionSort(int arr[], int n)
{
    int i, j, k;
    for (i = 1; i < n; i++)
    {
        k = arr[i];      // Element to be inserted
        j = i - 1;

        // Shift elements greater than k to one position ahead
        while (j >= 0 && arr[j] > k)
        {
            arr[j + 1] = arr[j];
            j--;
        }

        arr[j + 1] = k;  // Insert k at correct position
    }
}

int main()
{
    int arr[] = {12, 11, 13, 5, 6};
    int n = 5;
    int i;

    insertionSort(arr, n);

    printf("Sorted Array: ");

    for (i = 0; i < n; i++)
    {
        printf("%d ", arr[i]);
    }

    printf("\n");

    return 0;
}