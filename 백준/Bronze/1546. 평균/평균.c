#include <stdio.h>

int main() {
    int n;
    scanf("%d",&n);
    float num[n], m=0, sum=0;
    for (int i=0;i!=n;i++){
        scanf("%f",&num[i]);
        sum+=num[i];
        if (m<num[i]){
            m=num[i];
        }
    }
    printf("%.2f",((((sum)/m)*100))/n);

    return 0;
}