//
//  main.c
//  VanyaFence
//
//  Created by Alejandro Gleason on 01/09/17.
//  Copyright © 2017 Alejandro Gleason. All rights reserved.
//

#include <stdio.h>

int main() {
    int a, b, s=0;
    scanf("%i %i", &a, &b);
    while (a<=b) {
        a = (3*a);
        b = (2*b);
        s = s+1;
    }
    printf("%i", s);
    return 0;
}
