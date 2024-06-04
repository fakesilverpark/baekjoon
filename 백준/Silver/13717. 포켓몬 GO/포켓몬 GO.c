#include <stdio.h>

int candy(int m, int k, int b){
    if (m>=k){
        return candy(m/k*2+m%k,k,b+m/k);
    }
    else{
        return b;
    }
}

int main() {
    int n;
    int k,m,max=0,idx,cnt=0,c;
    scanf("%d",&n);
    char name[n][20];
    for (int i=0;i!=n;i++){
        scanf("%s %d %d",name[i],&k,&m);
        c=candy(m,k,0);
        if (c>max){
            max=c;
            idx=i;
        }
        if (c>=1){
            cnt+=c;
        }
    }
    printf("%d\n",cnt);
    printf("%s",name[idx]);

    return 0;
}