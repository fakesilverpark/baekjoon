#include <stdio.h>

int f(int n, int idx){
    if (idx==0){
        return n;
    }
    else{
        f(n*idx,idx-1);
    }
}

int main() {
    int n, k;
    scanf("%d %d",&n ,&k);
    printf("%d",f(1,n)/(f(1,n-k)*f(1,k)));

    return 0;
}