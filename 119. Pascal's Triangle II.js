/**
 * @param {number} rowIndex
 * @return {number[]}
 */
var getRow = function(rowIndex) {
    if (rowIndex === 0)
        return [1];
    else if (rowIndex == 1)
        return [1,1];
    let res = [1,1];
    for (let i = 2; i <= rowIndex; i++)
    {
        let temp = [1];
        for (let j = 1; j < res.length; j++)
            temp.push(res[j-1] + res[j]);
        res = temp.concat([1]);
    }
    return res;
};
