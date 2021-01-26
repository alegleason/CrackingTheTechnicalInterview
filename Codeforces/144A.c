//
//  main.c
//  144A
//
//  Created by Alejandro Gleason on 1/25/19.
//  Copyright © 2019 Alejandro Gleason. All rights reserved.
//

#include <stdio.h>

int main() {
    int n, res, num = 0, maxVal = 0, minVal=100, maxInd = 0, minInd = 0;
    scanf("%i", &n);
    for (int i = 0; i < n; i++) {
        scanf("%i", &num);
        if(num > maxVal){
            maxInd = i;//Guardamos el índice
            maxVal = num;//Guardamos el valor
        }
        if(num <= minVal){
            minInd = i;//Hacemos lo mismo para el caso del menor
            minVal = num;
        }
    }
    
    if (maxInd > minInd) {
        res = (maxInd-1) + (n-minInd)-1;
    }else{
        res = (maxInd-1) + (n-minInd);
    }
    printf("%i", res);
    return 0;
}
