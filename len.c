/*#include<stdio.h>
int main(){
    char a[100];
    printf("enter the char[c]:");
    scanf("%s",&a);
    int count=0;
    for(int i=0;a[i]!='\0';i++){
        count++;
    }
    printf("%d\n",count);
    return 0;
}

#include<stdio.h>
int main(){
    char s[100];
    printf("enter the char [%%c]:");
    scanf("%d",&s);
    int i=0;
    int count=0;
    while(s[i]!='\0'){
        count++;
        i++;
    }
    printf("%d\n",count);
    return 0;
}
*/
//buit in function
#include<stdio.h>
#include<string.h>
int main(){
    char a [100];
    printf("enter the char[%%c]:");
    scanf("%s",&a);
    int len=strlen(a);
    printf("%d\n",len);
    return 0;
}

