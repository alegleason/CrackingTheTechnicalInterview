//
//  main.c
//  minesweper
//
//  Created by Alejandro Gleason on 28/08/18.
//  Copyright © 2018 Alejandro Gleason. All rights reserved.
//

#include <stdio.h>
#include <ctype.h>

int main() {
    int n, m, i, j, auxi, auxj, mines, k;
    char matrix[101][101];
    int aroundX[] = {0, 1, 1, 1, 0, -1, -1, -1};
    int aroundY[] = {1, 1, 0, -1, -1, -1, 0, 1};
    scanf("%d %d", &n, &m);
    for (i = 0; i < n; i++) {//Metodo para llenar la fila completa
        scanf("%s", matrix[i]);
    }
    for (i = 0; i < n; i++) {
        for (j = 0; j < m; j++) {
            if (matrix[i][j] == '.') {
                for (k = 0; k < 8; k++) {//k < 8 porque checa los 8 lugares colindantes
                    auxi = i + aroundX[k];
                    auxj = j + aroundY[k];
                    if (auxi < 0 || auxi >= n || auxj < 0 || auxj >= m) {//Nada fuera de lo normal
                        continue;
                    }
                    if (matrix[auxi][auxj] == '*') {
                        printf("NO");
                        return 0;
                    }
                }
            }
            else if (isdigit(matrix[i][j])){
                mines = 0;
                for (k = 0; k < 8; k++) {//k < 8 porque checa los 8 lugares colindantes
                    auxi = i + aroundX[k];
                    auxj = j + aroundY[k];
                    if (auxi < 0 || auxi >= n || auxj < 0 || auxj >= m) {//Nada fuera de lo normal
                        continue;
                    }
                    if (matrix[auxi][auxj] == '*') {
                        ++mines;
                    }
                }
                if (mines != (matrix[i][j] - '0')) {
                    printf("NO");
                    return 0;
                }
            }
        }
    }
    printf("YES");
    return 0;
}
