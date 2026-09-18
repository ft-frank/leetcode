class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        int n = nums.size();
        vector<int> count(n+1, 0);
        for (int x: nums) ++count[x];

        vector<int> res(2);

        for (int i = 1; i<=n; ++i){
            if (count[i] == 2) {
                res[0] = i;
            }
            else if (count[i] == 0) {
                res[1] = i;
            }
        }

        return res;
    }
};
