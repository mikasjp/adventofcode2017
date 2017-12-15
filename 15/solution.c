#include <stdio.h>

int main()
{
    // First part
    unsigned long long A = 873;
    unsigned long long B = 583;
    unsigned long long AF = 16807;
    unsigned long long BF = 48271;
    int judge = 0;

    for(int i=0; i<40000000; i++)
    {
        A *= AF;
        A %= 2147483647;

        B *= BF;
        B %= 2147483647;

        if((A & 0xFFFF) == (B & 0xFFFF))
            judge++;
    }

    printf("First part: %u\n", judge);

    // Second part
    A = 873;
    B = 583;
    judge = 0;

    for(int i=0; i<5000000; i++)
    {
        while(1==1)
        {
            A *= AF;
            A %= 2147483647;
            if(A%4==0) break;
        }

        while(1==1)
        {
            B *= BF;
            B %= 2147483647;
            if(B%8==0) break;
        }

        if((A & 0xFFFF) == (B & 0xFFFF))
            judge++;
    }

    printf("Second part: %u\n", judge);
}
