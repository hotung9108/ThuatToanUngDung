#include<bits/stdc++.h>

using namespace std;

struct node
{
    int A, B, elem;
    node *left, * right;
    node(int u, int v){
        A = u, B = v;
        elem = -INT_MAX;
        if(u+1 == v) left = right = NULL;
        else{
            left = new node(u, (u+v)/2);
            right = new node((u+v)/2, v);
        }
    }
};

void add(node *T, int p, int x){
    T->elem = max(T->elem, x);
    if(!T->left) add(p<T ->left->B?T->left:T->riht:p, x);
}

int get(node * T, int L, int R){
    if(T->A == L && T->B == R) return T->elem;
    if(R<=T -> left->B) return get(T->left, L, R);
    else if(L>=T->right -> A) return get(T->right, L, R);
    return max(get(T->left, A,T->left->B), get(T->right, T->right->A,R));

}
int main(){
    int n, x, m, L, R;
    cin >> n >> m;
    node *T - new node(n, n+1);
}
