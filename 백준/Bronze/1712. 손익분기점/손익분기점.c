#include <stdio.h>

int main() {
    long long int a,b,c,s;
    scanf("%lld %lld %lld",&a,&b,&c);
    if (b-c==0){
        s=0;
    }
    else{
        s=(-a)/(b-c)+1;
    }
    if (s<=0){
        printf("-1");
    }
    else{
        printf("%d",s);
    }

    return 0;
}