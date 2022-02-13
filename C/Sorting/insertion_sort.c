#include <stdio.h>
#include <string.h>

void insertion_sort(char s[], int n);
void swap(char *p, char *q);


int main(void)
{
    char word[] = {"fedcba"};

    printf("Before sorting: ");
    printf("%s\n", word);

    insertion_sort(word, strlen(word));
    
    printf("After sorting: ");
    printf("%s\n", word);
    
    return 0;
}

void insertion_sort(char s[], int n) {
    int i, j;   // counters

    for (i = 1; i < n; i++) {
        j = i;
        while ((j > 0) && (s[j] < s[j - 1])) {
            swap(&s[j], &s[j - 1]);
            j = j-1;
        }
    }
}

void swap(char *p, char *q)
{
    char temp = *p;
    *p = *q;
    *q =temp;
}


