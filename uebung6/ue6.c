/*
Mathias Husted
CoMa Übung 6 - Python Aufgabe (implemented in C)
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Our 2 given functions: f and its inverse
float f(float x) { return x*(x+2); }
float fInverse (float x) { return sqrt(x+1) - 1; }

// 1a)
typedef float (*Function)(float); // Create a typedef to handle the pointer to our function

// Our concat function which concatenates two functions g and gInverse (since in our case we'll use the inverse of g)
float concat(Function g, Function gInverse, float x) {
    return g(gInverse(x));
}

// 1b)
// Let's define a data structure to hold our 4-tuple
typedef struct {
    float val1, val2, err1, err2;
} Tuple;

Tuple generateData(float x) {
    Tuple output;
    output.val1 = concat(fInverse, f, x);
    output.val2 = concat(f, fInverse, x);
    
    // This would work in theory, but is limited by the fact that we are performing the operations on floats, thereby making it useless
    // Alternatively, one could cast the floats to doubles to increase the accuracy
    output.err1 = fabs(output.val1 - x)/fabs(output.val1);
    output.err2 = fabs(output.val2 - x)/fabs(output.val2);

    return output;
}

// 1c)
void generateDataToFile() {

    FILE *fp;

    fp = fopen("daten.txt", "w");
    
    fputs("k\tval1\t\tval2\t\terr1\terr2\n", fp);

    for (unsigned char i = 0; i <= 12; i++) {
        float x = -1 + pow(10, -i);
        Tuple data = generateData(x);
        fprintf(fp, "%d\t", i);
        fprintf(fp, "%f\t", data.val1);
        fprintf(fp, "%f\t\t", data.val2);
        fprintf(fp, "%f\t", data.err1);
        fprintf(fp, "%f\n", data.err2);
    }

    fclose(fp);
}

int main() {
    float x = 392.5;
    float y = f(x);
    float z = concat(f, fInverse, x);
    printf("Initialization: x = %f, y = f(x) = %f, z = f(f^-1(x)) = %f\n\n", x, y, z);

    // 1a)
    printf("1a) %f => g^-1(g(x)) = %f\n\n", x, z);

    // 1b)
    Tuple aufgabeB = generateData(x);
    printf("1b) f^-1(f(%f)) = %f\n", x, aufgabeB.val1);
    printf("    f(f^-1(%f)) = %f\n", x, aufgabeB.val2);
    printf("    Relative error in first value = %f\n", aufgabeB.err1);
    printf("    Relative error in second value = %f\n", aufgabeB.err2);

    // 1c)
    generateDataToFile();
}