//
//  main.cpp
//  SerejaAndDima
//
//  Created by Alejandro Gleason on 06/10/18.
//  Copyright © 2018 Alejandro Gleason. All rights reserved.
//

#include <iostream>
using namespace std;

int main()
{
    //Creating the array with dynamic memory
    unsigned int size;
    cin >> size;
    int *cards = NULL;
    cards = new int[size];//POR QUE NO HACER LO DE scan size y asignar cards[size]
    
    int left = 0, right = (size - 1), sereja = 0, dima = 0, turn = 0;
   
    
    for (int i = 0; i < size; i++)
        cin >> cards[i];
    
    while (left < right + 1)
    {
        turn++;
        if (cards[left] > cards[right])
        {
            if (turn%2 == 1){
                sereja = sereja + cards[left];
            }
            else{
                dima = dima + cards[left];
            }
            left++;//Moving 1 space to the right side
        }
        else
        {
            if (turn%2 == 1){
                sereja = sereja + cards[right];
            }
            else{
                dima = dima + cards[right];
            }
            right--;//Moving 1 space to the left side
        }
    }
    cout << sereja << " " << dima << endl;
    return 0;
}
