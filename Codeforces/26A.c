//
//  main.c
//  almostPrimes
//
//  Created by Alejandro Gleason on 26/09/18.
//  Copyright © 2018 Alejandro Gleason. All rights reserved.
//

#include <stdio.h>

int isPrime(int n)
{
    int i, flag = 0;
    
    for(i = 2; i <= n-1; ++i)
    {
        // condition for nonprime number
        if(n%i == 0)
        {
            flag = 1;
            break;
        }
    }
    
    if (n == 1)
    {
        return 0;
    }
    else
    {
        if (flag == 0)
            return 1;
        else
            return 0;
    }
    return 0;
}

//Un numero es almost prime si tiene exactamente dos diferentes divisores primos.
int main() {
    int n, acum = 0, aux = 0;
    scanf("%i", &n);
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            if (i%j == 0) {
                if(isPrime(j)==1){
                    acum++;
                }
            }
        }
        if (acum == 2) {
            aux++;
            acum = 0;
        }else if (acum != 2){
            acum = 0;
        }
    }
    printf("%i\n", aux);
    return 0;
}
