#include <stdio.h>

int main() {
    int n,a,c=0,s=0;
    scanf("%d",&n);
    for (int i=0;i!=n;i++){
        scanf("%d",&a);
        if (a==0){
            c=0;
        }
        else{
            c+=1;
            s+=c;
        }
    }
    printf("%d",s);

    return 0;
}