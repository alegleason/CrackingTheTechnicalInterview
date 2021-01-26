//
//  main.cpp
//  BearStrings
//
//  Created by Alejandro Gleason on 03/11/18.
//  Copyright © 2018 Alejandro Gleason. All rights reserved.
//
#include <iostream>
using namespace std;
int main()
{
    string s;
    unsigned long count = 0;
    cin >> s;
    for(int i = 0;i < s.size(); i++)
    {//bearbtear
        int find = (s.substr(i)).find("bear");
        cout<<find<<" "<<s.substr(i).size()<<endl;
        if(find != -1){//true
            count = count + s.substr(i).size() - find - 3;
        }
    }
    cout<<count<<endl;
    return 0;
}
