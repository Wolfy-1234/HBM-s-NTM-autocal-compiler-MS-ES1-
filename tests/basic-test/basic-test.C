#include <cstdio>


//this is a test comment
//#clockspeed 10;
int main(){
    int input = 0;
    scanf("Testin%i", &input);
    /*
    this is
    a multiline
    comment
    */
    int output = input * 2;
    printf("Testout%i", output);
    output = output * 2;
    printf("Testout2%i", output);
    while (true) {
        output = output + 1;
        printf("Testout2%i", output);
    }
}