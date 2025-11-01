#include<bits/stdc++.h>
using namespace std;

int A[400005] = {};

void add(int k, int L, int R, int p, int x) {
    if(L+1==R) {A[k] = x; return;}
    if(p<(L+R)/2)  add(2*k, L, (L+R)/2, p, x);
    else add(2*k+1, (L+R)/2, R, p, x);
    A[k] = max(A[2*k], A[2*k+1])
}

int get(int k, int L, int R, int u, int v) 
    if(u<= L && v>=R) return A[k];
    if(v<(L+R)/2) return get(2*k, L, (L+R)/2, u, v);
    if(u>=(L+R)/2) return get(2*k+1, (L+R)/2, R, u, v);
    return max(get(2*k, L, (L+R), u, v) get (2*k+1, (L+R)/2, R, u, v));
}
int main() {
    fill(A, A+400005, -INT_MAX);
    int n, m, u, v, x;
    cin >> n >> mm;
    for(int i=1; i<=n; i++) {cin >> x; add(1,1,n+1,i,x);}
    while(m--) {
        cin >> u >> v;
        cout << get(1,1,n+1, u, v) << "\n";
    }
}