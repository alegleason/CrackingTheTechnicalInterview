//
//  main.cpp
//  600B
//
//  Created by Alejandro Gleason on 8/25/19.
//  Copyright © 2019 Alejandro Gleason. All rights reserved.
//

#include <iostream>
#include <algorithm>

using namespace std;

int main(int argc, const char * argv[]) {
    ios_base::sync_with_stdio (true);//quickness
    int sizeA, sizeB, aux = 0, count = 0, low, high, mid, flag = 0;
    int* a = NULL;   // Declare both arrays dinamically
    int* b = NULL;   // Pointer to int, initialize to nothing.
    
    cin >> sizeA >> sizeB;        // Read in the size
    a = new int[sizeA];  // Allocate n ints and save ptr in a.
    b = new int[sizeB];
    
    for (int i=0; i<sizeA; i++) {
        cin >> aux;
        a[i] = aux;    // Initialize all elements to zero.
    }
    
    sort(a, a+sizeA);
    
    for (int i=0; i<sizeB; i++) {
        cin >> aux;
        b[i] = aux;    // Initialize all elements to zero.
    }
    
   
    
    for(int i = 0; i <sizeB; i++){
        low = 0;
        flag = 0;
        high = sizeA-1;
        count = 0;
        while (low <= high) {
            flag = 0;
            mid = (high+low)/2;
            //not search on not needed parts
            if (a[mid] <= b[i]) {
                low = mid + 1; //reallocate low
                count = low;
                flag = 1;// turn on flag to know ive entered here
            } else if (a[mid] > b[i] && flag == 1) {
                break;//since we've already check smallers, we dont have to keep checking
            } else if(a[mid] > b[i] && flag == 0) {
                high = mid - 1;//reallocate high, we have not entered here
            }
        }
         cout << count << " ";
    }
 
    
    /*
     
     DOES NOT SOLVES ON TIME
     
    for (int i = 0; i<sizeB; i++) {
        count = 0;
        for (int j = 0; j<sizeA; j++) {
            if (a[j]<=b[i]) {
                count++;
            }
        }
        cout << count << " ";
    }*/
    
    delete [] a;  // When done, free memory pointed to by a.
    a = NULL;     // Clear a to prevent using invalid memory reference.
    delete [] b;
    b = NULL;

    return 0;
}
