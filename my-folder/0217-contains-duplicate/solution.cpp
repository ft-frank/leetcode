class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        std::unordered_set<int> s;

        for (int num : nums){
            if (s.find(num) != s.end()) {
                return true;
            }
            s.insert(num);
        }
        return false;
    }

};
