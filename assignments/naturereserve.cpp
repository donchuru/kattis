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

tup prims(vector<vector<tup>>&graph, ll common_source){

    // make it min heap
    priority_queue<tup, vector<tup>, greater<tup>> pq;

    pq.push({0, common_source});

    vector<bool> taken(graph.size(), false);
    ll activate = 0;
    ll tracker = -1; // cause we have extra common node btwn all sources from where we start the domino effect

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

        for (tup edge : graph[v - 1]) {
            ll nb = edge.first;
            ll weight = edge.second;
            if (!taken[nb - 1]) {
                pq.push({weight, nb});
            }
        }
    }
    return {activate, tracker};
}

int main(){
    ll ds; 
    cin >> ds;

    for (ll i = 0; i < ds; i++) {
        ll n, m, l, s;

        cin >> n >> m >> l >> s;

        ll sources[s];
        for (ll j = 0; j < s; j++){
            cin >> sources[j];
        }

        // n + 1 because we need extra node that will be common between all source
        vector<vector<tup>>graph(n+1);
        for (ll j = 0; j < m; j++) {
            ll u, v, w;
            cin >> u >> v >> w;

            graph[u - 1].emplace_back(v, w);
            graph[v - 1].emplace_back(u, w);
        }

        // connect the last(extra) node to the sources
        for (ll source : sources){
            graph[n].emplace_back(source, 0);
        }

        ll total_energy = 0;
        tup res = prims(graph, n + 1);
        ll activate = res.first; ll tracker = res.second;
        total_energy += activate + ((tracker - 1)*l);

        // you dont need to transfer the bytes to the initial sources so deduct the energy needed for this for all their edges(s-1)
        for (ll k = 0; k < s-1; k++){
            total_energy -= (l);
        }
        
        cout << (total_energy) << endl;
    }
    return 0;
}
