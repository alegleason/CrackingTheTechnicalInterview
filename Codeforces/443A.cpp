#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>//Set ensures there are no repetitions
using namespace std;

int main()
{
  string name;
  int sizeaux = 0;
  //cout << "What is your name? ";
  getline (std::cin, name);
  //cout << "Hello, " << name << "!\n";
  char arr [1001];
  set <char> st;
  vector<int> myvector;
  //cout << name.at(0) << endl;
  //cout << "size: " << name.size();
  int size = name.size();
  for(int i = 0;i < size; i++){
      if(name.at(i) >= 'a' && name.at(i) <= 'z'){
        //myvector.push_back(name.at(i));
        st.insert(name.at(i));
        //cout << arr[i] << endl;
        //sizeaux++;
      }
  }
  
  /*sort(arr, arr+size); 
  
  for(int i =0; i < sizeaux; i++){
      cout << arr[i] << " ";
  }
  
  int sum = 0;
  
  for(int i = 0;i < sizeaux; i++){
      if(arr[i] != arr[i+1] ){
        sum++;
      }
  }
  
  cout << sum;
  
  //cout << myvector.at(0) << endl;*/

  int sizefinal = st.size();

  cout << sizefinal << endl;
  
  return 0;
  
}

