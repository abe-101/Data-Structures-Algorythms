#include <stdio.h>

#define SIZE sizeof(a) / sizeof(a[0])

void move_zeros_to_beginning(int a[], int n);
void swap(int *p, int *q);

int main(void)
{
    int a[] = {4, 2, 0, 1, 0, 3, 0};

    printf("Original array: ");
    for (int i = 0; i < SIZE; i++)
        printf("%d ", a[i]);

    printf("\n");
    move_zeros_to_beginning(a, SIZE);

    printf("Modified array: ");
    for (int i = 0; i < SIZE; i++)
        printf("%d ", a[i]);
    
    printf("\n");
    return 0;
}
    

void move_zeros_to_beginning(int a[], int n)
{
    int boundary = 0;
    for (int i = 0; i < n; i++) {
        if (a[i] == 0) {
            swap(&a[i], &a[boundary]);
            boundary++;
        }
    }
}

void swap(int *p, int *q)
{
    int temp = *p;
    *p = *q;
    *q =temp;
}
