//
//  main.cpp
//  Hongcow
//
//  Created by Alejandro Gleason on 06/10/18.
//  Copyright © 2018 Alejandro Gleason. All rights reserved.
//


#include <iostream>
#include <set>
using namespace std;
int main()
{
    string ch;
    cin>>ch;
    int length=ch.size();
    int n=length;
    string st;
    set<string> W;//Set that contains strings
    while(length--)//While there is content
    {
        char temp=ch[n-1];
        for(int i=n-1;i>0;i--)
        {
            ch[i]=ch[i-1];
        }
        ch[0]=temp;
        W.insert(ch);
    }
    cout<<W.size();
    
    return 0;
}

/*abcd
while {
    length = 3
    temp = ‘d’
    i = 3; i > 0; i — {
        abcc
        abbc
        aabc
    }
    dabc
}*/

