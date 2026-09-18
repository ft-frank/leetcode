class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        

        std::vector<int> stack;
        int val1;
        int val2;
        int new_val;

        for (const auto& item : tokens) {
            
            if (item == "+" || item == "-" || item == "*" || item == "/") {

                val2 = stack[stack.size()-1];
                stack.pop_back();

                val1 = stack[stack.size()-1];
                stack.pop_back();

                if (item == "+") {
                    new_val = val1 + val2;
                }
                else if (item == "-") {
                    new_val = val1 - val2;
                }
                else if (item == "*") {
                    new_val = val1 * val2;
                }
                else if (item == "/") {
                    new_val = val1/val2;
                }

            }
            else{
                new_val = std::stoi(item);
            }

            stack.push_back(new_val);

            }

        
        return stack[0];
        }
};
