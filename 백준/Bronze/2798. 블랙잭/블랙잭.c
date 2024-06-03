#include <stdio.h>

int main() {
    int n,m,sum,max=0;
    scanf("%d %d",&n,&m);
    int num[n];
    for (int i=0;i!=n;i++){
        scanf("%d",&num[i]);
    }
    for (int i=0;i!=n;i++){
        for (int j=i+1;j!=n;j++){
            for (int l=j+1;l!=n;l++){
                sum=num[i]+num[j]+num[l];
                if ((sum<=m)&&(sum>max)){
                    max=sum;
                }
            }
        }
    }
    printf("%d",max);
    return 0;
}