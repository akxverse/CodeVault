// Word Counter Program

#include <stdio.h>

int main()
{

    char str[1000];
    int i;
    int characters = 0;
    int words = 1;
    int spaces = 0;

    printf("Enter a sentence:\n");
    fgets(str, sizeof(str), stdin);

    for (i = 0; str[i] != '\0'; i++)
    {

        characters++;

        if (str[i] == ' ')
        {
            spaces++;
            words++;
        }
    }

    printf("\nCharacters : %d", characters - 1);
    printf("\nWords      : %d", words);
    printf("\nSpaces     : %d\n", spaces);

    return 0;
}