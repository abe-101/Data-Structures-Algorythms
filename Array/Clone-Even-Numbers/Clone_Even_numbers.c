#include <stdio.h>

#define SIZE sizeof(a) / sizeof(a[0])

int *clone_even_numbers(int* a, int n);
int get_last_number(int* a, int n);

int main(void)
{
    int a[] = {1,2,3,4,-1,-1};
    printf("Before cloning even numbers\nArray a: ");
    for (int i = 0; i < SIZE; i++) {
        printf("%d ", a[i]);
    }

    clone_even_numbers(a, SIZE);
    printf("\nAfter cloning even numbers\nArray a: ");
    for (int i = 0; i < SIZE; i++) {
        printf("%d ", a[i]);
    }
    printf("\n");
    return 0;
}

int *clone_even_numbers(int* a, int n)
{
    int end = n, i = get_last_number(a, n);
    while (i >= 0) {
        if (a[i] % 2 == 0) {
            a[--end] = a[i];
        }
        a[--end] = a[i];
        i--;
    }
    return a;
}


int get_last_number(int* a, int n)
{
    int i = n -1;
    while ( i >= 0 && a[i] == -1) {
        i--;
    }
    return i;
}

