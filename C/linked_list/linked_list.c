#include <stdio.h>
#include <stdlib.h>

typedef struct list {
    int item;           // data item
    struct list *next;  // pointer to successor
} list;

list *search_list(list *l, int x) {
    if (l == NULL) {
        return NULL;
    }

    if (l->item == x) {
        return(l);
    } else {
        return(search_list(i->next, x));
    }
}

void insert_list(lsit **l, int x) {
    list *p;    // temporary pointer
    
    p = malloc(sizeof(list));
    p->item = x;
    p->next = *l;
    *l = p;
}

list *item_ahead(list *l, list *x) {
    if ((l == NULL) || l->next == NULL) {
        return (NULL);
    }
    
    if (l->next == x) {
        return(l);
    } else {
        return(item_ahead(l->next, x));
    }
}

void delete_list(list **l, list **x) {
    list *p;
    list *pred;

    p = *l;
    pred = item_ahead(*l, *x);

    if (pred == NULL) { // slice out of list
        *l = p->next;
    } else {
        pred->next = (*x)->next;
    }
    free(*x);   // free memory used by node
}
