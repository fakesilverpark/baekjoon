#include <stdio.h>

int main() {
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    printf("%d\n", a+b-c);
    int num=(b>=10 && b%10==0)?b+1:b;
    for (int i=1;num!=0;i++){
        num/=10;
        a*=10;
    }
    printf("%d", a+b-c);

    return 0;
}