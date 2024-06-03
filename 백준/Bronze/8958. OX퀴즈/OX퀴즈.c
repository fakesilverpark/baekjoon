#include <stdio.h>

int score(char a[], int i, int s, int c, int l){
    if (a[i]!='\0'){
        if (a[i]=='X'){
            return score(a,i+1,s,0,0);
        }
        else{
            if (l==1){
                return score(a,i+1,s+c+1,c+1,1);
            }
            else{
                return score(a,i+1,s+1,1,1);
            }
        }
    }
    return s;
}

int main() {
    int n;
    char a[80];
    scanf("%d",&n);
    for (int i=0;i!=n;i++){
        scanf("%s",a);
        printf("%d\n",((a[0]=='O')?score(a,1,1,1,1):score(a,1,0,0,0)));
    }
    return 0;
}