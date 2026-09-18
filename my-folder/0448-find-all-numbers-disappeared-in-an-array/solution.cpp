class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        
        int n = nums.size();    
        std::vector<int> found(n, 0);

        for (int i = 0; i < n; ++i) {
            found[nums[i] - 1] = 1;
            }

        std::vector<int> res;

        for (int i = 1;i <=n; ++i) {
            if (found[i - 1] == 0) {
                res.push_back(i);
            }
        }

        return res;

    }
};
