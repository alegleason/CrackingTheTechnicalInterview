//
//  main.cpp
//  467B
//
//  Created by Alejandro Gleason on 3/21/19.
//  Copyright © 2019 Alejandro Gleason. All rights reserved.
//

#include <iostream>
using namespace std;

int main() {
    int* a = NULL;   // Pointer to int, initialize to nothing.
    int n, m, k, res = 0,x,y;//n - types of soldiers, m - players, k - bits to differ
    int binary1[22], binary2[22];//1048576 is the max num to be converted, binary1 is fredors, binary2 are others
    int diff = 0;
    for (int i = 0; i < 22; i ++) {
        binary1[i] = 0;//initializing on 0
    }
    cin >> n >> m >> k;
    a = new int[m+10];  // Allocate n ints and save ptr in a.

    for (int i = 0; i < m + 1; i++){ //m + 1 because of Fedor
        cin >> a[i];//array of numbers
    }
    int aux = a[m];
    //cout << aux << " ";
    for(x=0; aux>0; x++)//x works as i
    {
        binary1[x]=aux%2;
        aux=aux/2;
    }
    //cout<<"Binary of the given (fredors) number= ";
    /*for(x=x-1;x>=0;x--)
    {
        cout<<binary1[x];//binary1 saves fredors number
    }*/
    
    for (int i = 0; i < 22; i ++) {
        binary2[i] = 0;//initializing on 0
    }
    
    //cout << endl;
    while (m > 0) {
        diff = 0;
        int aux = a[m-1];
        //cout << aux << " ";
        //cout << aux << endl;
        for(y=0; aux>0; y++)//x works as i
        {
            binary2[y]=aux%2;//binary 2 is auxiliar
            aux=aux/2;
        }
        
        /*for(y=y-1;y>=0;y--)
        {
            cout<<binary2[y];//binary1 saves fredors number
        }
        cout << endl;*/
        for (int i = 0; i < 22; i++) {
            if (binary1[i] != binary2[i]) {
                diff++;
            }
        }
        //cout << "Found " << diff << " differences" <<endl;
        if (diff <= k) {// if the differences are smaller or equal than the allowed
            res++;
        }
        for (int i = 0; i < 22; i ++) {
            binary2[i] = 0;//initializing on 0
        }
        m--;
    }
    
    cout << res << endl;
    
    delete [] a;  // When done, free memory pointed to by a.
    a = NULL;     // Clear a to prevent using invalid memory reference.
    return 0;
}
