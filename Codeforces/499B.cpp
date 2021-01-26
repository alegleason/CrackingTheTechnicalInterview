//
//  main.cpp
//  499B
//
//  Created by Alejandro Gleason on 2/7/19.
//  Copyright © 2019 Alejandro Gleason. All rights reserved.
//
// how do maps work? https://www.geeksforgeeks.org/map-associative-containers-the-c-standard-template-library-stl/

#include <iostream>
#include <iostream>
#include <iterator>
#include <map>
using namespace std;

int main() {
    map<string, string> dic;// empty map container, dic stands for dictionary
    int n = 0, m = 0; //n is number of words dictated and m are the lines (i)
    string ai, bi; //ai and bi are the words scanned
    cin >> n >> m;
    
    while (m--) {//while there is content on the lines (determined by 'm')
        cin >> ai >> bi;
        if(ai.length()>bi.length())//We save the word that is smaller in our 'dictionary'
            dic[ai] = bi;
        else{
            dic[ai] = ai;
        }
    }
    
    while (n--) {//while there is something to print (determined by 'n', which is the number of words that the professor will say)
        cin >> ai;//adding the new word
        cout << dic[ai] << " ";//dictionary will throw the smaller 'ai' word, which was already saved
    }
    return 0;
}
