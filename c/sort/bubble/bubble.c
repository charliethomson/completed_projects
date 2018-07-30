#include <stdio.h>
#include <string.h>
#include <stdlib.h>




int greater(int x, int y){
    if (x > y)
        return 1;
    return 0;
}

int main(int array_len){
    srand(time(NULL));
    
    int totalCount = 0;
    int info[array_len];

    for (int i = 0; i < array_len; i++)
        info[i] = rand();
    

    int comp = 0;
    for (int i = 0; i < array_len; i++){
        if (i == array_len - 1)
            printf("%d\n\n", info[i]);
        else
            printf("%d\n", info[i]);
    }
    do {
        int count = 0;
        int x, y;
        for (int i = 0; i < array_len; i++){
            x = info[i]; y = info[i + 1];
            if (greater(x, y) == 1){
                count++; totalCount++;
                info[i] = y; info[i + 1] = x;
            }
        }
        if (count == 0)
            comp = 1;
        else
            count = 0;
    } while (comp == 0);
    for (int i = 0; i < array_len; i++){
        printf("%d\n", info[i]);
    }
    printf("Total swap count %d", totalCount);
}