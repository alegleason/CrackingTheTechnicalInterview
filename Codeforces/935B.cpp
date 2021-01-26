// https://github.com/MathProgrammer/CodeForces/blob/master/Explanations/Explanations%2020/Fafa%20and%20the%20Gates%20Explanation.txt
//  main.cpp
//  Fafa
//
//  Created by Alejandro Gleason on 11/3/18.
//  Copyright © 2018 Alejandro Gleason. All rights reserved.
//

#include <iostream>
using namespace std;

int main()
{
    int noSteps;
    string steps;
    cin >> noSteps >> steps;//how many steps and string
    
    int x = 0, y = 0, coins = 0;
    
    if(noSteps == 1){
        cout << 0;
        return 0;
    }else{
        for(int i = 0; i < noSteps - 1; i++)
        {
            if(steps[i] == 'U'){
                y++;
            }
            if(steps[i] == 'R'){
                x++;
            }
            coins = coins + (x == y && (steps[i] == steps[i + 1]));//True = 1, false = 0
        }
        cout << coins;
        return 0;
    }
}
