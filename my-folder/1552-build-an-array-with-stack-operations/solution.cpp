class Solution {
public:
    vector<string> buildArray(vector<int>& target, int n) {
        
        int pointer {0};

        std::vector<int> stack;
        std::vector<std::string> operations;
        int value;
        for (int value = 1; value <= n; ++value) {
            stack.push_back(value);
            operations.push_back("Push");
            
            if (target[pointer] == value) 
            {
                ++pointer;
            }
            else 
            {
                stack.pop_back();
                operations.push_back("Pop");
            }

            if (pointer >= target.size()) {
                return operations;
            }

        }

        return operations;
    }
};
