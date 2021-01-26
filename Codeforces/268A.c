//
//  main.c
//  268A
//
//  Created by Alejandro Gleason on 4/6/19.
//  Copyright © 2019 Alejandro Gleason. All rights reserved.
//


#include <stdio.h>

int main() {
    int n, unilocal[50], univisitante[50], res = 0, i, j;
    scanf("%i", &n);
    for(i = 0; i<n; i++){
        scanf("%i %i", &unilocal[i], &univisitante[i]);
    }
    for(i = 0; i<n; i++){
        for(j = 0; j<n; j++){
            if(unilocal[i] == univisitante[j]){
                res++;
            }
        } // se incrementa j
    } // se incrementa i
    printf("%i\n", res);
    return 0;
}
