//
//  main.cpp
//  259B
//
//  Created by Alejandro Gleason on 3/8/19.
//  Copyright © 2019 Alejandro Gleason. All rights reserved.
//

#include <iostream>
using namespace std;

int main() {
    int mat[3][3];
    int magicC = 0;
    for(int i = 0; i < 3; i++){//filling the matrix
        for(int j = 0; j < 3; j++){
            cin >> mat[i][j];
            magicC+=mat[i][j];
        }
    }
    //Applying the magic constant formula with some modiffications, in order to know the expected sum
    magicC/=2;
    /*for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            cout << mat[i][j];
        }
        cout << endl;
    }*/
    
    //Calculating the missing components
    mat[0][0] = magicC - mat[0][1] - mat [0][2];
    mat[1][1] = magicC - mat[1][0] - mat [1][2];
    mat[2][2] = magicC - mat[2][0] - mat [2][1];
    
    //printing the matrix
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            cout << mat[i][j] << " ";
        }
        cout << endl;
     }
    
    return 0;
}
