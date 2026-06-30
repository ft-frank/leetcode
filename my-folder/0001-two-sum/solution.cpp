class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
      std::unordered_map<int, int> seen;

      for (int i=0; i < nums.size(); i++) {
        int looking = target - nums[i];
        if (seen.find(looking) != seen.end() ) {
            return {i, seen[looking]};

        }
        seen[nums[i]] = i;
      }      
      return {};
    }
};

