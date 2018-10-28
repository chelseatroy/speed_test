#include <stdio.h>
#include <stdlib.h>

typedef struct Collection {
    int     size;
    float   data[2000][2000];
} Collection;

void multiply(Collection *a, Collection *b, Collection *output, int x_dim, int y_dim) {
    int i,j;

    for (i = 0; i < x_dim; ++i) {
        for (j = 0; j < y_dim; ++j) {
            output->data[i][j] = a->data[i][j] * b->data[i][j];
        }
    }
}