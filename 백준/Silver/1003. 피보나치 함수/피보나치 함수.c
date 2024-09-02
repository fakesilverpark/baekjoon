#include <stdio.h>

void phibo(int a, int b, int n){
    (n!=0)?phibo(b,a+b,n-1):printf("%d %d\n",a,b);
}

int main(void){
    int i,n;
    scanf("%d",&i);
    for (;i!=0;i--){
        scanf("%d",&n);
        (n==0)?printf("1 0\n"):phibo(0,1,n-1);
    }
    return 0;
}