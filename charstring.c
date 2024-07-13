#include <stdio.h>

int main() {
    int a[5];
    int sz=sizeof(a)/sizeof(char);
    printf("%d\n",sz);
    printf("%d\n",sizeof(a));
    printf("%d\n",sizeof(int));
    return 0;
}
