#include <bits/stdc++.h>


using namespace std;
typedef long long ll;


struct Book{
    ll id;
    ll score;
};


struct Library {
    ll id;
    ll n;
    ll t;
    ll m;
    vector<Book> books;
    vector<Book> books_scanned;
    bool operator<(const Library l1){
        return t < l1.t;
    };
    bool operator==(const Library &l1){
        return id == l1.id;
    }
};



struct Scan {
    ll lib_id;
    ll day_left;
    ll can_scan;
};

bool comp(const Library &l1,const Library &l2){
    return l1.t < l2.t;
}

bool comp1(const Book &b1,const Book &b2){
    return b1.score > b2.score;
}


int main(){
    ll B, L, D;
    ll days_scaned = 0;
    cin>>B>>L>>D;
    vector<Library> libs;
    vector<ll> book_scores;
    vector<Scan> scan_order;
    set<ll> scanned;
    for(auto i=0;i<B;i++){
        ll s;cin>>s;
        book_scores.push_back(s);
    }
    

    for(auto j=0;j<L;j++){
        ll id, n, t, m;
        vector<Book> books;
        id = j;
        cin>>n>>t>>m;
        
        for(auto i=0;i<n;i++){
            ll c;cin>>c;
            struct Book b;
            b.id =c;
            b.score = book_scores[c];
            books.push_back(b);
        }
        struct Library l;
        l.id = id;
        l.n = n;
        l.t = t;
        l.m = m;
        l.books = books;
        libs.push_back(l);
    }
    sort(libs.begin(), libs.end(), comp);
    for(auto i=0;i<libs.size();i++){
        sort(libs[i].books.begin(), libs[i].books.end(), comp1);
    }
    // for(auto i=0;i< libs.size();i++){
    //     scan_order.push_back(libs[i].id);
    // }
    ll _i = 0;
    while(scan_order.size() < libs.size() && days_scaned <= D){
        // cout<<"\nDay"<<_i<<" Added: "<<libs[_i].id;
        struct Scan s;
        s.lib_id = libs[_i].id;
        days_scaned += libs[_i].t;
        s.can_scan = min(libs[_i].m * (D - days_scaned), (ll)libs[_i].books.size());
        s.day_left = D - days_scaned;
        scan_order.push_back(s);
        // cout<<"\n"<<_i<<" ";
        _i++;
    }

    for(auto i=0;i<scan_order.size();i++){
        cout<<scan_order.size()<<"\n";
        cout<<scan_order[i].lib_id<<" "<<scan_order[i].can_scan<<"\n";
        auto lib = libs.at(scan_order[i].lib_id); //find(libs.begin(), libs.end(), scan_order[i].lib_id);
        for(auto j=0;j<scan_order[i].can_scan;j++){
            if(scanned.count(lib.books[j].id) == 0){
                cout<<lib.books[j].id<<" ";
                scanned.insert(lib.books[j].id);
            }
        }
        cout<<"\n";
    }
    // for(auto x: scan_order){
    //     cout<<x<<"\n";
    // }
    // teesting 
    // for(ll i=0;i<libraries[1].n;i++){
    //     cout<<libraries[1].books[i];
    // }  
    // cout<<libraries[0].books[1];
    // while(D--){

    // }
    return 0;
}