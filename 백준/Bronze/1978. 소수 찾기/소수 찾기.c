#include <stdio.h>

int prime(int n, int i){
    if (n==1){
        return 0;
    }
    else if (n==0){
        return 0;
    }
    else if (n>i){
        if (n%i==0){
            return 0;
        }
        else{
            return prime(n,i+1);
        }
    }
    else{
        return 1;
    }
}

int main() {
    int n, sum=0, num;
    scanf("%d",&n);
    for (int i=0;i!=n;i++){
        scanf("%d",&num);
        sum+=prime(num,2);
    }
    printf("%d",sum);

    return 0;
}