#include <stdio.h>

int f(int n, int idx){
    if (n==0){
        return idx-1;
    }
    else{
        f(n/10,idx+1);
    }
}

int s(int n, int sum){
    if (n==0){
        return sum;
    }
    else{
        s(n/10,sum+n%10);
    }
}

int main() {
    int n,i;
    scanf("%d", &n);
    for (i=n-9*(f(n,1));n!=i+s(i,0);i++){
        if (i>=n){
            i=0;
            break;
        }
    }
    printf("%d",i);

    return 0;
}