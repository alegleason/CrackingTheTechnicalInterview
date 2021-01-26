//
//  main.cpp
//  1073B
//
//  Created by Alejandro Gleason on 10/26/19.
//  Copyright © 2019 Alejandro Gleason. All rights reserved.
//

#include <iostream>

using namespace std;

/*Tell him the number of books he will put into his backpack during each step.
 Lo que el problema nos da es un arreglo con las posiciones de los libros, y otro
 arreglo con los libros que se están moviendo, lo que tenemos que hacer es mover el
 libro de acuerdo al paso b(i) y guardar los que esten antes que el en la mochila,
 continuando con todos los libros.
*/
int main() {
    int books, aux;
    
    int* a = NULL;   // Pointer to int, initialize to nothing.
    int* b = NULL;
    int* c = NULL;      // Size needed for array
    cin >> books;   // Read in the size
    a = new int[books];  // Allocate n ints and save ptr in a.
    b = new int[books];  // Allocate n ints and save ptr in a.
    c = new int[books];  // Allocate n ints and save ptr in a.
    
    for (int i = 0; i < books; i++) {
        c[i] = 0;
    }
    
    for (int i = 0; i < books; i++) {
        cin >> aux;
        a[i] = aux;
    }
    
    for (int i = 0; i < books; i++) {
        cin >> aux;
        b[i] = aux;
    }
    
    int pos = 0;
    for (int i = 0; i < books; i++) {
        int x = b[i]; /*current movement*/
        if (c[x] == 1) { /*we are at the top already*/
            cout << 0 << " "; /*no movements to be done*/
            continue;
        }
        
        int cnt = 0;
        while (1) {
            cnt++;
            c[a[pos]] = 1; /*to mark it as already in backpack*/
            if (a[pos] == x) {
                break;
            }
            pos++;/*moving pos*/
        }
        
        pos++;/*moving pos*/
        cout << cnt << " "; /*movements*/
    }
    
   
    delete [] b;  // When done, free memory pointed to by a.
    b = NULL;     // Clear a to prevent using invalid memory reference.
    delete [] c;  // When done, free memory pointed to by a.
    c = NULL;     // Clear a to prevent using invalid memory reference.
    
    return 0;
}
