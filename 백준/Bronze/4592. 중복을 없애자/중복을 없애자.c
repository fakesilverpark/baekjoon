#include <stdio.h>

int main() {
    int n=1,N,l=0;
    while (1){
        scanf("%d",&n);
        if (n==0){
            break;
        }
        int num[n];
        for (int i=0;i!=n;i++){
            scanf("%d",&N);
            num[i]=(l==N)?0:N;
            l=N;
        }
        for (int i=0;i!=n;i++){
            if (num[i]!=0){
                printf("%d ",num[i]);
            }
        }
        printf("$\n");
        l=0;
    }

    return 0;
}