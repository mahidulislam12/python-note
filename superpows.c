/*#include<stdio.h>
int main(){
    //char a[2]={'w','k'};
    char a[2]="fd";
    for(int i=0;i<2;i++){
        printf("%c",a[i]);
    }
    return 0;
}
*/
#include<stdio.h>
int main(){
    char a[5]="berw\0";
    printf("%s",a);
    return 0;
}

