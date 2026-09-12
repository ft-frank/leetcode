class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
       
       std::vector<int> response(nums.size(), 0);

       for (int i = 0; i < nums.size(); ++i) {
            for (int j = 0; j < nums.size(); ++j) {
                if (nums[i] > nums[j]) {
                    ++response[i];
                }
            }

       }
       return response;

    }
};
