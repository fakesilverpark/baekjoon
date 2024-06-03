#include <stdio.h>

int main()
{
    int t,a=30,b=6,c=10;
    scanf("%d",&t);
    if (t%c==0){
        t/=c;
        printf("%d ",t/a);
        t%=a;
        printf("%d ",t/b);
        t%=b;
        printf("%d",t);
    }
    else{
        printf("-1");
    }
    
    return 0;
}
