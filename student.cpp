#include<iostream>
#include<string>
using namespace std;
class Student
{
    private:
    string name, reg_num, grade;
    public:
    void get_details()
    {
        cout<<"Enter the student name:  "<<endl;
        cin>>name;
        cout<<"Enter the student registration number"<<endl;
        cin>>reg_num;
        
    }
    void grade1()
    {
        cout<<"The student grade is: "<<endl;
        cin>>grade;
    }
    friend int main();
};
int main()
{
    Student m;
    m.get_details();
    m.grade1();
    return 0;
}