
#include<iostream>

using namespace std;


class Demo
{
    public:
        int no1;
        int no2;
    Demo(int A = 0,int B = 0):
    {
        this->no1 = A;
        this->no2 = B;

        cout<<"Inside Consturctor...\n";
    }
    ~Demo()
    {
        cout<<"Inside Desturctor...\n";
    }


    void Display()
    {
        cout<<"Value of no1 is : "<<this->no1;
        cout<<"Value of no2 is : "<<this->no2;
    }
};
int main()
{
    cout<<"Inside Main...\n";

    Demo obj1();
    Demo obj2();
    

    obj1.Display();
    obj2.Display();

    cout<<"End of Main.\n";
    return 0 ;
}

