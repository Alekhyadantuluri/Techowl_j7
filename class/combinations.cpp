#include<bits/stdc++.h>
using namespace std;
void comb(int i,int n,int k,int arr[],vector<int>&cs){
    if (i==n){
        if (k==0){
            for(int i = 0 ; i < cs.size() ;i++){
            	cout<<cs[i]<<" ";
            }
            cout<<endl;
        }
    return;
    }
    if (arr[i]<=k){
    	cs.push_back(arr[i]);
    	k=k-arr[i];
    	comb(i,n,k,arr,cs);
    	k=k+arr[i];
    	cs.pop_back();
	}
	comb(i+1,n,k,arr,cs);
}
int main(){
    int arr[3]={1,2,4};
    int k = 3;
    vector<int>cs;
    comb(0,3,k,arr,cs);
}
