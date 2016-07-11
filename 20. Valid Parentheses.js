/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    let stack = [];
    for (let i = 0; i < s.length; i++)
    {
        if (s[i] === '(' || s[i] === '[' || s[i] === '{')
            stack.push(s[i]);
        else
        {
            if (s[i] === ')')
            {
                if (stack.length === 0 || (stack.length > 0 && stack.pop() !== '('))
                    return false;
            }
            else if (s[i] === ']')
            {
                if (stack.length === 0 || (stack.length > 0 && stack.pop() !== '['))
                    return false;
            }
            else if (s[i] === '}')
            {
                if (stack.length === 0 || (stack.length > 0 && stack.pop() !== '{'))
                    return false;
            }
        }
    }
    return stack.length === 0 ? true : false;
};
