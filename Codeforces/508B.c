//
//  main.c
//  508B
//
//  Created by Alejandro Gleason on 2/7/19.
//  Copyright © 2019 Alejandro Gleason. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char s[100001];
    int flag = 0;
    gets(s);
    int size = strlen(s);
    int num = atoi(s);
    int n2=num;
    int count=0;
    char aux3;
    //For checking each odd digit
    while (n2!=0){
        if((n2%10)%2==0){
            count++;
        }
        n2=n2/10;
    }
    if(count==0){
        printf("-1");
        return 0;
    }
    
    char aux = s[size-1];
   // printf("%c\n", aux);
    for (int i = size-2; i >= 0; i--) {
        int aux2 = (int)s[i]-48;
        //printf("%i\n", aux2);
        //printf("%c\n", s[i]);
        if (s[i] < aux && (aux2%2 == 0)) {
            //printf("%c", s[i]);
          aux3 = s[i];
            s[i] = aux;
            s[size-1] = aux3;
            printf("%s", s);
            return 0;
        }
    }
    
    for (int i = 0; i < size-2; i++) {
        int aux2 = (int)s[i]-48;
        if (s[i] > aux && (aux2%2 == 0)) {
            //printf("%c", s[i]);
            aux3 = s[i];
            s[i] = aux;
            s[size-1] = aux3;
            printf("%s", s);
            return 0;
        }
    }
    
    return 0;
}
