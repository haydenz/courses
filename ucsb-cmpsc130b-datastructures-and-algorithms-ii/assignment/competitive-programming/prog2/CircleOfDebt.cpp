/*
https://open.kattis.com/problems/debt
*/

#include<iostream>
#include<cstdio>
using namespace std;
 
const int inf = 1000000000;
int deno[7]={0,100,50,20,10,5,1};
int acc[10][10],dp[10],res,cnt;
const int ppl_num=3, deno_num=6;
 
bool mod(int x,int mon) {
    switch(x) {
        case 1:return mon % 100 == 0;
        case 2:return mon % 50 == 0;
        case 3:case 4:return mon % 10 == 0;
        case 5:return mon % 5 == 0;
        case 6:return true;
    }
}
 
void dfs(int x)
{
    if(x==0) {if(dp[1]==dp[2]&&dp[2]==dp[3]) res=min(res, cnt); return;}
    if(cnt>=res) {
        return;
    }
    if(!mod(x,dp[1]-dp[2]) || !mod(x,dp[2]-dp[3])) {
        return;
    }

    for(int k=1;k<=ppl_num;k++) {
        k--;
        int a=(k+1)%ppl_num+1, b=(k+2)%ppl_num+1; 
        k++;
        for(int i=0;i<=acc[k][x];i++) {
            for(int j=0;j<=acc[k][x]-i;j++) {
                dp[k]-=i*deno[x]; 
                dp[b]+=j*deno[x]; 
                cnt+=i+j;
                dfs(x-1);
                dp[k]+=i*deno[x]; 
                dp[b]-=j*deno[x]; 
                cnt-=i+j;
            
            }
        }
        for(int i=0;i<=acc[a][x];i++) {
            for(int j=0;j<=acc[b][x];j++) {
                dp[k]+=i*deno[x]; 
                dp[b]-=j*deno[x]; 
                cnt+=i+j;
                dfs(x-1);
                dp[k]-=i*deno[x]; 
                dp[b]+=j*deno[x]; 
                cnt-=i+j;
            }
        }
    }
}
 
void debt_circle()
{
    for (int i=1; i<=ppl_num; ++i) {
        scanf("%d",&dp[i]);
    }

    for (int i=1; i<=ppl_num; ++i) {
        for (int j=1; j<=deno_num; j++) {
            scanf("%d",&acc[i][j]);
        }
    }
    res=inf;cnt=0;
    dfs(6);
    if(res==inf) {
        cout<<"impossible"<<endl;
    } else {
        cout<<res<<endl;
    }
}
 
int main()
{
    int test; cin>>test;
    for (int t=0; t<test; ++t) {
        debt_circle();
    }
    return 0;
}

