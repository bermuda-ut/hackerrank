// https://www.hackerrank.com/challenges/angry-professor/

#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    int t; 
    scanf("%d",&t);

    for(int a0 = 0; a0 < t; a0++){
        int n, k; 

        scanf("%d %d", &n, &k);

        int wtv, c = 0;
        for(int a_i = 0; a_i < n; a_i++){
	        scanf("%d",&wtv);
	        if(wtv <= 0)
	        	c++;
        }

        if(c < k)
        	printf("YES\n");
        else
        	printf("NO\n");
    }
    return 0;
}