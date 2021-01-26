//
//  main.cpp
//  620A
//
//  Created by Alejandro Gleason on 3/7/19.
//  Copyright © 2019 Alejandro Gleason. All rights reserved.
//

#include <iostream>
using namespace std;

int main() {
    int x1,y1;
    int x2,y2;
    cin>>x1>>y1;
    cin>>x2>>y2;
    int distx=abs(x2-x1);
    int disty=abs(y2-y1);
    int steps=0;
    if(distx==disty){
        steps+=distx;
    }else if(distx>disty){
        steps+=distx; //Los moviminetos de la distancia larga y en ella se incluyen los de la corta (el robot se mueve en ambas direcciones en 1 paso)
    }else{
        steps+=disty; //Los moviminetos de la distancia larga y en ella se incluyen los de la corta (el robot se mueve en ambas direcciones en 1 paso)
    }
    cout << steps;
    return 0;
}

