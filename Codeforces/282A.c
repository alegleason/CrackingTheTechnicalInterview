//
//  main.c
//  Bit++
//
//  Created by Alejandro Gleason on 11/10/17.
//  Copyright © 2017 Alejandro Gleason. All rights reserved.
//

#include <stdio.h>

int main() {
    int n, i, x = 0;
    char equis [3];
    scanf("%i", &n);
    for (i = 0; i<n;i++){
    scanf("\n%c%c%c", &equis[0], &equis[1], &equis[2]);
    if (equis [1] == '+')
        x++;
    else
        x--; }
    printf("%i\n", x);
    return 0;
}
