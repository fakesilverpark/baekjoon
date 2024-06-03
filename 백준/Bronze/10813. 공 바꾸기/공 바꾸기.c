#include <stdio.h>

int main() {
    int n,m;
    scanf("%d %d",&n,&m);
    int balls[n];
    int i,j;
    int temp;
    for (int i=0;i!=n;i++){
        balls[i]=i+1;
    }
    for (int l=m;l!=0;l--){
        scanf("%d %d",&i,&j);
        temp=balls[j-1];
        balls[j-1]=balls[i-1];
        balls[i-1]=temp;
    }
    for (int i=0;i!=n;i++){
        printf("%d ",balls[i]);
    }

    return 0;
}