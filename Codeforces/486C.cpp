//
//  main.cpp
//  486C
//
//  Created by Alejandro Gleason on 2/11/19.
//  Copyright © 2019 Alejandro Gleason. All rights reserved.
//

#include <iostream>
#include <math.h>
using namespace std;

int main() {
    int n, pos, mid, izq = 0, der = 0, ups = 0, sides = 0;
    string pal;
    cin >> n >> pos;
    cin >> pal;
    
    //converting to 0-based-index
    pos--;
    n--;
    
    //choosing which side are we staying with
    if(pos > (n-pos)){
        pos = n-pos;
    }
    
    //saving the middle pos of the word
    mid = n/2;
    
    //initializing der and izq on pos
    der = pos;
    izq = pos;
    
    for(int i = pos; i <= mid; i++){//from initial post to mid
        if(pal[i] != pal[n - i]){//saving which pos we need to move, in case there is difference
            der = i;
        }
    }
    
    for(int i = pos; i >= 0; i--){
        if(pal[i] != pal[n - i]){
            izq = i;
        }
    }
    
    //determining side movements
    if ((pos - izq) + (der - izq) < (der - pos) + (der - izq)) {
        sides = (pos - izq) + (der - izq);//moving from right to left
    }else{
        sides = (der - pos) + (der - izq);//moving from left to right
    }

    //determining the changing elements (up and down arrow)
    for(int i = izq; i <= der; i++){
        if(abs(pal[i] - pal[n - i]) < 26 - abs(pal[i] - pal[n - i])){
            ups += abs(pal[i] - pal[n - i]);//case when is better to move on the normal course of the abecedary
        }else{
            ups += 26 - abs(pal[i] - pal[n - i]);//case when is better to move towards the end of the abecedary
        }
    }
    
    cout << (ups+sides);//sum of ups-downs and sides(izq, der) movements
    
    return 0;
}
