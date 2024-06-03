#include <stdio.h>

int main() {
    int n[10],sum=0,fut=0;
    for (int i=0;i!=10;i++){
        scanf("%d",&n[i]);
    }
    fut=n[0];
    for (int i=0;i!=10;i++){
        fut+=n[i+1];
        sum+=n[i];
        if ((fut-100)>(100-sum)){
            printf("%d",sum);
            break;
        }
        else if ((fut-100)==(100-sum)){
            printf("%d",fut);
            break;
        }
        else{
            continue;
        }
    }
    return 0;
}