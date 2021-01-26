//
//  main.cpp
//  602A
//
//  Created by Alejandro Gleason on 2/11/19.
//  Copyright © 2019 Alejandro Gleason. All rights reserved.
//

#include <iostream>

using namespace std;

int main(){
    long long num,b,x=0,dig,y=0;
    
    cin >> num >> b;
    while(num > 0){
        cin >> dig;
        x = x*b;
        x = x+dig;
        num--;
    }
    
    cin >> num >> b;
    while(num > 0){
        cin >> dig;
        y = y*b;
        y = y+dig;
        num--;
    }
    
    if(x==y)
        cout << "=" << endl;
    else if(x<y)
        cout << "<" << endl;
    else if(x>y)
        cout << ">" << endl;
}
