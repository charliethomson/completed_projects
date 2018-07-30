#include <stdio.h>
#include <math.h>
#include <string.h>


int absoluteValue(int x){
    if (x < 0)
        return x * -1;
    return x;
}

int exponent(int x, int y){
    /* where x ^ y */
    int ret = x;
    for (int i = 0; i < y; i++){
        ret *= x;
    }
    return ret;
}

int getBlockSize(int cidr){
    return exponent(2, (absoluteValue(8 - (cidr % 8))));
}



int main(){
    char address[19]; // max characters for an ip address and cidr is 19 chars w/ dots and slashes

    printf("Enter your address here: ");
    fgets(address, 19, stdin);
    printf("%s", address);

    
    return 0;
}