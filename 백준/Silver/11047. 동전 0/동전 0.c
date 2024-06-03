#include <stdio.h>

int main() {
    int n,m,cnt=0;
    scanf("%d %d",&n,&m);
    int money[n];
    for (int i=0;i!=n;i++){
        int z;
        scanf("%d",&z);
        if (z<=m){
            money[i]=z;
        }
        else{
            money[i]=0;
        }
    }
    for (int i=n-1;i!=0;i--){
        if (money[i]!=0){
            cnt+=m/money[i];
            m%=money[i];
        }
    }
    if (m!=0){
        cnt+=(m/money[0]);
    }
    printf("%d",cnt);
    return 0;
}