#include <stdio.h>
#include <string.h>

void selection_sort(char s[], int n);
void swap(char *p, char *q);


int main(void)
{
    char word[] = {"fedcba"};

    printf("Before sorting: ");
    printf("%s\n", word);

    selection_sort(word, strlen(word));
    
    printf("After sorting: ");
    printf("%s\n", word);
    
    return 0;
}

void selection_sort(char s[], int n) {
    int i, j;   // counters
    int min;    // index of minimun

    for (i = 0; i < n; i++) {
        min = i;
        for (j = i + 1; j < n; j++) {
            if (s[j] < s[min]) {
                min = j;
            }
        }
        swap(&s[i], &s[min]);
    }
}

void swap(char *p, char *q)
{
    char temp = *p;
    *p = *q;
    *q =temp;
}


