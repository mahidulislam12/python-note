/*#include<stdio.h>
int main(){
    int a;
    sacnf("%c",&a);
    if(a>="a"&&a<="z"){
        int ans=a-32;
        printf("%c\n",ans);

    }
    else{
        int ans=a+32;
        printf("%c\n",ans);
    }
    return 0;
}
*/
/*#include <stdio.h>

int main() {
    char a;  // Use char for character manipulation
    printf("Enter a character: ");
    scanf("%c", &a);

    if (a >= 'a' && a <= 'z') {
        char ans = a - 32;  // Convert lowercase to uppercase
        printf("%c\n", ans);
    } else if (a >= 'A' && a <= 'Z') {
        char ans = a + 32;  // Convert uppercase to lowercase
        printf("%c\n", ans);
    } else {
        printf("Invalid input\n");  // Handle non-alphabetic input
    }

    return 0;
}
*/
/*
#include<stdio.h>
#include<ctype.h>
int main(){
    char lower ,upper;
    printf("enter any lowecast letter=");
    scanf("%c",&lower);
    upper=toupper(lower);
    printf("upper letter=%c",upper);
    return 0;
}
*/
/*
#include<stdio.h>
#include<ctype.h>
int main(){
    char upper,lower;
    printf("enter any upper letter=");
    scanf("%c",&upper);
    lower=tolower(upper);
    printf("enter the final letter=%c",lower);
    return 0;
*/

/*
#include<stdio.h>
#include<ctype.h>
int main(){
    char lower ,upper;
    printf("enter any lowcase =");
    scanf("%c",&lower);
    upper=toupper(lower);
    printf("enter any char=%c",upper);
    return 0;
} */
/*
#include<stdio.h>
int main(){
    int number;
    printf("Decimal number=");
    scanf("%d",&number);
    printf("octal number=%o",number);
    return 0;
}
*/
/*
#include<stdio.h>
int main(){
    int number;
    printf("enter any octal number=");
    scanf("%o",&number);
    printf("decimal number=%d",number);
    return 0;
}
*/
/*
#include<stdio.h>
int main(){
    int number;
    printf("enter any number=");
    scanf("%x",&number);
    printf("enter the number=%d",number);
    return 0;
} 
*/
/*
#include<stdio.h>
int main(){
    int n1,n2,sum;
    float avg;
    printf("enter the two number=");
    scanf("%d %d",&n1,&n2);
    sum=n1+n2;
    printf("%d+%d=%d\n",n1,n2,sum);
    avg=(float)sum/2;
    printf("enter the avg is=%.2f\n",avg);
    return 0;
}
*/
#include <stdio.h>

int main() {
    float base, height, area;
    printf("Enter the base of the triangle: ");
    scanf("%f", &base);
    printf("Enter the height of the triangle: ");
    scanf("%f", &height);
    area = 0.5 * base * height; // Correct formula for area
    printf("The area of the triangle is: %.2f\n", area);
    return 0;
}

