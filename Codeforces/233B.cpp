
//
//  main.cpp
//  equation
//
//  Created by Alejandro Gleason on 10/10/18.
//  Copyright © 2018 Alejandro Gleason. All rights reserved.
//

#include <iostream>
#include <string>
#include <cctype>
#include <cmath>
#include <sstream>


using namespace std;

long long sum(string st){
    unsigned long size = st.size();
    long long sum = 0;
    for (unsigned long i = 0; i < size; i++) {
        sum = sum + (st[i]-'0');
    }
    return sum;
}



int main() {
    string n;
    long long aux;
    
    cin >> aux;
    n = to_string(aux);
    long long res = 0, in, square;
    string aux2;
    
    for (int i = 0; i <= 90; i++) {
        in = (i*i) + (4*aux);//inside
        square = sqrt(in);
        if(square*square == in){//Raiz cuadrada perfecta
            res = (-i+square)/2;
            aux2 = to_string(res);
            if (res >= 0 && sum(aux2) == i){
                cout << res;
                return 0;
            }
        }
    }
    cout << "-1";
    return 0;
}

