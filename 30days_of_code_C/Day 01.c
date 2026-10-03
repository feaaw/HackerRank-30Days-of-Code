#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int i = 4;
    double d = 4.0;
    char s[] = "HackerRank ";

    
    // Declare second integer, double, and String variables.
    int input_integer;
    double input_double;
    char input_string[100];
    // Read and save an integer, double, and String to your variables.
    scanf("%d", &input_integer);
    scanf("%lf", &input_double);
    scanf(" %99[^\n]", input_string);
    // Print the sum of both integer variables on a new line.
    printf("%d\n", i + input_integer);
    // Print the sum of the double variables on a new line.
    printf("%.1lf\n", d + input_double);
    // Concatenate and print the String variables on a new line
    // The 's' variable above should be printed first.
    printf("%s%s\n", s, input_string);
    return 0;
}
