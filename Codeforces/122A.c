//
//  main.c
//  122A
//
//  Created by Alejandro Gleason on 2/7/19.
//  Copyright © 2019 Alejandro Gleason. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char s[1001];
    int flag = 0;
    gets(s);
    //scanf("%s", s);
    int size = strlen(s);
    for (int i = 0; i < size; i++) {
        if (s[i] == '4' || s[i] == '7') {
        }else{
            flag = 1;
        }
    }
    
    if (flag == 0) {
        printf("YES");
        return 0;
    }
    
    int num = atoi(s);
    
    if ((num%7 == 0) || (num%4 == 0) || (num%47 == 0) || (num%74 == 0)|| (num%447 == 0) || (num%474 == 0) || (num%477 == 0) || (num%774 == 0) || (num%747 == 0) || (num%744 == 0)){
        printf("YES");
    }else{
        printf("NO");
    }
    
    //printf("%i", num);
    return 0;
}
