#include<bits/stdc++.h>
using namespace std;
int mod = 1e9+7;
int pow(int a, int b){
	int ans=1;
	while(b){
		if (b&1){
			b = b - 1;
			ans *= a;
		}
		else{
			b = b / 2;
			a = a * a;
		}
	}
	return ans;
}
int reverse(int b){
	return pow(b,mod-2);
}
int main(){
	int a,b;
	cin >> a >> b;
	cout << reverse(b);
}
