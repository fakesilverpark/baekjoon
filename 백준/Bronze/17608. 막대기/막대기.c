#include <stdio.h>

int main() {
    int n,m,cnt=0;
    scanf("%d",&n);
    int sti[n];
    for (int i=0;i!=n;i++){
        scanf("%d",&sti[i]);
    }
    m=sti[-1];
    for (int i=n;i!=0;i--){
        if (sti[i-1]>m){
            cnt+=1;
            m=sti[i-1];
        }
    }
    printf("%d\n",cnt);

    return 0;
}