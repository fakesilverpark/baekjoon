#include <stdio.h>

int main() {
    int N;
    int h,w,n,idx;
    scanf("%d",&N);
    for (int i=0;i!=N;i++){
        scanf("%d %d %d",&h,&w,&n);
        idx=(n%h==0)?(n/h):(n/h+1);
        if (idx>=10){
            printf("%d%d\n",((n%h==0)?h:n%h),idx);
        }
        else
         printf("%d0%d\n",((n%h==0)?h:n%h),idx);
        
    }
    return 0;
}