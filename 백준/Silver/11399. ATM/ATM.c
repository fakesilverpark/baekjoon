#include <stdio.h>

int main() {
    int n,r=0;
    scanf("%d",&n);
    int num[n];
    for (int i=0;i!=n;i++){
        scanf("%d",&num[i]);
    }
    for (int i=0;i!=n;i++){
        for (int j=0;j!=n-1;j++){
            if (num[j]>=num[j+1]){
                int num1=num[j];
                int num2=num[j+1];
                num[j]=num2;
                num[j+1]=num1;
            }
            else{
                continue;
            }
        }
    }
    for (int i=0;i!=n;i++){
        r+=num[i]*(n-i);
    }
    printf("%d",r);
    return 0;
}