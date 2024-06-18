#include <stdio.h>

int main() {
    int n;
    scanf("%d",&n);
    float num[n], m=0, sum=0;
    for (int i=0;i!=n;i++){
        scanf("%f",&num[i]);
        if (m<num[i]){
            sum+=m;
            m=num[i];
        }
        else{
            sum+=num[i];
        }
    }
    printf("%.2f",((((sum+m)/m)*100))/n);

    return 0;
}