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


// tuple <int, int, int> sub_array;
typedef struct sub_array{
  int low;
  int high;
  int sum;
} sub_array;

sub_array max_cross_subarray(vector<int> a, int start, int mid, int end){
  int sum = 0;
  int max_left = INT_MIN;
  int left_index = mid;

  for (int i = mid; i >= start; i--){
    sum += a[i];
    if (sum > max_left){
      left_index = i;
      max_left = sum;
    }
  }

  sum = 0;
  int max_right = INT_MIN;
  int right_index = mid + 1;
  for (int i = mid + 1; i <= end; i++){
    sum += a[i];
    if (sum > max_right){
      left_index = i;
      max_right = sum;
    }
  }

  sub_array res = {left_index,right_index, max_left + max_right};
  return res;
}


sub_array max_subarray_sum(vector<int> a, int start, int end){
  if (start == end){
    return {start,end, a[start]};
  }
  int mid = (start + end)/2;

  sub_array max_left = max_subarray_sum(a, start, mid);

  sub_array max_right = max_subarray_sum(a, mid + 1, end);

  sub_array max_cross = max_cross_subarray(a, start, mid, end);

  if (max_left.sum >= max_right.sum && max_left.sum >= max_cross.sum){
    return max_left;
  }
  else if (max_right.sum >= max_left.sum && max_right.sum >= max_cross.sum){
    return max_right;
  }
  else{
    return max_cross;
  }

}

void solve() {

  int n; cin >> n;
  vector<int> a(n);
  for (int i = 0; i < n; i++) {
    cin >> a[i];
  }

  // store the difference between elements
  vector<int> diff(n - 1);
  for (int i = 0; i < n - 1; i++) {
    diff[i] = a[i + 1] - a[i];
  }

  sub_array res = max_subarray_sum(diff, 0, n - 2);

  // print the buy and sell days
  cout << res.low << " " << res.high + 1 << " " << res.sum << endl;
    
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
