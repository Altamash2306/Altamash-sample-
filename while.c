#include<stdio.h>

int main()
{
    int i;
    int j=7;

    for(i=0; i<=10; i++)
    {
        printf("%d x %d = %d\n",j, i,i*j );
    }
    return 0;
}