#include <stdio.h>

#define SIZE sizeof(a) / sizeof(a[0])

void dutch_national_flag(int a[], int pivot, int n);
void swap(int *p, int *q);

int main(void)
{
    int a[] = {5,2,4,4,6,4,4,3}, pivot = 4;

    printf("Original array: ");
    for (int i = 0; i < SIZE; i++)
        printf("%d ", a[i]);

    printf("\n");
    dutch_national_flag(a, pivot, SIZE);

    printf("Modified array: ");
    for (int i = 0; i < SIZE; i++)
        printf("%d ", a[i]);
    
    printf("\n");
    return 0;
}
    

void dutch_national_flag(int a[], int pivot, int n)
{
    int low_boundary = 0, high_boundary = n - 1, i = 0;

    while(i <= high_boundary) {
        if (a[i] < pivot) {
            swap(&a[i], &a[low_boundary++]);
            i++;
        } else if (a[i] > pivot) {
            swap(&a[i], &a[high_boundary--]);
        } else {  // eaual to pivot
            i++;
        }
    }
}

void swap(int *p, int *q)
{
    int temp = *p;
    *p = *q;
    *q =temp;
}
