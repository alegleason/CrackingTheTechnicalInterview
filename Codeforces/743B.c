//
//  main.c
//  vladik2
//
//  Created by Alejandro Gleason on 09/09/18.
//  Copyright © 2018 Alejandro Gleason. All rights reserved.
//

#include <stdio.h>

int main() {
    int n, x, y, z;
    scanf("%i", &n);
    if (n == 1) {
        printf("-1");
        return 0;
    }else{
        x = n;
        y = n + 1;
        z = n*(n+1);
        printf("%i %i %i", x, y, z);
    }
    return 0;
}
