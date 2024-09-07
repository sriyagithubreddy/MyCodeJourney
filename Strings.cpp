#include <iostream>
#include <string>
using namespace std;

int main() {
	// Complete the program
    string a,b,c;
    cin>>a;
    cin>>b;
    c=a+b;
    cout<<a.length()<<" "<<b.length()<<"\n";
    cout<<c<<"\n";
    char temp = b[0]; 
    b[0] = a[0];
    a[0] = temp; 
    cout<<a<<" "<<b;
    return 0;
}

