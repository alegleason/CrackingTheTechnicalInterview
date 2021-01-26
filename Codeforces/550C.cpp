//
//  main.cpp
//  550C
//
//  Created by Alejandro Gleason on 4/8/19.
//  Copyright © 2019 Alejandro Gleason. All rights reserved.
//

#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(true);//quickness
    bool ans = false;//flag
    int answer, first = 0, sec = 0, third = 0, probnum = 0;//first, sec and third will be the possible digits, prob num is the probable number with modifications
    string num; //since we will perform moving operations it is better to treat it as an string
    cin >> num;
    unsigned int size = num.size();
    //case for 1 length
    for (unsigned int i = 0; i < size && !ans; i++) {
        if (num[i] == '8' || num[i] == '0') {
            ans = true;
            answer = num[i] - '0';//parsing to real number
        }
    }
    
    //case for 2 length
    for(unsigned int i = 0; i < size && !ans; i++)
    {
        for(unsigned int j = i + 1; j < size && !ans; j++)
        {
            first = num[i] - '0';
            sec = num[j] - '0';
            
            probnum = 10*first + 1*sec;
            
            if(probnum%8 == 0){
                answer=probnum;
                ans = true;
        }
    }
    }
    
    //case for 2 length
    //in this for we will convert all digits
    for (unsigned int i = 0; i < size && !ans; i++) {//better to have the validation of ans on the for, skips unnecesary comparations
        for (unsigned int j =i+1; j < size && !ans; j++) {
            for (unsigned int k = j+1; k<size; k++) {
                first=num[i] - '0';//parsing to the real num
                sec=num[j] - '0';
                third=num[k] - '0';
                probnum=100*first + 10*sec+ 1*third;//formatting the number
                if(probnum%8 == 0){//valid
                    answer=probnum;
                    ans = true;
                }
            }
        }
    }
    
    if (ans) {
        cout << "YES" << endl << answer;
    }else{
        cout << "NO";
    }
    
    return 0;
}
