#include <bits/stdc++.h>

using namespace std;

#define endl "\n"

int insertion_sort(vector<int> a) {
  int comparisons = 0;

  int n = a.size();
  for (int i = 1; i < n; i++) {
    int key = a[i];
    int j = i - 1;
    while (j >= 0 && a[j] > key) {
      comparisons++;
      a[j + 1] = a[j];
      j--;
    }
    if (j >= 0) {
      comparisons++;
    }
    a[j + 1] = key;
  }

  return comparisons;
}

int merge(vector<int> &a, int p, int q, int r) {
  int comparisons = 0;

  int nl = q - p + 1;
  int nr = r - q;
  vector<int> L(nl), R(nr);
  for (int i = 0; i < nl; i++) {
    L[i] = a[p + i];
  }
  for (int i = 0; i < nr; i++) {
    R[i] = a[q + 1 + i];
  }

  int i = 0, j = 0, k = p;
  while (i < nl && j < nr) {
    comparisons++;
    if (L[i] <= R[j]) {
      a[k] = L[i];
      i++;
    } else {
      a[k] = R[j];
      j++;
    }
    k++;
  }

  while (i < nl) {
    a[k] = L[i];
    i++;
    k++;
  }

  while (j < nr) {
    a[k] = R[j];
    j++;
    k++;
  }

  return comparisons;
}

void solve() {
  int n;
  cin >> n;

  vector<int> a(n);
  for (int &x : a) {
    cin >> x;
  }

  vector<int> b = a;

  int insertion_comparisons = insertion_sort(a);

  int merge_comparisons = 0;

  function<void(int, int)> merge_sort = [&](int l, int r) {
    if (l < r) {
      int m = l + (r - l) / 2;
      merge_sort(l, m);
      merge_sort(m + 1, r);
      merge_comparisons += merge(b, l, m, r);
    }
  };

  merge_sort(0, n - 1);

  cout << insertion_comparisons << endl;
  cout << merge_comparisons << endl;
}

int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  int tc = 1;
  // cin >> tc;
  for (int t = 1; t <= tc; t++) {
    // cout << "Case #" << t << ": ";
    solve();
  }
}
