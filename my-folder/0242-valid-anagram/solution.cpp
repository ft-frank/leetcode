class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.empty() || t.empty()) return false;

        if(s.size() != t.size()) return false;

        vector<int> arr(26,0);

        int n = s.size();
        for(int i=0;i<n;i++) {
            arr[s[i]- 'a']+=1;
            arr[t[i] - 'a']-=1;
        }

        for(auto& ele: arr) {
            if(ele != 0) {
                return false;
            }
        }
        return true;
    }
};
