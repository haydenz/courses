/*
https://open.kattis.com/problems/convexhull
*/

#include <bits/stdc++.h>
using namespace std;
using Point = pair<long long,long long>; 

long long sq(long long a) { 
    return a*a; 
}

// L2 norm
long long norm_l2(const Point& p) { 
    return sq(p.first)+sq(p.second);  // x^2 + y^2
}

// basic operations
Point operator-(const Point& l, const Point& r) { 
    return Point(l.first-r.first,l.second-r.second); 
}

// cross product
long long cross(const Point& a, const Point& b) { 
    return a.first*b.second-a.second*b.first; 
} 

long long cross(const Point& p, const Point& a, const Point& b) {
    return cross(a-p,b-p); 
}

vector<int> GrahamScan(const vector<Point>& points) {
    // Find the bottommost point 
    long long y_min = points[0].second;
    int min_idx = 0; 
    for (int i = 1; i < int(points.size()); i++) { 
        long long y = points[i].second; 
        if ((y < y_min) || (y_min == y && points[i].first < points[min_idx].first)) {
            y_min = points[i].second;
            min_idx = i;                
        }
    }

    vector<int> rest, hull{min_idx};
    // points except for the bottonmost
    for (int i=0; i < int(points.size()); ++i) {
        if (points[i] != points[min_idx]) {
            rest.push_back(i);
        }
    }

    sort(begin(rest), end(rest), [&](int a, int b) {
        Point x = points[a]-points[min_idx];
        Point y = points[b]-points[min_idx];
        long long t = cross(x,y);
        return t != 0 ? t > 0 : norm_l2(x) < norm_l2(y);
    });

    for (int i=0; i<int(rest.size()); ++i) {
        int c = rest[i];
        while (hull.size() > 1 && cross(points[end(hull)[-2]], points[hull.back()], points[c]) <= 0) {
            hull.pop_back();
        }
        hull.push_back(c); 
    }
    return hull;
}


int main()
{
    int n;
    do {
        cin >> n;
        if (n == 0) break;

        // read in point pairs
        vector<Point> points(n);
        for (int i=0; i<n; ++i) {
            long long a, b; cin >> a >> b;
            points[i] = Point(a, b);
        }

        // solve the convex hull problem
        vector<int> res = GrahamScan(points);
        
        // print the results
        cout << res.size() << '\n';
        for (int i=0; i<int(res.size()); ++i) {
            cout << points[res[i]].first << " " << points[res[i]].second << '\n';
        }
    } while (n > 0);
}
