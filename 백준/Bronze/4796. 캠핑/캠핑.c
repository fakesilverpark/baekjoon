#include <stdio.h>

int main() {
    int l,p,v,idx=0;
    while (1){
        scanf("%d %d %d",&l,&p,&v);
        if (l==0 && p==0 && v==0){
            break;
        }
        else{
            printf("Case %d: %d\n",idx+1,((v/p)*l)+((v%p>l)?l:v%p));
            idx+=1;
        }
    }

    return 0;
}