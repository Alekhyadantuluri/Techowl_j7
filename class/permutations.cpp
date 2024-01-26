#include<bits/stdc++.h>
using namespace std;
void per(string s,string s1,vector<int>&freq){
	if (s1.size() == s.size()){
		cout << s1 <<endl;
		return;
	}
	for(int i = 0 ; i < s.size() ; i++){
		if (freq[i]==0){
			freq[i]=1;
			per(s,s1+s[i],freq);
			freq[i]=0;
			
		}
	}
}
int main(){
	string s;
	cin >> s;
	string s1="";
	vector<int>freq(s.size(),0);
	per(s,s1,freq);
}
