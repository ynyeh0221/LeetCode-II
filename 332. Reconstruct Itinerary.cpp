class Solution {
public:
    vector<string> findItinerary(vector<pair<string, string>> tickets) {
        vector<string> res;
        map<string, multiset<string>> from_to;  
        for(auto val:tickets)
            from_to[val.first].insert(val.second);
        stack <string> s;  
        s.push("JFK");
        
        while(!s.empty())
        {  
            string temp=s.top();  
            if(from_to.find(temp) != from_to.end() && from_to[temp].size() > 0)  
            {  
                s.push(*from_to[temp].begin());
                from_to[temp].erase(from_to[temp].begin());
            }
            else
            {
                res.insert(res.begin(), temp);
                s.pop();
            }
        }
        return res;  
    }
};
