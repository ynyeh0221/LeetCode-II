class Solution {
public:
    bool isValid(string s) {
    stack <char> stack;
    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] == '(' || s[i] == '[' || s[i] == '{')
            stack.push(s[i]);
        else
        {
            if (s[i] == ')')
            {
                if (stack.size() == 0)
                    return false;
                else
                {
                    char temp = stack.top();
                    stack.pop();
                    if (stack.size() > 0 && temp != '(')
                        return false;
                }
            }
            else if (s[i] == ']')
            {
                if (stack.size() == 0)
                    return false;
                else
                {
                    char temp = stack.top();
                    stack.pop();
                    if (stack.size() > 0 && temp != '[')
                        return false;
                }
            }
            else if (s[i] == '}')
            {
                if (stack.size() == 0)
                    return false;
                else
                {
                    char temp = stack.top();
                    stack.pop();
                    if (stack.size() > 0 && temp != '{')
                        return false;
                }
            }
        }
    }
    return stack.size() == 0 ? true : false;
    }
};
