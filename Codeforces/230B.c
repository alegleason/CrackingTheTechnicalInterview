#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int isPrime(long long num){
    long long raiz = sqrt(num);//Al hacer la raiz, se reduce lo que se tiene que revisar
    if(num < 2){
        return 0;
    }
    else if(num == 2){//El dos es un num primo
        return 1;//true
    }
    if(num%2 == 0){
        return 0;
    }
    for(int j = 3; j <= raiz; j +=2){//Si hay cualquier incidencia, el numero ya no es primo
        if(num%j == 0){
            return 0;//fale
        }
    }
    return 1;//true
}
int main(){
    long long n, num;
    scanf("%lld", &n);
    for (int i = 0; i < n; i++) {
        scanf("%lld", &num);
        int raiz = sqrt(num);
        if(pow(raiz,2)==num && (isPrime(raiz) == 1)){
            printf("YES\n");
        } else {
           printf("NO\n");
        }
    }
    return 0;
}
