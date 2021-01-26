//
//  main.cpp
//  archercpp
//
//  Created by Alejandro Gleason on 27/09/18.
//  Copyright © 2018 Alejandro Gleason. All rights reserved.
//
// Geometric progresion https://en.wikipedia.org/wiki/Geometric_progression
// Help: http://codeforces.com/blog/entry/7804

#include <cstdio>

int main(){
    
    int a = 0, b = 0, c = 0, d = 0;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    double first  = 1.0 * a / b;//Parsing to float
    double second = 1.0 * c / d;//Parsing to float
    
    printf("%.10lf\n", (first / (1 - ((1 - first)*(1 - second)))));
    return 0;
}

