/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>
#include <string.h>

void so_strcopy(char str1[],char str2[]){
    int sizeStr1 = strlen(str1);
    for(int i = 0; i <= sizeStr1;i++){
        str2[i] = str1[i];
    }
}
int main()
{
    char str1[] = "cadena";
    int sizeStr1 = strlen(str1);
    char str2[sizeStr1];
    so_strcopy(str1,str2);
    printf("%s",str2);
    return 0;
}
