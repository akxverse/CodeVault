// Student Marks and Grade Program

#include <stdio.h>

int main()
{
    int n, i;
    char name[50][30];
    int marks[50];
    char grade;

    printf("Enter number of students: ");
    scanf("%d", &n);

    // Input student details
    for (i = 0; i < n; i++)
    {

        printf("\nEnter name: ");
        scanf("%s", name[i]);

        printf("Enter marks: ");
        scanf("%d", &marks[i]);
    }

    // Display student details
    printf("\nStudent Details\n");

    for (i = 0; i < n; i++)
    {

        if (marks[i] >= 90)
            grade = 'A';

        else if (marks[i] >= 75)
            grade = 'B';

        else if (marks[i] >= 60)
            grade = 'C';

        else if (marks[i] >= 40)
            grade = 'D';

        else
            grade = 'F';

        printf("\nName  : %s", name[i]);
        printf("\nMarks : %d", marks[i]);
        printf("\nGrade : %c\n", grade);
    }

    return 0;
}
