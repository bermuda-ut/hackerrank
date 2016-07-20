// https://www.hackerrank.com/challenges/kangaroo
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

void intswap(int *a, int *b) {
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

int main() {
    int x1, v1, x2, v2; 
    scanf("%d %d %d %d",&x1,&v1,&x2,&v2);

    if(v2 > v1) {
    	intswap(&x1, &x2);
    	intswap(&v1, &v2);
    }

    while(x1 <= x2) {
    	if(x1 == x2) {
    		printf("YES");
    		return 0;
    	}
    	x1 += v1;
    	x2 += v2;
    }

    printf("NO");
	return 0;
}