//
//  main.cpp
//  Concurso
//
//  Created by Alejandro Gleason on 4/6/19.
//  Copyright © 2019 Alejandro Gleason. All rights reserved.
//

#include <iostream>
#include<string.h>
#include <string>
#include <algorithm>
using namespace std;

int main(){
    /*char str[101], temp, str2[101];
    int flag=0;
    string c1, c2, c3;
    int i, j;
    gets(str);
    gets(str2);
    j = strlen(str) - 1;
    for (i = 0; i < j; i++,j--)
    {
        temp = str[i];
        str[i] = str[j];
        str[j] = temp;
    }
    //cout << "\nAl reves: " << str;
    cin >> c1;
    cin >> c2;
    if(c2 == c3){//c3 is the reversed I calculated, c2 is the reversed given
        cout << "YES";
    }else{
        cout << "NO";
    }
    for (i = 0; i < j; i++)
    {
        if (str2[i] == str[i]) {
            flag = 0;
        }else{
            flag=1;
            cout << "NO";
            return 0;
        }
    }
    //cout << j;
    //cout << str[0];
    //cout << str2[0];
    if(j == 0 && (str[0] != str2[0])){
        cout <<"NO";
        return 0;
    }
    if (flag==0) {
        cout << "YES";
    }else{
        cout<<"NO";
    }*/
    string c1, c2;
    cin >> c1 >> c2;
    reverse(c2.begin(), c2.end());//Reverses the order of the elements in the range [first,last)
    if (c1 == c2) {
        cout << "YES";
    }else{
        cout << "NO";
    }
    return 0;
}
