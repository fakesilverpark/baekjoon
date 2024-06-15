#include <stdio.h>

int main() {
    int n, T[6], t, p, sum=0;
    scanf("%d", &n);
    for (int i=0;i!=6;i++){
        scanf("%d",&T[i]);
    }
    scanf("%d %d", &t, &p);
    for (int i=0;i!=6;i++){
        if (T[i]<=t && T[i]!=0){
            sum+=1;
        }
        else if (T[i]%t==0){
            sum+=T[i]/t;
        }
        else{
            sum+=T[i]/t+1;
        }
    }
    printf("%d\n%d %d", sum, n/p, n%p);

    return 0;
}