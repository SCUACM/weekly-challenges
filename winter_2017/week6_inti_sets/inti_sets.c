// Header files
#include <stdio.h>

int checkInti( int, int );

int main(void)
   {
    int students[Q][3], sum = 0;
    
    scanf( "%d %d %d", &students[i][1], &students[i][2], &students[i][3]);
    printOutput(students[i]);

    number = array[2];
    
    while( array[2] <= array[3] )
       {
        if( checkInti( array[1], array[2] ))
           sum += array[2];
        array[2]++;
       }
      
    printf( "%d\n", sum );

    return 0;
   }

int checkInti( int N, int x )
   {
    for( int i = 2; i < N/2; i++ )
       {
        if( N%i == 0 )
           {
            if( x%i == 0 )
               return 0;
           }
       }
    return 1;
   }
