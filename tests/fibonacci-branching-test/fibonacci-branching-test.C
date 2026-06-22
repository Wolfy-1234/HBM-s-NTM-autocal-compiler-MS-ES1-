#include <cstdio>


//this is a test comment
//#clockspeed 2;
int main(){
    int var1 = 1;
    int var2 = 0;
    int var3 = 0;
    while (true) {
        var3 = var1 + var2;
        var1 = var2;
        var2 = var3;
        printf("fibona%i", var3);
    }
}