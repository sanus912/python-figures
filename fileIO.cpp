#include <iostream>
#include <fstream>
#include <cstdlib>
#include <math.h>
int main()
{
    using namespace std;
    char Filename[20];
        
    ofstream outFile;
    outFile.open("fitting_3D.txt");
    for (double x=0.02;x<4;x+=0.04)
        for (double y=4e-5;y<4;y+=0.04)
        {
            outFile << x << "\t" << y << "\t" << 1.6*x*y/(x*x+y*y)*exp(-sqrt(0.8*x*x+y*y));

            outFile << endl;
        }
    outFile.close();
    return 0;
}
