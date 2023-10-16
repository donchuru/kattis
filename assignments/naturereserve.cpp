/*
  BEGIN-HEADER
  
  Name: David Onchuru
  
  Student-ID: 1647809

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  Competitive Programming 4

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  <List Classmates Here>

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 303/403.

  END-HEADER
*/

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<ll, ll> tup;

tup prims(vector<vector<ll>>&graph, ll source){

    // make it min heap
    struct CompareWeights {
        bool operator()(const tup& a, const tup& b) {
            return a.first > b.first;
        }
    };
    priority_queue<tup, vector<tup>, CompareWeights> pq;

    pq.push({0, source});

    vector<bool> taken(graph.size(), false);
    ll activate = 0;
    ll tracker = 0;

    while (!pq.empty()) {
        ll w = pq.top().first;
        ll v = pq.top().second;
        pq.pop();

        if (taken[v - 1] == true) {
            continue;
        }

        activate += w;
        tracker++;
        taken[v - 1] = true;

        for (ll nb = 0; nb < graph[v - 1].size(); nb++){
            if ( (graph[v - 1][nb] != -1) && (taken[nb] == false) ) {
                pq.push( {graph[v - 1][nb], (nb + 1)} );
            }
        }
        
    }
    // cout << "activate " << activate << " tracker " << tracker << endl;
    return {activate, tracker};
}

int main(){
    ll ds; 
    cin >> ds;

    for (ll i = 0; i < ds; i++) {
        ll n, m, l, s;

        cin >> n >> m >> l >> s;

        vector<ll> sources(s);
        for (ll j = 0; j < s; j++){
            cin >> sources[j];
        }

        vector<vector<ll>>graph(n, vector<ll>(n, -1));
        for (ll j = 0; j < m; j++){
            ll u, v, w;
            cin >> u >> v >> w;

            graph[u - 1][v - 1] = w;
            graph[v - 1][u - 1] = w;
        }

        ll total_energy = 0;
        for (ll source : sources){
            tup res = prims(graph, source);
            ll activate = res.first; ll tracker = res.second;
            total_energy += activate + ((tracker - 1)*l);
        }

        
        cout << (total_energy) << endl;

    }
    return 0;
}
