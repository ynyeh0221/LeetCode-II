/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    let en = 1;
    for (let i = digits.length-1; i >= 0; i--)
    {
        let temp = digits[i] + en;
        if (temp < 10)
        {
            digits[i] = temp;
            return digits;
        }
        else
            digits[i] = temp - 10;
    }
    digits.splice(0, 0, 1);
    return digits;
};
