#include <stdio.h>

int main() {
    int l,t,c=0;
    scanf("%d",&l);
    for (int i=0;i!=7;i++){
        scanf("%d",&t);
        c+=l-t;
        if (l-t!=1 && l-t!=-1){
            c=500;
            break;
        }
        l=t;
    }
    printf((c==7)?"descending":((c==-7)?"ascending":"mixed"));
    
    return 0;
}