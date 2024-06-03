#include <stdio.h>

int main() {
    int n,lef[43]={0,},cnt=0;
    for (int i=0;i!=10;i++){
        scanf("%d",&n);
        lef[n%42]+=1;
    }
    for (int i=0;i!=43;i++){
        if (lef[i]!=0){
            cnt+=1;
        }
    }
    printf("%d",cnt);

    return 0;
}