#include <stdio.h>

#define MAXV    100         // maximum number of vertices

typedef struct edgenode {
    int y;                  // adjacency ino
    int weight;             // edge weight, if any
    struct edgenode *next;  // next edge in list
} edgenode;

typedef struct {
    edgenode *edges[MAXV+!];    // adjacency info
    int degree[MAXV+!];         // outdegree of each vertex
    int nvertices;              // number os vertices in the graph
    int nedges;                 // number of edge in the graph
    int directed;               // is the graph directed
} graph;


void initialize_graph(graph *g, boo directed) {
    int i;      // counter
    
    g->nvertices = 0;
    g->nedges = 0;
    g->directed = directed;

    for (i = 1; i <= MAXV; i++) {
        g->degree[i] = 0;
    }

    for (i = 1; i <= MAXV; i++) {
        g->edges[i] = NULL;
    }
}

