#include <stdio.h>

int main() {
    int a,b,c,sum,num[11]={0,};
    scanf("%d %d %d",&a,&b,&c);
    if (a==0 && b==0 && c==0){
        num[0]+=1;
    }
    sum=a*b*c;
    for (int i=0;sum!=0;i++){
        num[sum%10]+=1;
        sum/=10;
    }
    for (int i=0;i!=10;i++){
        printf("%d\n",num[i]);
    }
    return 0;
}