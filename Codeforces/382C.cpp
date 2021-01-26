//
//  main.cpp
//  382C
//
//  Created by Alejandro Gleason on 3/13/19.
//  Copyright © 2019 Alejandro Gleason. All rights reserved.
//

/*1) If n = 1, the answer is -1. Because of any two numbers is arithmetical progression.
2) If array is constant, the answer if that constant.
3) If you have arithmetical progression initially, you can compute its difference d. In this case you should just to output minVal - d, and maxVal + d, where minVal is minimum value among a[i], and maxVal is maximum value among a[i]. But in case of n = 2, also you should check (a[0] + a[1]) / 2. If this number is integer, it is needed to be output.
4) Else, the answer has at most one integer. You find this integer you should sort the sequence, and find the place where the number is missed. If such a place exists you should add the corresponding number to the sequence, else, the answer is 0.
5) In all other cases the answer is 0.*/

#include <iostream>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int* a = NULL;   // Pointer to int, initialize to nothing.
    int n, aux, dif = 0, ct = 0, difAux = 0, mistakesCnt = 0, indexCnt = 0;           // Size needed for array
    cin >> n;        // Read in the size
    a = new int[n];  // Allocate n ints and save ptr in a.
    for (int i=0; i<n; i++) {
        cin >> aux;
        a[i] = aux;    // Initialize all elements
    }
    // Use a as a normal array
    /*for (int i=0; i<n; i++) {
        cout << a[i];
    }*/
    
    sort(a,a+n); //Sort ascending
    
    if(n==1){
        cout << -1 << endl;
        return 0;
    }else if(n==2){//Any two numbers is arithmetical progression
        dif=a[1]-a[0];
        if (dif == 0) { //We are talking about the same number
            cout << 1 << endl <<a[0];
        }else if(dif%2 == 0){ //In case we have an even difference
            cout << 3 << endl; //Left side
            ct = a[0]-dif;
            cout << ct << " "; //Half
            ct = a[0]+dif/2;
            cout << ct << " ";
            ct = a[1]+dif;
            cout << ct; //Right side
        }else if(dif%2 != 0){ //In case we have an uneven difference
            cout << 2 << endl;
            ct = a[0]-dif;
            cout << ct <<endl; //Left side
            ct = a[1]+dif;
            cout << ct <<endl; //Right side
        }
    }
    else if (n>=3){ //Last case
        dif = a[1] - a[0];
        for(int i = 1; i < n; i++){ // Getting the min diff
            difAux = a[i]-a[i-1];
            dif = min(difAux,dif);
        }
        for(int i = 1; i < n; i++){ // Retrieving the amount of times where the diff isnt the minimum and saving the index
            if(a[i] - a[i-1] != dif){
                indexCnt = i;
                mistakesCnt++;
            }
        }
        // Repeated values
        if(mistakesCnt == 0 && dif == 0){
            cout<< 1 << endl << a[0];
        }
        // Equally spaced sequence
        else if(mistakesCnt == 0 && dif != 0){
            cout << 2 << endl;
            ct = a[0] - dif;
            cout << ct << " "; //izq
            ct = a[n-1] + dif;
            cout << ct; //der
        }else if(mistakesCnt == 1 && (a[indexCnt] - a[indexCnt-1] == (2*dif))){// Double difference
            cout << 1 << endl;
            ct = a[indexCnt-1] + dif;
            cout << ct;
        }else{//Unsolvable
            cout << 0;
        }
    }else{ //Impossible
        cout << -1 << endl;
    }
    delete [] a;  //When done, free memory pointed to by a.
    a = NULL;     //Clear a to prevent using invalid memory reference.
    return 0;
}
