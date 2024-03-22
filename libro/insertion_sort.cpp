// time-limit: 3000
#include <bits/stdc++.h>

using namespace std;


#define ll long long
#define ld long double
#define all(a) (a).begin(), (a).end()
#define endl "\n"


const int MAX_N = 1e5 + 5;
const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;


void insertion_sort(vector<int> &a) {
  for (int i = 1; i < a.size(); i++){
    int key = a[i];

    int j = i - 1;

    while (j >= 0 && key < a[j]){

      a[j+1] = a[j];

      j--;

    }

    a[j+1] = key;

  }
}

void decreasing_insertion_sort(vector<int> &a){

  for (int i = a.size() - 2; i >= 0; i--){
    int key = a[i];

    int j = i + 1;

    while (j < a.size() && key < a[j]){
      a[j-1] = a[j];
      j++;
    }

    a[j-1] = key;
  }
}

void print_vector(vector<int> &a){
  for (int i = 0; i < a.size(); i++) {
    cout << a[i] << " ";
  }

  cout << endl;

}


void solve() {

  int n;

  cin >> n;

  vector<int> a(n);

  for (int i = 0; i < n; i++) {
    cin >> a[i];
  }

  insertion_sort(a);
  print_vector(a);
  decreasing_insertion_sort(a);
  print_vector(a);
  insertion_sort(a);
  print_vector(a);

}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    // cin >> tc;
    for (int t = 1; t <= tc; t++) {
        // cout << "Case #" << t << ": ";
        solve();
    }
}
