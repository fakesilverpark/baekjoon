#include <stdio.h>

int main() {
    int n;
    scanf("%d",&n);
    float num, m=0, sum=0;
    for (int i=0;i!=n;i++){
        scanf("%f",&num);
        sum+=num;
        if (m<num){
            m=num;
        }
    }
    printf("%.2f",(((sum)/m)*100)/n);

    return 0;
}