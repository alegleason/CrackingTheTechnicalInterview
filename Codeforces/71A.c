//
//  main.c
//  TooLongW
//
//  Created by Alejandro Gleason on 29/10/17.
//  Copyright © 2017 Alejandro Gleason. All rights reserved.
//

#include <stdio.h>
#include <string.h>

int cuenta (char array [100]);

int main()
{
    int pruebas, longitud;
    scanf ("%i", &pruebas);
    char palabra [100];
    while (pruebas > 0) {
        scanf ("%s", palabra);
        longitud = cuenta(palabra);
        if (longitud > 10) {
            printf ("%c%d%c\n", palabra[0], longitud - 2, palabra[longitud - 1]);
        } else {
            printf ("%s\n", palabra);
        }
        pruebas--;
    }
    
    return 0;
}

int cuenta (char array [100]){
    int i = 0;
    while (array[i] != '\0') {
        i++;
    }
    return i;
}
