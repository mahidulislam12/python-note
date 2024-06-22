 /*1.#include <stdio.h>

int main() {
    for (int i = 20; i <= 100; i++) {
        if ((i >= 40 && i <= 50) || i == 65) {
            continue;
        }
        printf("%d\n", i); 
    }
    return 0;
}*/
/*
#include <stdio.h>

int main() {
    int i = 1;
    while (i <= 100) {
        if (i >= 1 && i <=70) {
            printf("%d\n", i);
        }
        i += 1;
    }
    return 0;
}
*/
/*
#include <stdio.h>

int main() {
    int i = 11;
    while (i <= 100) {
        if (i == 50 || i == 65 || (i >= 90 && i <= 95)) {
            i += 1;
            continue; // Skip 50, 65, and numbers from 90 to 95
        }
        printf("%d\n", i); // Print the number if it's not in the skip range
        i += 1;
    }
    return 0;
}
*/
#include <stdio.h>
int main() {
    int i = -1;
    while (i >= -100) {
        if (i == -65 || (i >= -75 && i <= -70)) {
            i -= 1;
            continue; // Skip -65 and numbers from -70 to -75
        }
        printf("%d\n", i); // Print the number if it's not in the skip range
        i -= 1;
    }
    return 0;
}




