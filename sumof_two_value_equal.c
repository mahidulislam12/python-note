#include<stdio.h>

int main() {
    int a;
    printf("Enter the value of a: ");
    scanf("%d", &a);
    
    int arr[a];
    printf("Enter the array elements:\n");
    for(int i = 0; i < a; i++) {
        scanf("%d", &arr[i]);
    }
    
    int x;
    printf("Enter the value of x: ");
    scanf("%d", &x);
    
    int flag = 0;
    
    for(int i = 0; i < a - 1; i++) {
        for(int j = i + 1; j < a; j++) {
            if(arr[i] + arr[j] == x) { // শর্তটি সঠিকভাবে চেক করা
                flag = 1;
                break; // জোড়া পেলে লুপ থেকে বেরিয়ে আসা
            }
        }
        if(flag == 1) {
            break; // বাহ্যিক লুপ থেকেও বেরিয়ে আসা
        }
    }
    
    if(flag == 1) {
        printf("Yes\n"); // জোড়া পাওয়া গেলে "Yes" প্রিন্ট করবে
    } else {
        printf("No\n"); // জোড়া না পাওয়া গেলে "No" প্রিন্ট করবে
    }
    
    return 0;
}
